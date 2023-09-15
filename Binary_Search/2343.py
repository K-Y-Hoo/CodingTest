import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)
answer = 0

while start <= end:
  mid = (start + end) // 2
  sum = 0
  count = 0
  for i in range(len(arr)):
    if sum + arr[i] > mid:
      count += 1
      sum = 0
    sum += arr[i]

  if sum:
    count += 1
  if count > m:
    start = mid + 1
  else:
    end = mid - 1
    answer = mid
    
print(answer)