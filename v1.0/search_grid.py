#!/usr/bin/python

from numpy import *

class SearchGrid:
    """SearchGrid is a given grid with a start node, a goal node and 
    a set of forbidden nodes.

    If grid_size is 8x8:
    - Start node: 44
    - Goal node: 19
    - Forbidden nodes: 27, 28, 29, 30, 31, 34, 43, 47

    If grid_size is 16x16:
    - Start node: 152
    - Goal node: 103
    - Forbidden nodes: 119, 120, 121, 122, 123, 134, 151, 155

    """

    def build_8x8(self):
        """Builds an 8x8 grid, setting its values from 1 to 64.

        """

        self.grid = arange(64).reshape(8,8) + 1     # set 8x8 array of values 
                                                    # 1 to 64
        self.start_pos = [5,3]                      # start node is 44
        self.goal_pos = [2,2]                       # goal node is 19

        "set forbidden nodes (27, 28, 29, 30, 31, 34, 43, 47)"
        for i in range(8):
            for j in range(8):
                temp = self.grid[i,j]
                if temp >= 27 and temp <= 31 or temp == 34 or \
                    temp == 43 or temp == 47:
                    self.grid[i,j] = -1
    
    def build_16x16(self):
        """Builds a 16x16 grid setting its values from 1 to 256.

        """
    
        self.grid = arange(256).reshape(16,16) + 1  # set 16x16 array of values
                                                    # 1 to 256
        self.start_pos = [9,7]                      # start node is 152
        self.goal_pos = [6,6]                       # goal node is 103
    
        "set forbidden nodes (119, 120, 121, 122, 123, 134, 151, 155)"
        for i in range(16):
            for j in range(16):
                temp = self.grid[i,j]
                if temp >= 119 and temp <= 123 or temp == 134 or \
                    temp == 151 or temp == 155:
                    self.grid[i,j] = -1
          
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
            
