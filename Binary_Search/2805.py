import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int,input().split()))
left = 1
right = max(arr)
rest = 0
answer = 0

while (left <= right):
  mid = (left + right) // 2
  rest = 0
  for i in arr:
    if i >= mid:
      rest += i - mid
  if rest >= m:
    answer = mid
    left = mid + 1
  else:
    right = mid - 1

print(answer)