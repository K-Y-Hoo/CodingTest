import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 

def dfs(x, y):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  for i in range(4):
    ddx = x + dx[i]
    ddy = y + dy[i]
    if (0<=ddx<n) and (0<=ddy<m) and array[ddx][ddy] == 1:
      array[ddx][ddy] = -1
      dfs(ddx,ddy)
          
t = int(input())
for _ in range(t):
  m, n, k = map(int,input().split())
  array = [[0] *m for _ in range(n)]
  cnt = 0
  for _ in range(k):
    y, x = map(int,input().split())
    array[x][y] = 1
  for i in range(n):
    for j in range(m):
      if array[i][j] > 0:
        dfs(i,j)
        cnt += 1 
        
  print(cnt)