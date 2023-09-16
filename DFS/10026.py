import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x,y):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  current_color = arr[x][y]
  for i in range(4):
    ddx = x + dx[i]
    ddy = y + dy[i]
    if (0<=ddx<n) and (0<=ddy<n) and not visited[ddx][ddy]:
      if arr[ddx][ddy] == current_color:
        visited[ddx][ddy] = True
        dfs(ddx,ddy)

n = int(input())
arr = [list(map(str,input())) for _ in range(n)]

for i in range(len(arr)):
  arr[i].pop()

cnt1 = 0
cnt2 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      visited[i][j] = True
      dfs(i,j)
      cnt1 += 1
      
for i in range(n):
  for j in range(n):
    if arr[i][j] == 'G':
      arr[i][j] = 'R'
      
visited = [[False] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      visited[i][j] = True
      dfs(i,j)
      cnt2 += 1

print(cnt1, cnt2)