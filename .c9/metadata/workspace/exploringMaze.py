{"filter":false,"title":"exploringMaze.py","tooltip":"/exploringMaze.py","undoManager":{"mark":5,"position":5,"stack":[[{"start":{"row":0,"column":0},"end":{"row":55,"column":0},"action":"insert","lines":[" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","","\t","","def searchFrom(maze, startRow, startColumn):","    maze.updatePosition(startRow, startColumn)","   #  Check for base cases:","   #  1. We have run into an obstacle, return false","   if maze[startRow][startColumn] == OBSTACLE :","        return False","    #  2. We have found a square that has already been explored","    if maze[startRow][startColumn] == TRIED:","        return False","    # 3. Success, an outside edge not occupied by an obstacle","    if maze.isExit(startRow,startColumn):","        maze.updatePosition(startRow, startColumn, PART_OF_PATH)","        return True","    maze.updatePosition(startRow, startColumn, TRIED)","","    # Otherwise, use logical short circuiting to try each","    # direction in turn (if needed)","    found = searchFrom(maze, startRow-1, startColumn) or \\","            searchFrom(maze, startRow+1, startColumn) or \\","            searchFrom(maze, startRow, startColumn-1) or \\","            searchFrom(maze, startRow, startColumn+1)","    if found:","        maze.updatePosition(startRow, startColumn, PART_OF_PATH)","    else:","        maze.updatePosition(startRow, startColumn, DEAD_END)","    return found",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":[" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","","\t",""],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":26,"column":0},"action":"remove","lines":["def searchFrom(maze, startRow, startColumn):","    maze.updatePosition(startRow, startColumn)","   #  Check for base cases:","   #  1. We have run into an obstacle, return false","   if maze[startRow][startColumn] == OBSTACLE :","        return False","    #  2. We have found a square that has already been explored","    if maze[startRow][startColumn] == TRIED:","        return False","    # 3. Success, an outside edge not occupied by an obstacle","    if maze.isExit(startRow,startColumn):","        maze.updatePosition(startRow, startColumn, PART_OF_PATH)","        return True","    maze.updatePosition(startRow, startColumn, TRIED)","","    # Otherwise, use logical short circuiting to try each","    # direction in turn (if needed)","    found = searchFrom(maze, startRow-1, startColumn) or \\","            searchFrom(maze, startRow+1, startColumn) or \\","            searchFrom(maze, startRow, startColumn-1) or \\","            searchFrom(maze, startRow, startColumn+1)","    if found:","        maze.updatePosition(startRow, startColumn, PART_OF_PATH)","    else:","        maze.updatePosition(startRow, startColumn, DEAD_END)","    return found",""],"id":4},{"start":{"row":0,"column":0},"end":{"row":131,"column":0},"action":"insert","lines":["import turtle","","PART_OF_PATH = 'O'","TRIED = '.'","OBSTACLE = '+'","DEAD_END = '-'","","class Maze:","    def __init__(self,mazeFileName):","        rowsInMaze = 0","        columnsInMaze = 0","        self.mazelist = []","        mazeFile = open(mazeFileName,'r')","        rowsInMaze = 0","        for line in mazeFile:","            rowList = []","            col = 0","            for ch in line[:-1]:","                rowList.append(ch)","                if ch == 'S':","                    self.startRow = rowsInMaze","                    self.startCol = col","                col = col + 1","            rowsInMaze = rowsInMaze + 1","            self.mazelist.append(rowList)","            columnsInMaze = len(rowList)","","        self.rowsInMaze = rowsInMaze","        self.columnsInMaze = columnsInMaze","        self.xTranslate = -columnsInMaze/2","        self.yTranslate = rowsInMaze/2","        self.t = turtle.Turtle()","        self.t.shape('turtle')","        self.wn = turtle.Screen()","        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)","","    def drawMaze(self):","        self.t.speed(10)","        self.wn.tracer(0)","        for y in range(self.rowsInMaze):","            for x in range(self.columnsInMaze):","                if self.mazelist[y][x] == OBSTACLE:","                    self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'orange')","        self.t.color('black')","        self.t.fillcolor('blue')","        self.wn.update()","        self.wn.tracer(1)","","    def drawCenteredBox(self,x,y,color):","        self.t.up()","        self.t.goto(x-.5,y-.5)","        self.t.color(color)","        self.t.fillcolor(color)","        self.t.setheading(90)","        self.t.down()","        self.t.begin_fill()","        for i in range(4):","            self.t.forward(1)","            self.t.right(90)","        self.t.end_fill()","","    def moveTurtle(self,x,y):","        self.t.up()","        self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))","        self.t.goto(x+self.xTranslate,-y+self.yTranslate)","","    def dropBreadcrumb(self,color):","        self.t.dot(10,color)","","    def updatePosition(self,row,col,val=None):","        if val:","            self.mazelist[row][col] = val","        self.moveTurtle(col,row)","","        if val == PART_OF_PATH:","            color = 'green'","        elif val == OBSTACLE:","            color = 'red'","        elif val == TRIED:","            color = 'black'","        elif val == DEAD_END:","            color = 'red'","        else:","            color = None","","        if color:","            self.dropBreadcrumb(color)","","    def isExit(self,row,col):","        return (row == 0 or","                row == self.rowsInMaze-1 or","                col == 0 or","                col == self.columnsInMaze-1 )","","    def __getitem__(self,idx):","        return self.mazelist[idx]","","","def searchFrom(maze, startRow, startColumn):","    # try each of four directions from this point until we find a way out.","    # base Case return values:","    #  1. We have run into an obstacle, return false","    maze.updatePosition(startRow, startColumn)","    if maze[startRow][startColumn] == OBSTACLE :","        return False","    #  2. We have found a square that has already been explored","    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:","        return False","    # 3. We have found an outside edge not occupied by an obstacle","    if maze.isExit(startRow,startColumn):","        maze.updatePosition(startRow, startColumn, PART_OF_PATH)","        return True","    maze.updatePosition(startRow, startColumn, TRIED)","    # Otherwise, use logical short circuiting to try each direction","    # in turn (if needed)","    found = searchFrom(maze, startRow-1, startColumn) or \\","            searchFrom(maze, startRow+1, startColumn) or \\","            searchFrom(maze, startRow, startColumn-1) or \\","            searchFrom(maze, startRow, startColumn+1)","    if found:","        maze.updatePosition(startRow, startColumn, PART_OF_PATH)","    else:","        maze.updatePosition(startRow, startColumn, DEAD_END)","    return found","","","myMaze = Maze('maze2.txt')","myMaze.drawMaze()","myMaze.updatePosition(myMaze.startRow,myMaze.startCol)","","searchFrom(myMaze, myMaze.startRow, myMaze.startCol)",""]}],[{"start":{"row":1,"column":0},"end":{"row":3,"column":21},"action":"insert","lines":["import matplotlib","# Force matplotlib to not use any Xwindows backend.","matplotlib.use('Agg')"],"id":5}],[{"start":{"row":1,"column":0},"end":{"row":3,"column":21},"action":"remove","lines":["import matplotlib","# Force matplotlib to not use any Xwindows backend.","matplotlib.use('Agg')"],"id":6}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":56,"column":26},"end":{"row":56,"column":26},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1435307779000,"hash":"fe5f8d5acb85611bec64608230f997656a373f4c"}