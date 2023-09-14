import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))

arr.sort(reverse=True)

result = 0
for i in range(len(arr)-2):
  if arr[i] < arr[i+1] + arr[i+2]:
    result = (arr[i] + arr[i+1] + arr[i+2])
    break

if result == 0:
  print(-1)
else:
  print(result)