# Ben Karabinus
# Databricks notebook source
# MAGIC %md
# MAGIC # __Lab 8 Spark Streaming__

# COMMAND ----------

"""load the required packages"""

from pyspark.sql import Row, functions as f
from pyspark.sql.types import StructType, StructField, LongType, StringType, TimestampType

# COMMAND ----------

"""create file storage location for lab 8 data"""

dbutils.fs.mv("dbfs:/FileStore/tables/FIFA.csv", "dbfs:/FileStore/tables/lab8/FIFA.csv")

# COMMAND ----------

"""valid streaming approach by build stream components in staticc environment"""

# specify the dataframe schema
fifaSchema = StructType( \
                        [StructField('ID', LongType(), True), \
                        StructField('lang', StringType(), True), \
                        StructField('Date', TimestampType(), True), \
                        StructField('Source', StringType(), True), \
                        StructField('len', LongType(), True), \
                        StructField('Orig_Tweet', StringType(), True), \
                        StructField('Tweet', StringType(), True), \
                        StructField('Likes', LongType(), True), \
                        StructField('RTs', LongType(), True), \
                        StructField('Hashtags', StringType(), True), \
                        StructField('UserMentionNames', StringType(), True), \
                        StructField('UserMentionID', StringType(), True), \
                        StructField('Name', StringType(), True), \
                        StructField('Place', StringType(), True), \
                        StructField('Followers', LongType(), True), \
                        StructField('Friends', LongType(), True), \
])

# specify file path to load the initial dataset then load FIFA.csv
path = "dbfs:/FileStore/tables/lab8/FIFA.csv"

fifaDF = spark.read.format("csv")\
                   .option("header", True)\
                   .schema(fifaSchema)\
                   .option("ignoreLeadingWhiteSpace", True)\
                   .option("mode", "dropMalformed")\
                   .load(path).persist()

# repartition the data
# print the number of partitions prior to transformation
print(fifaDF.rdd.getNumPartitions())
# orderBy "Date" and repartition the data to 25 partitions
# order by should only be  used for testing, when creating stream the data should be randomly shuffled
fifaDF = fifaDF.orderBy("Date").repartition(25).persist()
print(fifaDF.rdd.getNumPartitions())
# specify path to write data
outPath = "dbfs:/FileStore/tables/lab8/partitioned"
# remove any existing files in path
dbutils.fs.rm(outPath, True)
# write the data to specified path
fifaDF.write.format("csv").option("Hader", True).save(outPath)
# create a static window for testing
fifaStaticWindow = fifaDF.select(f.col("ID"), f.col("Date"), f.col("HashTags"))\
                         .filter(f.col("Hashtags")\
                         .isNotNull()).withColumn("HashTags", f.explode(f.split("HashTags", ",")))\
                         .groupBy(f.window("Date", "60 minutes", "30 minutes"), "Hashtags")\
                         .agg(f.count("HashTags").alias("count"))\
                         .filter(f.col("count") > 100)

# print results of the static window testing
fifaStaticWindow.orderBy(f.col("window"), f.col("count")).show(truncate=False)


# COMMAND ----------

"""repartition the data in an unordered fashion for realistic simulation"""

# specify file path to load the initial dataset then load FIFA.csv
path = "dbfs:/FileStore/tables/lab8/FIFA.csv"

fifaDF = spark.read.format("csv")\
                   .option("header", True)\
                   .schema(fifaSchema)\
                   .option("ignoreLeadingWhiteSpace", True)\
                   .option("mode", "dropMalformed")\
                   .load(path).persist()

# repartition data
fifaDF = fifaDF.repartition(25).persist()
# specify path to write data
outPath = "dbfs:/FileStore/tables/lab8/partitionedUnordered"
# remove any existing files in path
dbutils.fs.rm(outPath, True)
# write the data to specified path
fifaDF.write.format("csv").option("Hader", True).save(outPath)

# COMMAND ----------

"""stream the world cup tweets"""

# source
sourceStream = spark.readStream\
                    .format("csv")\
                    .option("header", True)\
                    .schema(fifaSchema)\
                    .option("maxFilesPerTrigger", 1)\
                    .load(outPath)

# query
reducedStream = sourceStream.withWatermark("Date", "24 hours")\
                            .select(f.col("ID"), f.col("Date"), f.col("HashTags"))\
                            .filter(f.col("Hashtags").isNotNull()).withColumn("HashTags", f.explode(f.split("HashTags", ",")))\
                            .groupBy(f.window("Date", "60 minutes", "30 minutes"), "Hashtags")\
                            .agg(f.count("HashTags")\
                            .alias("count"))\
                            .filter(f.col("count") > 100)


# sink
sinkStream = reducedStream.writeStream.outputMode("complete")\
                          .format("memory")\
                          .queryName("hashTagCount")\
                          .trigger(processingTime='10 seconds')\
                          .option("truncate", False)\
                          .start()

# COMMAND ----------

"""run a query on the HashTag stream to test"""

currentStream = spark.sql("SELECT * FROM hashTagCount")
currentStream.show(truncate=False)
