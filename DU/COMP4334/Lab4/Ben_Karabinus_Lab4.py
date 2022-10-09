# Ben Karabinus Lab 4

# Databricks notebook source
# MAGIC %md
# MAGIC # __Lab 4 Page Rank__

# COMMAND ----------

# MAGIC %md
# MAGIC # PageRank Overview
# MAGIC PageRank was the original ranking algorithm used at Google, developed by and named after
# MAGIC one of Google's co-founders, Larry Page. It works generally as follows:
# MAGIC 
# MAGIC 1. Every page has a number of points: its PageRank score.
# MAGIC 2. Every page votes for the pages that it links to, distributing to each page a number of points
# MAGIC equal to the linking page’s PageRank score divided by the number of pages it links to.
# MAGIC 3. Each page then receives a new PageRank score, based on the sum of all the votes it
# MAGIC received.
# MAGIC 4. The process is repeated until the scores are either within a tolerance or for a fixed number
# MAGIC of iterations.

# COMMAND ----------

"""instantiate spark object"""

sc = spark.sparkContext


# COMMAND ----------

"""page rank test with hard coded values"""

# sample data setup
links = sc.parallelize(["a b c", "b a a", "c b", "d a"]).map(lambda x: x.split(" ")).map(lambda x: (x[0], list(set(x[i] for i in range(1, len(x))))))
# partition an persist the links RDD by 1, the rankings rdd will be joined on the links RDD for each page rank iteration
links.partitionBy(1)
links.persist()
# initialize rankings, rankings should be initialized so the sum of all rankings equal 1 (1/numRankRecords)
rankings = sc.parallelize([(page, 0.25) for page in links.keys().collect()])
num_iter = 10

# define function to compute neighbor contributions

def vote(linkRank):
    """
    The vote function takes a single linkRank record in the form (linkingPage, [linkedPages], linkingPageScore) and
    returns votes as key/value pairs (linkedPage, vote) for each linkedPage in [linkedPages].
    
    a single vote for a linked page is calculated as (linkingPageScore/length([linkedPages]))
    """
    new = []
    numerator = linkRank[1][1]
    denominator = len(linkRank[1][0])
    for value in linkRank[1][0]:
        new.append((value, numerator/denominator))
    return(new)

# print the initial links and rankings
print('Initial links: ', links.collect())
print('Initial ranks: ', rankings.collect())
# perform 10 iterations of page rank
for i in range(num_iter):
    print('Iteration: ', i)
    # print the temporary joined RDD
    tempRDD = links.join(rankings)
    print('Joined RDD: ', tempRDD.collect())
    # apply vote function, partition the resulting RDD to eliminate shuffling time
    rankings = tempRDD.flatMap(vote).partitionBy(1)
    rankings.persist()
    print('Neighbor contributions: ', rankings.collect())
    rankings = rankings.reduceByKey(lambda x, y: x+y)
    print('New rankings: ', rankings.collect())
# print the final sorted rankings
print('Final sorted rankings:')
for ranking in rankings.sortBy(lambda x: x[1], ascending=False).collect():
    print('{0} has rank: {1}'.format(ranking[0], ranking[1]))
    
    

# COMMAND ----------

"""perform page rank on lab3ShortData"""

# load the lab3short data, split into a list of site references, and persist the RDD for later use
links = sc.textFile("dbfs:/FileStore/tables/lab3short").map(lambda x: x.split(" ")).map(lambda x: (x[0], list(set(x[i] for i in range(1, len(x))))))
# partition an persist the links RDD by 1, the rankings rdd will be joined on the links RDD for each page rank iteration
links.partitionBy(1)
links.persist()
# initialize rankings, rankings should be initialized so the sum of all rankings equal 1 (1/numRankRecords)
rankings = sc.parallelize([(page, 0.05) for page in links.keys().collect()])
num_iter = 10

# define function to compute neighbor contributions

def vote(linkRank):
    """
    The vote function takes a single linkRank record in the form (linkingPage, [linkedPages], linkingPageScore) and
    returns votes as key/value pairs (linkedPage, vote) for each linkedPage in [linkedPages].
    
    a single vote for a linked page is calculated as (linkingPageScore/length([linkedPages]))
    """
    new = []
    numerator = linkRank[1][1]
    denominator = len(linkRank[1][0])
    for value in linkRank[1][0]:
        new.append((value, numerator/denominator))
    return(new)

# print the initial links and rankings
print('Initial links: ', links.collect())
print('Initial ranks: ', rankings.collect())
# perform 10 iterations of page rank
for i in range(num_iter):
    # inner join creates tempRDD used to calculate votes
    tempRDD = links.join(rankings)
    # apply vote function, partition the resulting RDD to eliminate shuffling time in next run
    rankings = tempRDD.flatMap(vote).partitionBy(1)
    rankings.persist()
    rankings = rankings.reduceByKey(lambda x, y: x+y)
# print the final sorted rankings
print('Final sorted rankings:')
for ranking in rankings.sortBy(lambda x: x[1], ascending=False).collect():
    print('{0} has rank: {1}'.format(ranking[0], ranking[1]))
    

