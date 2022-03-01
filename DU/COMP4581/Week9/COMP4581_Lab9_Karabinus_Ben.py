"""
Ben Karabinus
University of Denver
Lab 9, COMP 4581
Winter Quarter 2022
"""

#Dijkstra's shortest path greedy algorithm
# Find the min priority vertex from the list of given vertices
# Each vertex in the form of a list with priority as the first
# element returns the min vertex and removes it from the list


def extractMin(verts):
    minIndex = 0
    for v in range(1, len(verts)):
        if verts[v][1] < verts[minIndex][1]:
            minIndex = v
    return verts.pop(minIndex)


# Dijkstra's shortest path algorithm
def shortest(g):
    # Create a list of vertices and their current shortest distances
    # from vertex 0
    # [vertNum, dist]
    nVerts = len(g)
    vertsToProcess = [[i, float("inf")] for i in range(nVerts+1)]

    #Start at vertex 0 - it has a current shortest distance of 0
    vertsToProcess[0][1] = 0
    # Start with an empty list of processed edges
    vertsProcessed = []
    while len(vertsToProcess) > 0:

        u = extractMin(vertsToProcess)
        vertsProcessed.append(u)
        print("to process:",vertsToProcess)
        print(" processed:",vertsProcessed)
        # Examine all potential verts remaining
        for v in vertsToProcess:
            # Only care about the ones that are adjacent to u
            print(u[0])
            print(v[0])
            print(g[u[0]][v[0]])
            if g[u[0]][v[0]] > 0:
            # Update the distances if necessary
                if u[1] + g[u[0]][v[0]] < v[1]:
                    v[1] = u[1] + g[u[0]][v[0]]
    print(vertsProcessed)


def mst(G):

    # get number of vertices in Graph
    nVerts = len(G)
    # initialize edge weight == infinity for all nodes
    vertsToProcess = [[i, float('inf')] for i in range(nVerts)]
    # initisalize distance from starting node to itself == 0
    vertsToProcess[0][1] = 0
    # initialize A to store processed nodes "minimum cut"
    A = [False for i in range(nVerts)]
    # initialize edges to store the edges of minimum spanning tree
    edges = [None for i in range(nVerts)]
    # initialize edge to -1 for root node
    edges[0] = [0, -1]
    # loop through the priorty queue until empty
    while len(vertsToProcess) > 0:
        # extract min replicates priority queue
        u = extractMin(vertsToProcess)
        A[u[0]] = u
        # examine all nodes to be processed
        for v in vertsToProcess:
            # if adjacent to u
            if G[u[0]][v[0]] > 0:
                # if A[v[0]] == False and G[u[0]][v[0]] < v[1]:
                if G[u[0]][v[0]] < v[1]:
                    v[1] = G[u[0]][v[0]]
                    edges[v[0]] = [v[0], u[0]]
    return edges


def main():

# Adjacency matrix representation of a graph
# This particular graph is the one from the videos
# The vertices didn't have labels in the videos
# so I'm using the following vertex labels:
#   2
#  / \
# 3---1--7
# | \ |
#   4 | 0--6
# \|/
#  5
    graph = [[0, 7, 0, 0, 0, 10, 15, 0],
             [7, 0, 12, 5, 0, 0, 0, 9],
             [0, 12, 0, 6, 0, 0, 0, 0],
             [0, 5, 6, 0, 14, 8, 0, 0],
             [0, 0, 0, 14, 0, 3, 0, 0],
             [10, 0, 0, 8, 3, 0, 0, 0],
             [15, 0, 0, 0, 0, 0, 0, 0],
             [0, 9, 0, 0, 0, 0, 0, 0]]
    #shortest(graph)
    minimumTree = mst(graph)
    print("The edges of the minmum spanning tree (mst) for the input graph are as follows:")
    print()
    print(minimumTree)


if __name__ == '__main__':
    main()
