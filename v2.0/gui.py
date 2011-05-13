#!/usr/bin/python

from Tkinter import *
from search_grid import *
from search import *

class Maze(Frame):
    """This is the GUI for displaying user options.
    
    Layout management is handled by Tkinter's Grid geometry manager.

    """
    def __init__(self, master=None):
        """Constructor.
        
        This creates the Maze Options and Maze Display window. Maze size
        defaults to 8 by 8.
        
        """     
        
        "node list"
        self.node_list = []
        
        "indices of Start and End nodes"
        self.start_node_index = []
        self.end_node_index = []
        
        "Maze Preference window"
        pref_window = Frame.__init__(self, master)
        self.master.title('Pathfinder - Maze Options')
        self.grid(padx=25, pady=25)
        self.__createWidgets()
        
        "Maze Display window"
        maze_window = self.__createMaze()
        
        
    
    def __createWidgets(self):
        """Create all the widgets required for the GUI.

        """

        "minimum and maximum values for maze width and height"
        MIN_ROWS = MIN_COLS = 8
        MAX_ROWS = MAX_COLS = 16

        "maze size label"
        self.mazesize_label = Label(self, text='Maze Size')
        self.mazesize_label.grid(row=0, column=0, padx=20, sticky=W)
        
        "maze rows option menu"
        mazerows_optlist = range(8, MAX_ROWS + 1)
        self.mazerows_arr = StringVar()
        self.mazerows_arr.set(mazerows_optlist[0])
        self.mazerows_om = OptionMenu(self, self.mazerows_arr,\
            *mazerows_optlist)
        self.mazerows_om.grid(row=0, column=1, sticky=W)
        
        "rows label"
        self.row_label = Label(self, text='rows')
        self.row_label.grid(row=0, column=2, sticky=W)

        "maze columns option menu"
        mazecols_optlist = range(8, MAX_COLS + 1)
        self.mazecols_arr = StringVar()
        self.mazecols_arr.set(mazecols_optlist[0])
        self.mazecols_om = OptionMenu(self, self.mazecols_arr,\
            *mazecols_optlist)
        self.mazecols_om.grid(row=0, column=4, sticky=W)
        
        "columns label"
        self.col_label = Label(self, text='columns')
        self.col_label.grid(row=0, column=5, sticky=W)

        "search algorithm label"
        self.algo_label = Label(self, text='Algorithm')
        self.algo_label.grid(row=3, column=0, padx=20, sticky=W)
        
        "search algorithm option menu"
        algo_optlist = ('Breadth-First', 'Depth-First', 'Greedy', 'A*',\
            'Hill-Climbing')
        self.algo_arr = StringVar()
        self.algo_arr.set(algo_optlist[0])
        self.algo_om = OptionMenu(self, self.algo_arr, *algo_optlist)
        self.algo_om.grid(row=3, column=1, columnspan=4, sticky=W)

        "go button"
        self.go_button = Button(self, text='Go!', command=self.__execute)
        self.go_button.grid(row=4, column=5, padx=20, pady=20)
        
        "set key bindings to all widgets"
        self.__keyBindings()
        
        
        
    def __createMaze(self):
        """Create maze based on supplied height and width.
        
        Maze will be displayed in its own window and will change size
        in accordance to the current value of the option menus that user
        chooses to specify the maze size. The actual maze in the back-end
        will also be created.
        
        """
        
        "separate window for maze display"
        self.window = Toplevel(padx=30, pady=30)
        self.window.title('Pathfinder - Maze')
        
        self.msg_label = Label(self.window, justify=LEFT, \
text='Instructions:\n\
1. Click on a node to toggle between Normal and Forbidden node.\n\
2. Hold the Shift key and click on a node to toggle between Normal and \
Start node.\n\
3. Hold the Control key and click on a node to toggle between Normal and \
End node.twi\n')
        self.msg_label.grid(row=0, column=0, columnspan=16, sticky=W)
        
        "record maze dimensions"
        self.rows = int(self.mazerows_arr.get())
        self.cols = int(self.mazecols_arr.get())
        
        "indices of Start and End nodes"
        self.start_node_index = []
        self.end_node_index = []
        
        "list of all nodes in the maze"
        self.node_list = []
        for i in range(self.rows * self.cols):
            "create all nodes on the maze"
            node = self.__createNode('Normal', i)
            self.node_list.append((node, 'Normal'))
            
        "disallow maze display modification that could potentially\
        happen if mouse pointer loses focus of maze size option boxes"
        self.allow_modify = False

        # create backend maze with specified number of rows and columns"
        self.grid = SearchGrid(self.rows, self.cols)
        
        
        
        
    def __execute(self):
        """Executes program and allows pathfinder to compute path around
        the maze.
        
        """
        
        if self.grid.start_pos == []:
            print 'Start node unspecified'
        elif self.grid.goal_pos == []:
            print 'Goal node unspecified'
        else:
            "select search algorithm based on option menu selection"
            algorithm = self.algo_arr.get()
            search = []
            if algorithm == 'Breadth-First':
                search = BreadthFirstSearch(self.grid)
            elif algorithm == 'Depth-First':
                search = DepthFirstSearch(self.grid)
            elif algorithm == 'Greedy':
                search = GreedySearch(self.grid)
            elif algorithm == 'A*':
                search = AStarSearch(self.grid)
            else:
                search = HillClimbingSearch(self.grid)
            
            "execute search"
            search.search()
            
            if len(search.path) > 0:
                "display path on GUI"
                _displayPath(
                for node in search.path:
                	pass
            else:
                "show Path Not Found popup"
                
                
                
    def __displayPath(self, path):
    	"""Display path on GUI.
    	
    	Nodes that the pathfinder use will change into a new node with
    	directional arrows.
    	
    	"""
    	
    	pass
            
        

            
    def __allowModifyMaze(self, event):
        """This helper function is designed to control whether losing pointer
        focus on a maze dimension option box will modify the maze display.
        
        Event should be a mouse left-click, which sets allow_modify to true,
        and may be followed by a Leave event to re-display the new dimensions
        of the maze.
        
        Parameters:
        - event : the event that will trigger this function
        
        """
        
        self.allow_modify = True
        
        
    
    def __createNode(self, type, i):
        """Create a node on the grid.
        
        Parameters:
        - type : type of Node, either Normal, Forbidden, Start or End
        - i : node index
        
        Returns: created node
        
        """

        "all key bindings"        
        def toggleForbiddenNode(event, self=self, i=i):
            "event handler to toggle between Normal and Forbidden node"
            return self.__toggleForbiddenNode(i, event)
            
        def toggleStartNode(event, self=self, i=i):
            "event handler to toggle between Normal and Start node"
            return self.__toggleStartNode(i, event)
        
        def toggleEndNode(event, self=self, i=i):
            "event handler to toggle between Normal and End node"
            return self.__toggleEndNode(i, event)
        
        "different label and key bindings depending on node type"
        node = []
        if type == 'Normal':
            node = Label(self.window, width=4, height=2,\
                background='#DDDDDD', text=i+1)
            node.bind('<Button-1>', toggleForbiddenNode)
            node.bind('<Shift-Button-1>', toggleStartNode)
            node.bind('<Control-Button-1>', toggleEndNode)
        elif type == 'Forbidden':
            node = Label(self.window, width=4, height=2,\
                background='#FF0000', text='F')
            node.bind('<Button-1>', toggleForbiddenNode)
        elif type == 'Start':
            "existing Start node will have to revert to Normal"
            if self.start_node_index != []:
                self.__toggleStartNode(self.start_node_index)
            "create Start node on current index"
            node = Label(self.window, width=4, height=2,\
                background='#00FF00', text='S')
            node.bind('<Shift-Button-1>', toggleStartNode)
        else:
            "existing End node will have to revert back to Normal"
            if self.end_node_index != []:           
                self.__toggleEndNode(self.end_node_index)
            "create Start node on current index"
            node = Label(self.window, width=4, height=2,\
                background='#00FFFF', text='G')
            node.bind('<Control-Button-1>', toggleEndNode)
        
        "position new node on grid"
        row = i / self.cols + 2
        col = i % self.cols
        node.grid(row=row, column=col)
        
        return node
        
        
    
    def __modifyMaze(self, event):
        """This is an event handler to modify maze based on values within the
        maze width and height option menu. It should be called after the mouse
        pointer loses focus of the option menu.
        
        Parameters:
        - event : the event that will trigger this function
        
        """
        
        if self.allow_modify == True:
            "destroy current maze and recreate a new one"
            self.window.destroy()
            self.__createMaze()
            
        self.allow_modify = False
        
        
        
    def __toggleForbiddenNode(self, i, event=''):
        """Toggle between Normal and Forbidden node.
        
        Parameters:
        - event : the event that will trigger this function
        - i : node index
        
        """
        
        node = self.node_list[i]
        
        if node[1] == 'Forbidden':
            "change to Normal if Forbidden"
            node = self.__createNode('Normal', i)
            node = (node, 'Normal')
            
            # remove Forbidden node from backend as well"
            self.grid.removeForbiddenNode(i)
        else:
            "change to Forbidden if Normal"
            node = self.__createNode('Forbidden', i)
            node = (node, 'Forbidden')
            
            # add node as Forbidden in backend as well"
            self.grid.addForbiddenNode(i)
            
        "insert changed node back to list"
        self.node_list.pop(i)
        self.node_list.insert(i, node)
    
    
    
    def __toggleStartNode(self, i, event=''):
        """Toggle between Normal and Start node.
        
        Parameters:
        - event : the event that will trigger this function
        - i : node index
        
        """
        
        node = self.node_list[i]
        
        if node[1] == 'Start':
            "change Start node back to Normal"
            node = self.__createNode('Normal', i)
            node = (node, 'Normal')
            self.start_node_index = []
            
            # unset Start node in backend as well"
            self.grid.unsetStartNode()
        else:
            "change current node to Start node"
            node = self.__createNode('Start', i)
            node = (node, 'Start')
            self.start_node_index = i
            
            # set as Start node in backend as well"
            self.grid.setStartNode(i)
        
        "insert changed node back to list"
        self.node_list.pop(i)
        self.node_list.insert(i, node)
        
    
    
    def __toggleEndNode(self, i, event=''):
        """Toggle between Normal and End node.
        
        Parameters:
        - event : the event that will trigger this function
        - i : node index
        
        """
        
        node = self.node_list[i]
        
        if node[1] == 'End':
            "change End node back to Normal"
            node = self.__createNode('Normal', i)
            node = (node, 'Normal')
            self.end_node_index = []
            
            # unset End node in backend as well"
            self.grid.unsetEndNode()
        else:
            "change current node to End node"
            node = self.__createNode('End', i)
            node = (node, 'End')
            self.end_node_index = i
            
            # set End node in backend as well"
            self.grid.setEndNode(i)
        
        "insert changed node back to list"
        self.node_list.pop(i)
        self.node_list.insert(i, node)
        
        
        
        
    def __keyBindings(self):
        """Specifies all the key bindings for each widget.
        
        """
        
        "key bindings to modify maze display"
        self.mazerows_om.bind('<Button-1>', self.__allowModifyMaze)
        self.mazerows_om.bind('<Leave>', self.__modifyMaze)
        self.mazecols_om.bind('<Button-1>', self.__allowModifyMaze)
        self.mazecols_om.bind('<Leave>', self.__modifyMaze)

#################### Main Program ####################

maze_pref = Maze()
maze_pref.mainloop()
