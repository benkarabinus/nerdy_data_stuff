# Ben Karabinus Lab 3
# Databricks notebook source
# MAGIC %md
# MAGIC # __Lab 3: Map Reduce and Web Indexing__

# COMMAND ----------

"""Setup file directories for lab3"""

# loop through files in default table storage
for path in dbutils.fs.ls("dbfs:/FileStore/tables/"):
    
    # if test file move to lab3short else if full file move to fulllab
    if "shortLab" in path[0]:
        dbutils.fs.mv(path[0], "dbfs:/FileStore/tables/lab3short/" + path[0][path[0].rindex("/")+1:])
    elif "fullLab" in path[0]:
        dbutils.fs.mv(path[0], "dbfs:/FileStore/tables/lab3full/" + path[0][path[0].rindex("/")+1:])

# COMMAND ----------

"""perform map reduce on lab3short data"""

# initiate context
sc = spark.sparkContext
# load the lab3short data, split into a list of site references, and persist the RDD for later use
short = sc.textFile("dbfs:/FileStore/tables/lab3short").map(lambda x: x.split(" "))
short.persist()
# create key/value pairs for each site and the site it was referenced from (site, siteRefrencedFrom)
# persisit the RDD for later use
keyValPairs = short.flatMap(lambda x: [(x[i], x[0]) for i in range(1, len(x))])
keyValPairs.persist()
# reduce the key/value pairs, sort values for given key, sort paired RDD's by key, print results
keyValPairs.groupByKey().mapValues(list).mapValues(lambda x: sorted(x)).sortByKey().collect()

# COMMAND ----------

"""perform map reduce on lab3full data"""

# load the lab3full data, split into a list of site references, and persist the RDD for later use
full = sc.textFile("dbfs:/FileStore/tables/lab3full").map(lambda x: x.split(" "))
full.persist()
# create key/value pairs for each site and the site it was referenced from (site, siteRefrencedFrom)
# persisit the RDD for later use
keyValPairs = full.flatMap(lambda x: [(x[i], x[0]) for i in range(1, len(x))])
keyValPairs.persist()
# reduce the key/value pairs, get results, persist rresluts for later use
finalKeyValPairs = keyValPairs.groupByKey().mapValues(list).mapValues(lambda x: sorted(x)).sortByKey()
finalKeyValPairs.persist()

# COMMAND ----------

# print count of reesults
finalKeyValPairs.count()

# COMMAND ----------

# print first 10 reesults
finalKeyValPairs.take(10)
