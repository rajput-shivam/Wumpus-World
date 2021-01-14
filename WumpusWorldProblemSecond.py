#WumpusWorldProblemSecond

class Environment:
        hasWumpus = False          
        hasStench = False
        hasPit = False       
        hasBreeze = False
        hasGold = False  
        hasGlitter = False

Yes = 1
No = 0
NotSure = 0.5
class KnowledgeBase:
        isVisited = No        
        wumpusStatus = NotSure
        stenchStatus = NotSure
        pitStatus = NotSure
        breezeStatus = NotSure
        goldStatus = NotSure
        glitterStatus = NotSure
        
   
def addGold(r, c):
        maze[r][c].hasGold = True
        maze[r][c].hasGlitter = True

def addWumpus(order, r, c):
        maze[r][c].hasWumpus = True
        if r>0:
                maze[r-1][c].hasStench = True
        if c>0:
                maze[r][c-1].hasStench = True
        if r<order-1:
                maze[r+1][c].hasStench = True
        if c<order-1:
                maze[r][c+1].hasStench = True

def addPit(order, r, c):
        maze[r][c].hasPit = True
        if r>0:
                maze[r-1][c].hasBreeze = True
        if c>0:
                maze[r][c-1].hasBreeze = True
        if r<order-1:
                maze[r+1][c].hasBreeze = True
        if c<order-1:
                maze[r][c+1].hasBreeze = True
        
def printMaze(message, order, r, c):
        print(message)
        for i in range(order-1, -1, -1):
                for j in range(order):
                        if r==i and c==j:
                                print('*', end = "  ")
                        elif maze[i][j].hasGold:
                                print('$', end = "  ")
                        elif maze[i][j].hasWumpus:
                                print('X', end = "  ")
                        elif maze[i][j].hasPit:
                                print('O', end = "  ")
                        else:
                                print('-', end = "  ")
                print()
        
                                
order = 4
maze = [[Environment() for i in range(order)] for i in range(order)]
agent = [[KnowledgeBase() for i in range(order)] for i in range(order)]
r,c=map(int,input("Enter location of Gold:  ").split())
addGold(r-1, c-1)
r,c=map(int,input("Enter location of Wumpus:  ").split())
addWumpus(order, r-1, c-1)
for i in range(int(input("Number of Pits:  "))):
        r,c=map(int,input("Enter location of Pit:  ").split())
        addPit(order, r-1, c-1)

moves=0
r,c=map(int,input("Enter starting-location of Agent:  ").split())
r, c, rPre, cPre = r-1, c-1, -1, -1
printMaze("\nInitial State", order, r ,c)
while not maze[r][c].hasGold:
        agent[r][c].isVisited = Yes
        agent[r][c].pitStatus = No
        agent[r][c].wumpusStatus = No
        if not maze[r][c].hasBreeze:
                agent[r][c].breezeStatus = Yes
                if r>0:
                        agent[r-1][c].pitStatus = No
                if c>0:
                        agent[r][c-1].pitStatus = No
                if r<order-1:
                        agent[r+1][c].pitStatus = No
                if c<order-1:
                        agent[r][c+1].pitStatus = No
        if not maze[r][c].hasStench:
                agent[r][c].stenchStatus = Yes
                if r>0:
                        agent[r-1][c].wumpusStatus = No
                if c>0:
                        agent[r][c-1].wumpusStatus = No
                if r<order-1:
                        agent[r+1][c].wumpusStatus = No
                if c<order-1:
                        agent[r][c+1].wumpusStatus = No

        if r<order-1 and not agent[r+1][c].isVisited and not agent[r+1][c].pitStatus and not agent[r+1][c].wumpusStatus:
                rPre, cPre = r, c
                r = r+1
        elif c<order-1 and not agent[r][c+1].isVisited and not agent[r][c+1].pitStatus and not agent[r][c+1].wumpusStatus:
                rPre, cPre = r, c
                c = c+1
        elif r>0 and not agent[r-1][c].isVisited and not agent[r-1][c].pitStatus and not agent[r-1][c].wumpusStatus:
                rPre, cPre = r, c
                r = r-1
        elif c>0 and not agent[r][c-1].isVisited and not agent[r][c-1].pitStatus and not agent[r][c-1].wumpusStatus:
                rPre, cPre = r, c
                c = c-1
        else:
                r, rPre = rPre, r
                c, cPre = cPre, c
        moves = moves+1
        printMaze("move "+str(moves), order, r , c)

print("Gold Found in", moves, "moves.")

        
        
                        
        



