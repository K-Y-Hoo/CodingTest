import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 

def dfs(v):
  visited[v] = True
  for i in arr[v]:
    if not visited[i]:
      dfs(i)

n, m = map(int,input().split())
visited = [False] * (n+1)
cnt = 0
arr = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
  a, b = map(int,input().split())
  arr[a].append(b)
  arr[b].append(a)

for i in range(1,n+1):
  if not visited[i]:
    if not arr[i]:
      cnt += 1
      visited[i] = True
    else:
      dfs(i)
      cnt += 1
      
print(cnt)