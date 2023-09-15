import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(m):
  arr.append(int(input()))

start = 1
end = max(arr)
answer = 0

while start <= end:
  count = 0
  mid = (start + end) // 2
  
  for jewel in arr:
    a = jewel // mid
    b = jewel % mid
    count += a
    if b > 0:
      count += 1
    
  if count > n:
    start = mid + 1
  else:
    end = mid - 1
    answer = mid
    
print(answer)