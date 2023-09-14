import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr = sorted(arr, key = lambda x: (x[1], x[0]))
#print(arr)
result = []
result.append(arr[0])
for i in range(1, N):
  if arr[i][0] >= result[-1][1]:
    result.append(arr[i])
    
print(len(result))