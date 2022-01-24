#

def nextMove(n,r,c,grid):
        for i in range(n):
                for j in range(n):
                        if grid[i][j] == 'p':
                                p_row, p_col = i, j
                                break
        if r < p_row:
                return 'DOWN'
        elif r > p_row:
                return 'UP'
        elif c > p_col:
                return 'LEFT'
        elif c < p_col:
                return 'RIGHT'
                
        

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))