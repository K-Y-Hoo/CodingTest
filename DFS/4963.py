import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 

def dfs(x, y):
  dx = [-1,1,0,0,-1,1,-1,1]
  dy = [0,0,-1,1,-1,-1,1,1]
  for i in range(8):
    ddx = x + dx[i]
    ddy = y + dy[i]
    if (0<=ddx<n) and (0<=ddy<m) and array[ddx][ddy] == 1:
      array[ddx][ddy] = -1
      dfs(ddx,ddy)
    
while(True):
  m, n = map(int,input().split())
  if m == 0 and n == 0:
    break
  array = [list(map(int,input().split())) for _ in range(n)]

  cnt = 0
  for i in range(n):
    for j in range(m):
      if array[i][j] > 0:
        dfs(i,j)
        cnt += 1 
        
  print(cnt)