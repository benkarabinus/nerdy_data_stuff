# Ben Karabinus
# Lab 2
# Databricks notebook source
# MAGIC %md
# MAGIC # <center>__Ben Karabinus Lab 2__</center>

# COMMAND ----------

"""notebook setup"""

# import necessary python modules

import math
import random
import statistics

# instantiate object to access RDD

sc = spark.sparkContext

# COMMAND ----------

# MAGIC %md
# MAGIC ## <center>__Prime Exercise__</center>

# COMMAND ----------

"""command block for prime exercise"""

# create a python list of numbers in the range 100, 10,000
nums = [i for i in range(100, 10001)]
print(nums[0], nums[9900])

# creat a parallel RDD from the nums list
numsRDD = sc.parallelize(nums)
print(numsRDD)

# define a function to test if a number is prime

def isPrime(num):
    
    if num <= 1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
        
    return True

# filter the numsRDD using the prime function and print count of primes to screen

print(numsRDD.filter(isPrime).count())

# COMMAND ----------

# MAGIC %md
# MAGIC ## <center>__Celsius Exercise__</center>

# COMMAND ----------

"""command block for celsius exercise"""

# generate a list of 1000 Farenheit temps between 0 and 100 degrees and convert to RDD

temps = [random.randint(0, 100) for i in range(1000)]
tempsRDD = sc.parallelize(temps)
print(tempsRDD.count())

# convert the temperatures to celsius using map function

celsiusTempsRDD = tempsRDD.map(lambda x : (x-32)*(5/9))

# print the mean of celsius temperatures above freezing

mean = statistics.mean(celsiusTempsRDD.filter(lambda x : x > 0).collect())
print("The mean of celsius temperatures above freezing (0 degrees celsius) is {:.4f}.".format(mean))
