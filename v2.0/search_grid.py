#!/usr/bin/python

from numpy import *

class SearchGrid:
    """SearchGrid is a grid with a start node, a goal node and 
    a set of forbidden nodes.

    Nodes are represented as a positive integer, with the exception
    of Forbidden nodes which are represented with value -1.

    """
    
    def __init__(self, rows, cols):
        """Constructor.
        
        Parameters:
        - width : width of the maze
        - height : height of the maze
        
        """
        
        "set width x height array and initialise forbidden nodes"
        self.rows = rows
        self.cols = cols
        self.grid = arange(rows * cols).reshape(rows, cols) + 1
        
        "start_pos and goal_pos are (x, y) coordinate tuples"
        self.start_pos = []
        self.goal_pos = []
                    
                    
        
    def addForbiddenNode(self, forbidden_node_index):
        """Adds a forbidden node on the maze.
        
        Parameters:
        - forbidden_node_index : forbidden node index
        
        """
        
        row = forbidden_node_index / self.cols
        col = forbidden_node_index % self.cols
        print "Node", self.grid[row, col], "set to forbidden"
        self.grid[row, col] = -1
        
        
        
    def removeForbiddenNode(self, forbidden_node_index):
        """Removes a forbidden node from the maze.
        
        Parameters:
        - forbidden_node_index : forbidden node index
        
        """
        
        row = forbidden_node_index / self.cols
        col = forbidden_node_index % self.cols
        print "Node", forbidden_node_index, "set to normal"
        self.grid[row, col] = forbidden_node_index
        
        
        
    def setStartNode(self, start_node_index):
        """Sets a start node on the maze.
        
        Parameters:
        - start_node_index : start node index
        
        """
        
        row = start_node_index / self.cols
        col = start_node_index % self.cols
        self.start_pos = (row, col)
        print "Node", self.grid[row, col], "set to start node"
        
        
        
    def unsetStartNode(self):
        """Unsets a start node from the maze.
        
        """
        
        row = self.start_pos[0]
        col = self.start_pos[1]
        print "Node", self.grid[row, col], "set to normal"
        self.start_pos = []
              
        
        
    def setEndNode(self, end_node_index):
        """Sets an end node on the maze.
        
        Parameters:
        - end_node_index : end node index
        
        """
        
        row = end_node_index / self.cols
        col = end_node_index % self.cols
        self.goal_pos = (row, col)
        print "Node", self.grid[row, col], "set to forbidden"
        
        
        
    def unsetEndNode(self):
        """Unsets an end node from the maze.
        
        Parameters:
        - end_node_index : end node index
        
        """

        row = self.goal_pos[0]
        col = self.goal_pos[1]
        print "Node", self.grid[row, col], "set to normal"        
        self.goal_pos = []
        
        
          
    def position(self, value):
        """Finds the coordinate of a given grid value.
        
        Parameter: value - value of current node 
        Returns: (row, column) tuple indicating the position of value inside
            the grid
        
        """
        return (nonzero(self.grid == value)[0][0], \
            nonzero(self.grid == value)[1][0])
            
            
    
    def heuristic(self, value):
        """Computes the heuristic of a given grid value and returns it.
        
        The heuristic is the cost estimate to the goal node. In this case, the
        heuristic is calculated as the sum of the differences between the row 
        and column positions of the current node and the goal node. For
        example, if node is located at (4,3) and goal is located at (7,4), the
        heuristic will compute the step cost as (7 - 4) + (4 - 3) = 4.
        
        Parameter: value - value of current node
        Returns: the heuristic value for the given node
        
        """
    
        position = self.position(value)             # finds position of 'value'
        return abs(self.goal_pos[0] - position[0]) + \
            abs(self.goal_pos[1] - position[1])
            
