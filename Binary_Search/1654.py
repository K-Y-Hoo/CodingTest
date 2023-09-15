import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = []
for _ in range(k):
  arr.append(int(input()))

left = 1
right = max(arr)
cnt = 0
answer = []
while (left <= right):
  mid = (left + right) // 2
  for i in range(k):
    a = (arr[i] // mid)
    cnt += a
  if cnt >= n:
    answer = mid
    cnt = 0
    left = mid + 1
  else:
    right = mid - 1
    cnt = 0

print(answer)