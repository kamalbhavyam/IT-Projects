#!/usr/bin/env python3
from Agent import * # See the Agent.py file
from pysat.solvers import Glucose3
import copy

#### All your code can go here.
###############################################################################################################
# Knowledge Base : Currently Contains
KB = [
# First and Last cells are safe so they do not contain mines in them ( Mines in a cell x,y are signified by 9xy )
    [-911],
    [-944],
# There always exists a safe path so one of 1,2 and 2,1 has to be safe since otherwise we wouldnt be able to leave 1,1. Similar logic can be applied to 4,4
    [611],
    [644],
# Safety of a cell implies there is no mine in adjacent cells. Safe Cells are signified as 6xy
    [-611, -912], [-611, -921], [611, 912, 921],
    [-644, -934], [-644, -943], [644, 934, 943],
    [-641, -931], [-641, -942], [641, 942, 931],
    [-614, -924], [-614, -913], [614, 913, 924],
    [-612, -911], [-612, -922], [-612, -913], [612, 911, 922, 913],
    [-613, -912], [-613, -923], [-613, -914], [613, 912, 923, 914],
    [-624, -914], [-624, -923], [-624, -934], [624, 914, 923, 934],
    [-634, -924], [-634, -933], [-634, -944], [634, 924, 933, 944],
    [-621, -911], [-621, -931], [-621, -922], [621, 922, 931, 911],
    [-631, -921], [-631, -941], [-631, -932], [631, 932, 921, 941],
    [-642, -932], [-642, -941], [-642, -943], [642, 941, 932, 943],
    [-643, -944], [-643, -942], [-643, -933], [643, 933, 944, 942],
    [-622, -921], [-622, -923], [-622, -912], [-622, -932], [622, 921, 923, 912, 932],
    [-623, -922], [-623, -924], [-623, -913], [-623, -933], [623, 922, 924, 913, 933],
    [-632, -922], [-632, -942], [-632, -931], [-632, -933], [632, 922, 942, 931, 933],
    [-633, -932], [-633, -934], [-633, -923], [-633, -943], [633, 932, 934, 923, 943],
# If percept was one means only one of the adjacent cells can have bomb ( 1 percept is shown as 1xy )
    [-921, -111, -912], [912, -111, 921],
    [-924, -114, -913], [913, -114, 924],
    [-931, -141, -942], [942, -141, 931],
    [-934, -144, -943], [943, -144, 934],
    [-922 , -112 , -911], [-913 , -112 , -911], [- 922 , -112 , -913], [911 , -112 , 922 , 913],
    [-923 , -113 , -912], [-914 , -113 , -912], [- 923 , -113 , -914], [912 , -113 , 923 , 914],
    [-934 , -124 , -923], [-914 , -124 , -923], [- 934 , -124 , -914], [923 , -124 , 934 , 914],
    [-944 , -134 , -933], [-924 , -134 , -933], [- 944 , -134 , -924], [933 , -134 , 944 , 924],
    [-931 , -121 , -911], [-922 , -121 , -911], [- 931 , -121 , -922], [911 , -121 , 931 , 922],
    [-941 , -131 , -921], [-932 , -131 , -921], [- 941 , -131 , -932], [921 , -131 , 941 , 932],
    [-932 , -142 , -941], [-943 , -142 , -941], [- 932 , -142 , -943], [941 , -142 , 932 , 943],
    [-933 , -143 , -942], [-944 , -143 , -942], [- 933 , -143 , -944], [942 , -143 , 933 , 944],
    [-921, -122, -912], [-923 , -122 , -912 ], [- 921 , -122 , -923], [-921 , -122 , -932], [-923 , -122 , -932], [-912 , -122 , -932], [912, -122, 922, 923, 932],
    [-922, -123, -913], [-924 , -123 , -913 ], [- 922 , -123 , -924], [-922 , -123 , -933], [-924 , -123 , -933], [-913 , -123 , -933], [922, -123, 913, 924, 933],
    [-931, -132, -922], [-933 , -132 , -922 ], [- 931 , -132 , -933], [-931 , -132 , -942], [-933 , -132 , -942], [-922 , -132 , -942], [931, -132, 922, 933, 942],
    [-932, -133, -923], [-934 , -133 , -923 ], [- 932 , -133 , -934], [-932 , -133 , -943], [-934 , -133 , -943], [-923 , -133 , -943], [932, -133, 923, 934, 943],
# If percept was more than one means more than one adjacent cells has bomb ( shown as 5xy )
    [921, -511], [912, -511], [511, -912, -921],
    [913, -514], [924, -514], [514, -913, -924],
    [931, -541], [942, -541], [541, -931, -942],
    [934, -544], [943, -544], [544, -934, -943],
    [911, 922, -512], [922, 913, -512], [911, 913, -512], [512, -911, -913, -922],
    [912, 923, -513], [923, 914, -513], [912, 914, -513], [513, -912, -914, -923],
    [931, 922, -521], [922, 911, -521], [931, 911, -521], [521, -931, -911, -922],
    [941, 932, -531], [932, 921, -531], [941, 921, -531], [531, -941, -921, -932],
    [941, 932, -542], [932, 943, -542], [941, 943, -542], [542, -941, -943, -932],
    [942, 933, -543], [933, 944, -543], [942, 944, -543], [543, -942, -944, -933],
    [923, 934, -524], [934, 914, -524], [923, 914, -524], [524, -923, -914, -934],
    [933, 944, -534], [944, 924, -534], [933, 924, -534], [534, -933, -924, -944],
    [912, 932, 921, -522], [912, 932, 923, -522], [912, 923, 921, -522], [923, 932, 921, -522], [522, -912, -932, -921, -923],
    [913, 933, 922, -523], [913, 933, 924, -523], [913, 924, 922, -523], [924, 933, 922, -523], [523, -913, -933, -922, -924],
    [922, 942, 931, -532], [922, 942, 933, -532], [922, 933, 931, -532], [933, 942, 931, -532], [532, -922, -942, -931, -933],
    [923, 943, 932, -533], [923, 943, 934, -533], [923, 934, 932, -533], [934, 943, 932, -533], [533, -923, -943, -932, -934]
]
###############################################################################################################
validmoves = [[0,1],[0,-1],[-1,0],[1,0]]
grid = [[1,1],[1,2],[1,3],[1,4],[2,1],[2,2],[2,3],[2,4],[3,1],[3,2],[3,3],[3,4],[4,1],[4,2],[4,3],[4,4]]

#### You can change the main function as you wish. Run this program to see the output. Also see Agent.py code.
###############################################################################################################
def check_safety(g,row,column):
    temp = 900+(10*row)+column
    return (not g.solve(assumptions=[temp]))
###############################################################################################################
def sortfunc(val):
    return (8-val[0]-val[1])
###############################################################################################################
def findallsafe(grid, safe, g):
    for elem in grid:
        if elem not in safe:
            if check_safety(g, elem[0], elem[1]):
                safe.append(elem)
###############################################################################################################

class Node:
    def __init__(self,pos):
        self.parent = None
        self.pos = pos
        self.f = None
    def __repr__(self):
        return str(self.pos)
    def __eq__(self, other):
        return self.pos==other.pos
    def __ne__(self, other):
        return not self.__eq__(other)

    def generatesuccessors(self, source, g):
        x,y = self.pos
        succ = []
        for _,inc in enumerate(validmoves):
            zx = x + inc[0]
            zy = y + inc[1]
            if zx>4 or zx<1 or zy>4 or zy<1 or not check_safety(g,zx,zy):
                continue
            nodetoadd = Node([zx,zy])
            comp = source[0]+source[1]
            nodetoadd.f = abs(comp - nodetoadd.pos[0] - nodetoadd.pos[1]) + (8 - nodetoadd.pos[0] - nodetoadd.pos[1])
            succ.append(nodetoadd)
        return succ
###############################################################################################################
def findleastf(openlist, current):
    comp  = current[0] + current[1]
    minn = openlist[0]
    minv = abs(comp - minn.pos[0] - minn.pos[1])
    for elem in openlist:
        if abs(comp - elem.pos[0] - elem.pos[1])<minv:
            minn = elem
    return minn
###############################################################################################################
def pathify(elem, current):
    lst=[]
    while elem.pos!=current:
        lst.insert(0, elem)
        elem = elem.parent
    return lst
###############################################################################################################
def reversepathify(elem, goal):
    lst=[]
    while elem.parent.pos not in goal:
        lst.append(elem.parent)
        elem = elem.parent
    lst.append(elem.parent)
    return lst
###############################################################################################################
def astar(current, goal, allowed, g):
    openlist = []
    closedlist = []


    if len(goal)==1:
        tmp = Node(current)
        tmp.f = 0
        openlist.append(tmp)
        destination = Node(goal[0])
    elif len(goal)>1:
        for x in goal:
            tmp = Node(x)
            tmp.f = 0
            openlist.append(tmp)
        destination = Node(current)

    while(len(openlist))>0:
        foundflag=False
        q = findleastf(openlist, current)
        openlist.remove(q)
        for elem in q.generatesuccessors(current, g):
            skipflag = False
            elem.parent=q
            if elem==destination:
                foundflag=True
                break
            for check in openlist:
                if check==elem:
                    if check.f <= elem.f:
                        skipflag=True
                        break
            if skipflag:
                continue
            for check in closedlist:
                if check==elem:
                    if check.f <= elem.f:
                        skipflag=True
                        break
            if skipflag:
                continue
            openlist.append(elem)
        if foundflag:
            if len(goal)==1:
                return pathify(elem, current)
            else:
                return reversepathify(elem, goal)
        closedlist.append(q)

    return None
###############################################################################################################
def main():
    ag = Agent()
    g = Glucose3()

    #####################################
    # Add Knowledge Base to clauses
    for elem in KB:
        g.add_clause(elem)
    #####################################
    finalpath = []
    safe = []
    unvisited=copy.deepcopy(grid)

    while(1):
        unvisited.remove(ag.FindCurrentLocation())
        #####################################
        x,y = ag.FindCurrentLocation()
        if(ag.FindCurrentLocation()==[4,4]):
            finalpath.append(ag.FindCurrentLocation())
            print(finalpath)
            break
        # If percept return =0, then the cells adjacent have to be clear. So current cell is safe: add 6xy to KB
        if(ag.PerceiveCurrentLocation()=='=0'):
            temp = 600 + (10*x) + y
        # If percept return >=1, then mines are present: add -6xy to KB 
        else:
            temp = -1*(600 + (10*x) + y)
            # If percept returns =1, then only one of the adjacent cells has a mine: add 1xy to KB alongside -6xy
            if(ag.PerceiveCurrentLocation()=='=1'):
                extra = 100 + (10*x) + y
            else:
                extra = 500 + (10*x) + y
            g.add_clause([extra])
        g.add_clause([temp])
        #####################################
        findallsafe(grid, safe, g)
        # Try to reach goal cell
        path = astar(ag.FindCurrentLocation(),[[4,4]],safe, g)
        # If no path to the goal exists, find a path to the closest unvisited node that is safe.
        if path == None:
            goals = [i for i in unvisited if i in safe]
            path = astar(ag.FindCurrentLocation(),goals,safe, g)
        
        while(len(path)>0):
            x,y = ag.FindCurrentLocation()
            finalpath.append([x,y])
            elem = path.pop(0)
            v=[elem.pos[0]-x, elem.pos[1]-y]
            index = validmoves.index(v)
            if index==0:
                ag.TakeAction('Up')
            elif index==1:
                ag.TakeAction('Down')
            elif index==2:
                ag.TakeAction('Left')
            elif index==3:
                ag.TakeAction('Right')
        #####################################


if __name__=='__main__':
    main()