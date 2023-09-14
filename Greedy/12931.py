N = int(input())
A = [0] * N
B = list(map(int,input().split()))

def Bcnt():
  bcnt = 0
  for i in range(N):
    if B[i] % 2 == 0:
      bcnt += 1
  if bcnt == N:
    return True
  return False

cnt = 0
while(A != B):
  if Bcnt():
    for i in range(N):
      B[i] = int(B[i] / 2)
    cnt += 1
  else:
    for i in range(N):
      if B[i] % 2 != 0:
        B[i] -= 1
        cnt += 1

print(cnt)