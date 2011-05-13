#!/usr/bin/python

"""
    main.py - A simple implementation of path finding robot.

    The robot may use one of five distinct search algorithms as follows:
    - Breadth-First Search (BFS)
    - Depth-First Search (DFS)
    - Greedy Search
    - A* Search
    - Hill-Climbing Search

    ************************************************************
    Version: 1.0
    Date: April 9, 2010
    UoS: COMP3308 Introduction to Artificial Intelligence
    Author: Anggiarto Rimbun & Sarto Halim
          School of Information Technologies
          The University of Sydney
          arim0337@uni.sydney.edu.au
          shal8818@uni.sydney.edu.au
    ************************************************************

    Copyright (c) 2010 Anggiarto Rimbun & Sarto Halim.
    All Rights Reserved.
  
"""

import sys
from search_grid import *
from search import *

################################# MAIN PROGRAM ################################

# ask for grid size
grid_size = raw_input("\
1: 8x8\n\
2: 16x16\n\
Size of grid? ")

sg = SearchGrid()
if grid_size == "1":
    sg.build_8x8()
elif grid_size == "2":
    sg.build_16x16()
else:
    print "Please enter either 1 or 2."
    sys.exit(0)

# ask for search strategy
search_opt = raw_input("\n\
B: BFS\n\
D: DFS\n\
G: Greedy\n\
A: A*\n\
H: Hill-Climbing\n\
Search option? ")

# run appropriate search algorithm
s = []
if search_opt == "B":
    s = BreadthFirstSearch(sg)
    s.search()
elif search_opt == "D":
    s = DepthFirstSearch(sg)
    s.search()
elif search_opt == "G":
    s = GreedySearch(sg)
    s.search()
elif search_opt == "A":
    s = AStarSearch(sg)
    s.search()
elif search_opt == "H":
    s = HillClimbingSearch(sg)
    s.search()
else:
    print "Please enter either B, D, G, A or H. It is case sensitive."
    sys.exit(0)
  
# print results
print "\nExpanded: ", s.expanded
print "Path: ", s.path
print "Path Cost: ",

# print path cost only if there exists a path from start to goal
if (len(s.path) > 0):
    print len(s.path) - 1
else:
    print "N/A (path not found)"

program_stop = raw_input("\nPlease Enter to exit...")
