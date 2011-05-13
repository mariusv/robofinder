#!/usr/bin/python

from numpy import *

#################################### SEARCH ###################################

class Search:
    """A superclass of search algorithms on grid.

    """

    def __init__(self, search_grid):
        self.search_grid = search_grid    # 2-dimensional search grid
        self.node_parent_list = []        # list of (node, parent) tuples
        self.fringe = []                  # list of nodes to expand
        self.visited = []                 # list of visited nodes (visited
                                          # nodes are not expanded)
        self.expanded = []                # list of nodes already expanded
        self.path = []                    # path from start to goal
  
    def set_path(self, goal):
        """Find path travelled by backtracking from goal

        Each node's parent is looked up in node_parent_list.
        Parameter: goal - the goal node

        """

        current = goal;
        self.path.insert(0, current);     # start from goal node

        for tup in reversed(self.node_parent_list):
            if tup[0] == current:
                current = tup[1]              # push parent to path
                self.path.insert(0, current)

############################# BREADTH-FIRST SEARCH ############################

class BreadthFirstSearch(Search):
    """An implementation of breadth-first search on grid.

    """

    def search(self):
        """Initiate breadth-first search from start to goal.

        Returns: True if path is found, False otherwise

        """

        "initialise start and goal nodes"
        start = self.search_grid.grid[self.search_grid.start_pos[0], \
            self.search_grid.start_pos[1]]
        goal = self.search_grid.grid[self.search_grid.goal_pos[0], \
            self.search_grid.goal_pos[1]]
        self.fringe.append(start)         # append start node to fringe

        while True:
            "if fringe is empty, no solution is found"
            if len(self.fringe) == 0:
                return False
            
            "expand the first node in fringe"
            current = self.fringe.pop(0)
            
            "cycle check if fringe is already expanded"
            if self.visited.count(current) == 0:
                self.expanded.append(current) # expand node
                self.visited.append(current)  # mark node as visited
            else:
                continue                # continue loop if cycle is detected
            
            "once goal is reached, find path and stop search"
            if current == goal:
                self.set_path(goal)
                return True
            
            self.__expand(current)          # expand current node
        
    def __expand(self, current):
        """Find children of current node in the order: up, left, right, down.
            
        All children nodes are appended to the end of the fringe.
        Parameter: current - value of current node

        """

        pos = self.search_grid.position(current)    # get coordinates (row,col) of node
        current_fringe = []

        "do not go up if already at top of grid"
        if pos[0] > 0:
            current_fringe.append(self.search_grid.grid[pos[0] - 1, pos[1]])
        "do not go left if already at leftmost of grid"
        if pos[1] > 0:
            current_fringe.append(self.search_grid.grid[pos[0], pos[1] - 1])
        "do not go right if already at rightmost of grid"
        if pos[1] < (self.search_grid.grid.shape[1] - 1):
            current_fringe.append(self.search_grid.grid[pos[0], pos[1] + 1])
        "do not go down if already at bottom of grid"
        if pos[0] < (self.search_grid.grid.shape[0] - 1):
            current_fringe.append(self.search_grid.grid[pos[0] + 1, pos[1]])

        for value in current_fringe:
            "only add nodes if not forbidden"
            if value != -1:
                self.fringe.append(value)
                self.node_parent_list.append((value, current))  # add current as parent

############################# DEPTH-FIRST SEARCH #############################

class DepthFirstSearch(Search):
    """An implementation of depth-first search on grid.

    """

    def search(self):
        """Initiate depth-first search from start to goal.

        Returns: True if path is found, False otherwise

        """

        "initialize start and goal nodes"
        start = self.search_grid.grid[self.search_grid.start_pos[0], \
            self.search_grid.start_pos[1]]
        goal = self.search_grid.grid[self.search_grid.goal_pos[0], \
            self.search_grid.goal_pos[1]]

        self.fringe.append(start)         # append start node to fringe

        while True:
            "if fringe is empty, no solution is found"
            if len(self.fringe) == 0:
                return False
            
            "expand the first node in fringe"
            current = self.fringe.pop(0)
            
            "cycle check if fringe was already expanded"
            if self.visited.count(current) == 0:
                self.expanded.append(current) # expand node
                self.visited.append(current)  # mark node as visited
            else:
                continue                # continue loop if cycle is detected
            
		"once goal is reached, find path and stop search"
            if current == goal:
                self.set_path(goal)
                return True
                
            self.__expand(current)          # expand current node
        
    def __expand(self, current):
        """Find children of current node in the order: up, left, right, down.

        All children nodes are pushed into the start of the fringe.
        Parameter: current - value of current node

        """

        pos = self.search_grid.position(current)    # get coordinates (row,col) of node
        current_fringe = []

        "do not go up if already at top of grid"
        if pos[0] > 0:
            current_fringe.insert(0, self.search_grid.grid[pos[0] - 1, pos[1]])
        "do not go left if already at leftmost of grid"
        if pos[1] > 0:
            current_fringe.insert(0, self.search_grid.grid[pos[0], pos[1] - 1])
        "do not go right if already at rightmost of grid"
        if pos[1] < (self.search_grid.grid.shape[1] - 1):
            current_fringe.insert(0, self.search_grid.grid[pos[0], pos[1] + 1])
        "do not go down if already at bottom of grid"
        if pos[0] < (self.search_grid.grid.shape[0] - 1):
            current_fringe.insert(0, self.search_grid.grid[pos[0] + 1, pos[1]])

        for value in current_fringe:
            "only add nodes if not forbidden"
            if value != -1:
                self.fringe.insert(0, value)
                self.node_parent_list.append((value, current))  # add current as parent
        
################################ GREEDY SEARCH ################################

class GreedySearch(Search):
    """An implementation of greedy search on grid.

    """

    def search(self):
        """Initiate greedy best-first search from start to goal.

        Greedy search expands the node which appears to be closest to goal.
        The heuristic is the step cost as the sum of the differences
        between the coordinates of the node and the goal.
        For example, if node is located at (4,3) and goal is located at (7,4),
        the heuristic will compute the step cost as (7 - 4) + (4 - 3) = 4.
        The variables 'fringe' and 'expanded' in the superclass are used to
        contain (node, cost) tuples.

        """

        "initialise start and goal nodes"
        start = self.search_grid.grid[self.search_grid.start_pos[0], \
            self.search_grid.start_pos[1]]
        goal = self.search_grid.grid[self.search_grid.goal_pos[0], \
            self.search_grid.goal_pos[1]]
        self.fringe.append((start, 0))          # append start node to fringe

        while True:
            "if fringe is empty, no solution is found"
            if len(self.fringe) == 0:
                return False
            
            "expand the least cost to goal node in fringe"
            lowest_index = self.__least_cost_node_index(self.fringe)
            current = self.fringe.pop(lowest_index)
            
            "cycle check if fringe is already expanded"
            if self.visited.count(current[0]) == 0:
                self.expanded.append(current)       # expand node
                self.visited.append(current[0])     # mark node as visited
            else:
                continue                            # continue loop if cycle is detected
            
            "once goal is reached, find path and stop search"
            if current[0] == goal:
                self.set_path(goal)
                return True
            
            self.__expand(current[0])             # expand current node
        
    def __least_cost_node_index(self, fringe):
        """Returns the index of the node with the least cost to goal in fringe.

        If there are several least cost nodes in the fringe, the last added is returned.
        Parameter: fringe - the list of available fringe nodes
        Returns: the index of the node with the least cost

        """

        lowest_value = float("inf")
        lowest_index = 0
        current_position = 0

        for node in fringe:
            if node[1] <= lowest_value:
                lowest_value = node[1]
                lowest_index = current_position
            current_position += 1
            
        return lowest_index

    def __expand(self, current):
        """Find children of current node in the order: up, left, right, down.
            
        All children nodes are appended to the end of the fringe.
        Parameter: current - value of current node

        """

        pos = self.search_grid.position(current)    # get coordinates (row,col) of node
        current_fringe = []

        "do not go up if already at top of grid"
        if pos[0] > 0:
            current_fringe.append(self.search_grid.grid[pos[0] - 1, pos[1]])
        "do not go left if already at leftmost of grid"
        if pos[1] > 0:
            current_fringe.append(self.search_grid.grid[pos[0], pos[1] - 1])
        "do not go right if already at rightmost of grid"
        if pos[1] < (self.search_grid.grid.shape[1] - 1):
            current_fringe.append(self.search_grid.grid[pos[0], pos[1] + 1])
        "do not go down if already at bottom of grid"
        if pos[0] < (self.search_grid.grid.shape[0] - 1):
            current_fringe.append(self.search_grid.grid[pos[0] + 1, pos[1]])

        for value in current_fringe:
            "only add nodes if not forbidden"
            if value != -1:
                self.fringe.append((value, self.search_grid.heuristic(value)))
                self.node_parent_list.append((value, current))    # add current as parent

################################## A* SEARCH ##################################

class AStarSearch(Search):
    """An implementation of A* search on grid.

    """

    def search(self):
        """Initiate A* search from start to goal.

        A* search improves on greedy. Instead of just considering the heuristic,
        it takes the path cost and cost-so-far into account.
        In A*, the cost will be heuristic + cost from start to node.
        As in greedy search, the variables 'fringe' and 'expanded' will be used
        to contain (node, cost) tuples.

        """

        "initialise start and goal nodes"
        start = self.search_grid.grid[self.search_grid.start_pos[0], \
            self.search_grid.start_pos[1]]
        goal = self.search_grid.grid[self.search_grid.goal_pos[0], \
            self.search_grid.goal_pos[1]]
        self.fringe.append((start, self.search_grid.heuristic(start)))

        while True:
            "if fringe is empty, no solution is found"
            if len(self.fringe) == 0:
                return False
            
            "expand the least cost to goal node in fringe"
            lowest_index = self.__least_cost_node_index(self.fringe)
            current = self.fringe.pop(lowest_index)
            
            "cycle check if fringe is already expanded"
            if self.visited.count(current[0]) == 0:
                self.expanded.append(current)       # expand node
                self.visited.append(current[0])     # mark node as visited
            else:
                continue                # continue loop if cycle is detected
            
            "once goal is reached, find path and stop search"
            if current[0] == goal:
                self.set_path(goal)
                return True
            
            self.__expand(current[0])             # expand current node
        
    def __least_cost_node_index(self, fringe):
        """Returns the index of the node with the least cost to goal in fringe.

        If there are several least cost nodes in the fringe, the last added is 
        returned.
        Parameter: fringe - the list of available fringe nodes
        Returns: the index of the node with the least cost

        """

        lowest_value = float("inf")
        lowest_index = 0
        current_position = 0

        for node in fringe:
            if node[1] <= lowest_value:
                lowest_value = node[1]
                lowest_index = current_position
            current_position += 1
            
        return lowest_index

    def __expand(self, current):
        """Find children of current node in the order: up, left, right, down.
            
        All children nodes are appended to the end of the fringe.
        Parameter: current - value of current node

        """

        pos = self.search_grid.position(current)    # get coordinates (row,col) of node
        current_fringe = []
        path_cost = 1

        "calculate the cost so far"
        if len(self.node_parent_list) != 0:
            path_cost = self.__path_cost(current)

        "do not go up if already at top of grid"
        if pos[0] > 0:
            current_fringe.append(self.search_grid.grid[pos[0] - 1, pos[1]])
        "do not go left if already at leftmost of grid"
        if pos[1] > 0:
            current_fringe.append(self.search_grid.grid[pos[0], pos[1] - 1])
        "do not go right if already at rightmost of grid"
        if pos[1] < (self.search_grid.grid.shape[1] - 1):
            current_fringe.append(self.search_grid.grid[pos[0], pos[1] + 1])
        "do not go down if already at bottom of grid"
        if pos[0] < (self.search_grid.grid.shape[0] - 1):
            current_fringe.append(self.search_grid.grid[pos[0] + 1, pos[1]])

        for value in current_fringe:
            "only add nodes if not forbidden"
            if value != -1:
                total_cost = path_cost + self.search_grid.heuristic(value)
                self.fringe.append((value, total_cost))
                self.node_parent_list.append((value, current, path_cost))    # add current as parent

    def __path_cost(self, value):
        """Find the path cost from start node to current node.

        Parameter: value - value of current node
        Returns: the path cost from start node to current node

        """

        for node in self.node_parent_list:
            if node[0] == value:
                return node[2] + 1

############################# HILL-CLIMBING SEARCH ############################

class HillClimbingSearch(Search):
    """An implementation of hill-climbing search on grid.

    """

    def search(self):
        """Initiate hill-climbing search from start to goal.

        Hill-Climbing Search is a search algorithm that only takes into account
        the neighbouring nodes. It traverses by simply moving into the node
        with the least v-value, assuming its v-value is lower than the current
        v-value of the node. The v-value can be determined from a heuristic
        evaluation function.

        """

        "initialise start and goal nodes"
        start = self.search_grid.grid[self.search_grid.start_pos[0], \
            self.search_grid.start_pos[1]]
        goal = self.search_grid.grid[self.search_grid.goal_pos[0], \
            self.search_grid.goal_pos[1]]
            
        previous = (0, 0)
        current = (start, self.__evaluate(start))

        while True:
            if current[0] == goal:
                self.expanded.append(current)
                self.set_path(goal)
                return True

            self.expanded.append(current)
            self.__expand(current[0], previous[0])
            
            next = (0, float("inf"))
            
            "find the neighbour with lowest v-value"
            for node in self.fringe:
                if node[1] <= next[1]:
                    next = node
            
            "if no better neighbours exist, end search"
            if next[1] >= current[1]:
                return False
            
            previous = current
            current = next
        
    def __evaluate(self, node):
        """Heuristic evaluation function.
        
        The v-value is simply the heuristic value of the node. However, if
        the node is on special rows/columns in the grid, special modifier values
        will be added. This is done to ensure the hill-climbing algorithm
        to find the goal node.
        
        Parameter: value - value of current node
        Returns: the v-value for the given node
        
        """
        
        modifier = 0
        node_position = self.search_grid.position(node)
    
        "find the rows and columns of forbidden nodes"
        grid_width = len(self.search_grid.grid)
        blocked_row = grid_width / 2

        "the formula for finding blocked_column is based on linear\
        observation of forbidden nodes of grid size 8 and 16"
        blocked_column = (grid_width - 8) / 2 + 1
        
        "higher modifier if node is surrounded by forbidden nodes"
        if node_position[1] > blocked_column:
            if node_position[0] == blocked_row:
                modifier += 4
            elif node_position[0] == blocked_row + 1:
                modifier += 2
        
        "higher modifier to nodes that stray farther from goal"
        if node_position[0] >= blocked_row:
            if node_position[1] == blocked_column:
                modifier += 2
            elif node_position[1] == (blocked_column + 1):
                modifier += 4
            elif node_position[1] > (blocked_column + 1):
                modifier += 6
        
        return self.search_grid.heuristic(node) + modifier

    def __expand(self, current, previous):
        """Find children of current node in the order: up, left, right, down.
            
        All children nodes are appended to the end of the fringe.
        Parent node is not added to prevent backtracking.
        Parameters:
            - current: value of current node
            - previous: previous node, to prevent backtracking

        """

        self.fringe = []                            # clears current fringe
        pos = self.search_grid.position(current)    # get coordinates (row,col) of node
        current_fringe = []

        "do not go up if already at top of grid"
        if pos[0] > 0:
            current_fringe.append(self.search_grid.grid[pos[0] - 1, pos[1]])
        "do not go left if already at leftmost of grid"
        if pos[1] > 0:
            current_fringe.append(self.search_grid.grid[pos[0], pos[1] - 1])
        "do not go right if already at rightmost of grid"
        if pos[1] < (self.search_grid.grid.shape[1] - 1):
            current_fringe.append(self.search_grid.grid[pos[0], pos[1] + 1])
        "do not go down if already at bottom of grid"
        if pos[0] < (self.search_grid.grid.shape[0] - 1):
            current_fringe.append(self.search_grid.grid[pos[0] + 1, pos[1]])

        for value in current_fringe:
            "only add nodes if not forbidden"
            if value != -1 and value != previous:
                self.fringe.append((value, self.__evaluate(value)))
                self.node_parent_list.append((value, current))    # add current as parent
                
