N, K = map(int, input().split())
coins = []

for _ in range(N):
  coin = int(input())
  coins.append(coin)
coins = sorted(coins, reverse = True)

cnt = 0
while (K>0):
  for coin in coins:
    if coin <= K:
      cnt += K // coin
      K = K % coin

print(cnt)