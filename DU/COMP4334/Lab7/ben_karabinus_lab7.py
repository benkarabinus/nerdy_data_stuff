# Ben Karabinus

# Databricks notebook source
# MAGIC %md
# MAGIC # __Lab 7: Spark ML__

# COMMAND ----------

"""load  the required modules"""

from pyspark.sql import Row, functions
from pyspark.sql.types import StructType, StructField, LongType, StringType
from pyspark.ml import Pipeline
from pyspark.ml.feature import Bucketizer, StringIndexer, VectorAssembler
from pyspark.ml.linalg import Vectors
from pyspark.ml.classification import LogisticRegression

# COMMAND ----------

"""Setup file directories for lab 7"""

# loop through files in default table storage
for path in dbutils.fs.ls("dbfs:/FileStore/tables/"):
    
    # if test file move to lab3short else if full file move to fulllab
    if "heart" in path[0]:
        dbutils.fs.mv(path[0], "dbfs:/FileStore/tables/lab7/" + path[0][path[0].rindex("/")+1:])

# COMMAND ----------

"""read in the training and test datasets"""

# create the dataframe schema
schema = StructType([\
                     StructField('Id', StringType(), True),\
                     StructField('age', LongType(), True),\
                     StructField('sex', StringType(), True),\
                     StructField('chol', LongType(), True),\
                     StructField('pred', StringType(), True)
                     ])
# specify file paths  for data
train = "dbfs:/FileStore/tables/lab7/heartTraining.csv"
test = "dbfs:/FileStore/tables/lab7/heartTesting.csv"
# read the training and test data into dataframes using specified schema
trainDFRaw = spark.read.format("csv").option("header", True).schema(schema).load(train)
testDFRaw = spark.read.format("csv").option("header", True).schema(schema).load(test)
# shpw the top twenty rows of data
trainDFRaw.show()
testDFRaw.show()

# COMMAND ----------

"""create the sparkML pipeline"""

# create the splits for the bucketizer
buckets = [-float('inf'), 40, 50, 60, 70, float('inf')]
# instantiate  the column transformers
ageGroups = Bucketizer(splits=buckets, inputCol='age', outputCol='ageGroups')
sexIndexer = StringIndexer(inputCol='sex', outputCol='sexIndex')
predIndexer = StringIndexer(inputCol='pred', outputCol='label')
# instantiatee vector assembler
vectorizer = VectorAssembler(inputCols=['chol', 'ageGroups', 'sexIndex'], outputCol='features')
# instantiate the logistic regression model
lr = LogisticRegression()
#create the pipeline
pipeStages = [ageGroups, sexIndexer, vectorizer, predIndexer, lr]
pipeline = Pipeline(stages=pipeStages)
# fit the pipeline to the training data
pipelineModel = pipeline.fit(trainDFRaw)

# COMMAND ----------

""" test the pipeline by making predictions on the test set and show results"""

predTest = pipelineModel.transform(testDFRaw)
predTest.select('Id', 'probability', 'prediction').show()

# COMMAND ----------

"""analyze predictions made against the training set"""

predTrain = pipelineModel.transform(trainDFRaw)
predTrain.select('Id', 'pred', 'label', 'probability', 'prediction').show()

# COMMAND ----------

"""display accuracy of model applied to the training set"""

accuracy = predTrain.filter(predTrain.label == predTrain.prediction).count() / float(predTrain.count())
print("Accuracy: ", accuracy)
