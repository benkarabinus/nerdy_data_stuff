"""
Ben Karabinus
University of Denver
COMP 4581, Winter quarter 2022
Assignment 1

"""
from collections import defaultdict


class MyQueue:

    def __init__(self):
        self.q = []

    def qSize(self):
        return len(self.q)

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        return self.q.pop(0)

    def empty(self):
        if len(self.q) == 0:
            return True
        else:
            return False

    def __str__(self):

        strQ = " ".join(self.q)
        return strQ


def loadGraph(edgeFileName):

    with open(edgeFileName, 'r') as f:
        edges = [line.split() for line in f.readlines()]
    f.close()

    adjList = defaultdict(list)
    for edge in edges:
        u, v = edge[0], edge[1]
        adjList[u].append(v)
        adjList[v].append(u)

    return adjList


def BFS(G, s):

    dist = {}
    q = MyQueue()
    vertices = G.keys()

    for u in vertices:  # O(n)
        dist[u] = float('inf')  # distance for all vertices == infinity flag
    dist[s] = 0  # distance of source node to itself is 0
    q.enqueue(s)
    while not q.empty():
        u = q.dequeue()
        neighbors = G[u]
        for neighbor in neighbors:  # O(n+m)
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[u]+1
                q.enqueue(neighbor)

    return dist


def distanceDistribution(G):

    distribution = defaultdict(int)
    numDistances = 0

    for v in G.keys():
        dist = BFS(G, v)
        for d in dist.values():
            distribution[d] += 1

    numDistances = sum(distribution.values())
    distribution = {key: "{:.2%}".format(value / numDistances) for
                    key, value in distribution.items()}

    return distribution


def main():

    adjList = loadGraph('/Users/benkarabinus/Documents/Git/nerdy_data_stuff/'
                        'DU/COMP4581/Assignment1/edges.txt')
    distribution = distanceDistribution(adjList)
    print(distribution)


"""
The provided Facebook data satisifies the small world problem to the extent
that approximately 98% of users represented by nodes in the graph are 6 connections
or less away from each other.

Aside

After removing the print statements used for debuging the program runtime is
roughly 3-4 minutes.

A sample of the program output is given below:

{0: '0.02%', 1: '1.08%', 4: '35.93%', 2: '16.65%', 3: '24.41%', 6: '4.15%',
5: '15.72%', 7: '1.93%', 8: '0.10%'}
"""


if __name__ == '__main__':
    main()
