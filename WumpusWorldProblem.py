#WumpusWorldProblem

class Block:
        isVisited = False         # Knowledge Base of Agent
        wumpusStatus = "NotSure"  # Knowledge Base of Agent
        pitStatus = "NotSure"     # Knowledge Base of Agent
        
        hasWumpus = False         # Environment Knowledge
        hasStench = False         # Environment Knowledge
        hasPit = False            # Environment Knowledge
        hasBreeze = False         # Environment Knowledge
        hasGold = False           # Environment Knowledge
        hasGlitter = False        # Environment Knowledge
   
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
maze = [[Block() for i in range(order)] for i in range(order)]
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
        maze[r][c].isVisited = True
        maze[r][c].pitStatus = 0
        maze[r][c].wumpusStatus = 0
        if not maze[r][c].hasBreeze:
                if r>0:
                        maze[r-1][c].pitStatus = 0
                if c>0:
                        maze[r][c-1].pitStatus = 0
                if r<order-1:
                        maze[r+1][c].pitStatus = 0
                if c<order-1:
                        maze[r][c+1].pitStatus = 0
        if not maze[r][c].hasStench:
                if r>0:
                        maze[r-1][c].wumpusStatus = 0
                if c>0:
                        maze[r][c-1].wumpusStatus = 0
                if r<order-1:
                        maze[r+1][c].wumpusStatus = 0
                if c<order-1:
                        maze[r][c+1].wumpusStatus = 0

        if r<order-1 and not maze[r+1][c].isVisited and not maze[r+1][c].pitStatus and not maze[r+1][c].wumpusStatus:
                rPre, cPre = r, c
                r = r+1
        elif c<order-1 and not maze[r][c+1].isVisited and not maze[r][c+1].pitStatus and not maze[r][c+1].wumpusStatus:
                rPre, cPre = r, c
                c = c+1
        elif r>0 and not maze[r-1][c].isVisited and not maze[r-1][c].pitStatus and not maze[r-1][c].wumpusStatus:
                rPre, cPre = r, c
                r = r-1
        elif c>0 and not maze[r][c-1].isVisited and not maze[r][c-1].pitStatus and not maze[r][c-1].wumpusStatus:
                rPre, cPre = r, c
                c = c-1
        else:
                r, rPre = rPre, r
                c, cPre = cPre, c
        moves = moves+1
        printMaze("move "+str(moves), order, r , c)

print("Gold Found in", moves, "moves.")

        
        
                        
        
        
        





