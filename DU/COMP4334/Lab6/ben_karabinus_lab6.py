# Ben Karabinus Lab 6 Fall 2022

# Databricks notebook source
# MAGIC %md
# MAGIC # __Lab 6 Advanced Spark SQL__

# COMMAND ----------

"""import necessary packages"""

from pyspark.sql import functions as f

# COMMAND ----------

"""create new storage location for lab 6 data"""

dbutils.fs.cp("dbfs:/FileStore/tables/lab5/Master.csv", "dbfs:/FileStore/tables/lab6/Master.csv")
dbutils.fs.mv("dbfs:/FileStore/tables/AllstarFull.csv", "dbfs:/FileStore/tables/lab6/AllStarFull.csv")
dbutils.fs.mv("dbfs:/FileStore/tables/Teams.csv", "dbfs:/FileStore/tables/lab6/Teams.csv")

# COMMAND ----------

"""read in the baseball datarames and perform join operations"""

# read in Master convert to dataframe
master = "dbfs:/FileStore/tables/lab6/Master.csv"
masterDF = spark.read.format("csv").option("header", True).option("inferSchema", True).load(master).select(["playerID", "nameFirst", "nameLast"])

# read in AllStarFull and convert to dataframe
allstar = "dbfs:/FileStore/tables/lab6/AllStarFull.csv"
allstarDF = spark.read.format("csv").option("header", True).option("inferSchema", True).load(allstar).select(["playerID", "teamID"])

# read in Teams and convert to dataframe
teams = "dbfs:/FileStore/tables/lab6/Teams.csv"
teamsDF = spark.read.format("csv").option("header", True).option("inferSchema", True).load(teams).select(["teamID", "name"])

# join allstarDF and teamsDF
allstarsTeams = allstarDF.join(f.broadcast(teamsDF), ['teamID'], 'inner')

# join masterDF and allstarsTeamsDF
allstarsMaster = masterDF.join(f.broadcast(allstarsTeams), ['playerID'], 'inner').distinct()

# show the final dataframe
allstarsMaster.filter(f.col('teamID')show()

# COMMAND ----------

"""create the parquet file, partition by team name for read performance"""

path = "dbfs:/FileStore/tables/lab6/allstarMasterParque"
allstarsMaster.write\
     .partitionBy("name")\
     .parquet(path)

# COMMAND ----------

"""test the parquet file by reading in as dataframe and filtering to find all Rockies players"""

rockiesAllstars = spark.read.format('parquet').load(path).filter(f.col('name') == 'Colorado Rockies')
print("The Colorado Rockies have", rockiesAllstars.count(), "allstars.")
rockiesAllstars.show(24)
