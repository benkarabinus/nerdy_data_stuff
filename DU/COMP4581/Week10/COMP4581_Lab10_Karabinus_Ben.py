"""
Ben Karabinus
University of Denver
Lab 10, COMP 4581
Winter Quarter 2022
"""

"""

Ran out of time and was not able to find a solution. I think my problem is that
adjacency check is flawed at line 110 in python file
"""

# Finds ALL ways to place n nonattacking queens on a n x n board
# NOTE: State[i] is the row for the queen on Column i
# NOTE: There are solutions for n>3
# Stack ADT with list implementation from Lab 5


class MyStack:

    def __init__(self, type):
        # Creates an empty list
        self.elemType = type
        self.state = [] # Empty list

    def str(self):
         # for print
        return str(self.state)

    def empty(self):

        return len(self.state) == 0

    def push(self, elem):
         # Adds an element to the top of a stack
        #assert type(elem) == self.elemType
        self.state.append(elem)

    def pop(self):
         # Removes an element from the top of the stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state.pop()

    def top(self):
         # Returns the top of a nonempty stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]


def nQueens(n):

    # Each state will include only the queens that have been placed so far
    initialState = [] # Initial empty state
    s = MyStack(list) # For a depth first search
    s.push(initialState) # Push the initial state onto the Stack
    # While we still have states to explore
    while not s.empty():
        currentState = s.pop() # Grab the next state
        currentCol = len(currentState)
        # See if we found a solved state at a leaf node
        # That is, we have filled in every column with a queen
        if currentCol == n:
            print(currentState) # Display the solution
        else:
        # Produce the state's children (if they are feasible)
        # Note children are produced backward so they come off the
        # stack later left to right
            for currentRow in range(n,0,-1):
                # Check horizontal and both diagonals of previous queens
                feasible = True
                for previousCol in range(currentCol):
                    if (currentState[previousCol] == currentRow) or \
                    abs(currentState[previousCol]-currentRow) == (currentCol - previousCol):
                        feasible = False
                        break
                if feasible:
                    # Create child by making a copy and appending new col
                    childState = currentState.copy()
                    childState.append(currentRow)
                    s.push(childState) # Push child onto data structure

def graphColoring(graph, colors):

    n = len(graph)

    initialState = [] # Initial empty state
    s = MyStack(list)
    # push the initial state on to the graph
    s.push(initialState)

    while not s.empty():
        currentState = s.pop() # Grab the next state
        currentNode = len(currentState)
        color = colors[0]
        # when all columns are filled in goal state is reached
        if currentNode == n:
            return currentState
        else:
            for currentRow in range(n, 0, -1):
                feasible = True
                for previousNode in range(currentNode):
                    #get previous color
                    previousColor = currentState[previousNode]
                    #check adjacency
                    if graph[previousNode][currentNode] == True and color == previousColor:
                        for i in range(len(colors)):
                            if colors[i] != previousColor:
                                color = colors[i]
                                break
                if feasible:
                    # Create child by making a copy and appending new col
                    childState = currentState.copy()
                    childState.append(color)
                    s.push(childState) # Push child onto data structure


def main():

    #for n in range(4, 8):
        #nQueens(n)

    graph = [[False, True, False, False, False, True ],
            [True, False, True, False, False, True ],
            [False, True, False, True, True, False],
            [False, False, True, False, True, False],
            [False, False, True, True, False, True ],
            [True, True, False, False, True, False]]
    colors = ['r', 'g', 'b']
    print(graphColoring(graph, colors))



if __name__ == '__main__':
    main()
