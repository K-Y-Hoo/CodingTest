import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x,y):
  global count
  count += 1
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  for i in range(4):
    ddx = x + dx[i]
    ddy = y + dy[i]
    if (0<=ddx<n) and (0<=ddy<n) and arr[ddx][ddy] == 1 and not visited[ddx][ddy]:
      visited[ddx][ddy] = True
      arr[ddx][ddy] = -1
      dfs(ddx,ddy)

n = int(input())
arr = [list(map(str,input())) for _ in range(n)]
for i in range(len(arr)):
  arr[i].pop()
for i in range(len(arr)):
  for j in range(len(arr)):
    arr[i][j] = int(arr[i][j])
visited = [[False] * n for _ in range(n)]

count = 0
cntarr = []

for i in range(n):
  for j in range(n):
    if arr[i][j] == 1 and not visited[i][j]:
      visited[i][j] = True
      arr[i][j] = -1
      dfs(i,j)
      cntarr.append(count)
      count = 0

cntarr.sort()
print(len(cntarr))
for i in range(len(cntarr)):
  print(cntarr[i])