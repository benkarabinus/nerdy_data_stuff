# Ben Karabinus Lab 5

# Databricks notebook source
# MAGIC %md
# MAGIC # __Lab 5 Basic Spark SQL__

# COMMAND ----------

"""import the necessary libraries and instantiate spark object"""

from pyspark.sql import Row, functions
from pyspark.sql.types import StructType, StructField, LongType, StringType
sc = spark.sparkContext

# COMMAND ----------

"""create file storage location for lab 5 data"""

dbutils.fs.mv("dbfs:/FileStore/tables/Master.csv", "dbfs:/FileStore/tables/lab5/Master.csv")
        

# COMMAND ----------

"""read in Master.csv as a text file, prapare data, create datframe"""

# read in the csv and persist
master = sc.textFile("dbfs:/FileStore/tables/lab5").map(lambda x: x.split(","))
master.persist()
# remove the header
header = master.collect()[0]
master = master.filter(lambda x: x != header)
# extract desired feature names from the header
features = ['playerID', 'birthCountry', 'birthState', 'height']
colnames  = [(item, index) for (index, item) in enumerate(header) if item in features]
print(colnames)
# filter null values from the height column, print count before and after for sanity check
print(master.count())
master = master.filter(lambda x: x[17] != '')
print(master.count())
# create the dataframe schema
masterSchema = StructType([\
                         StructField('playerID', StringType(), False),\
                         StructField('birthCountry', StringType(), False),\
                         StructField('birthState', StringType(), False),\
                         StructField('height', LongType(), False)
                         ])
# create a "Row" RDD
masterRows = master.map(lambda x: Row(playerID=x[0],\
                                      birthCountry=x[4],\
                                      birthState=x[5],\
                                      height=int(x[17])))
# create the dataframe and display
masterDF = spark.createDataFrame(masterRows, masterSchema)
masterDF.show()

# COMMAND ----------

"""find the number of players born in Colorado"""

# register the dataframe as a temp table
masterDF.createOrReplaceTempView("state")
# find the number of players in Colorado using Spark SQL
spark.sql("SELECT COUNT(playerID) AS playerCountCO FROM state WHERE birthState = 'CO'").show()
# find the number of players in Colorado using Spark dataframe functions
masterDF.filter(masterDF['birthState'] == 'CO').\
                agg(functions.count(masterDF['birthState']).\
                alias('playerCountCO')).show()

# COMMAND ----------

"""list the average height by birth country of all players ordered from highest to lowest"""

# Spark SQL
spark.sql("SELECT birthCountry, AVG(height) FROM state GROUP BY birthCountry ORDER BY AVG(height) DESC").show()
# Spark dataframe functions
masterDF.select(masterDF['birthCountry'], masterDF['height']).\
                groupBy(masterDF['birthCountry']).\
                agg(functions.avg(masterDF['height'])).\
                sort('avg(height)', ascending=False).show()
