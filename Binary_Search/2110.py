import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))
arr.sort()

start = 1
end = max(arr) - min(arr)
answer = 0

while start <= end:
  cnt = 1
  temp = arr[0]
  mid = (start+end) // 2
  for i in range(1,len(arr)):
    if arr[i] >= temp + mid:
      cnt += 1
      temp = arr[i]

  if cnt >= c:
    answer = mid
    start = mid + 1
  else:
    end = mid - 1
print(answer)