S = input()
T = input()

def solution(S, T):
  while(len(T)>1):
    if T[-1] == 'B':
      T = T[:-1]
      T = T[::-1]
    elif T[-1] == 'A':
      T = T[:-1]
    if S == T:
      return True
  return False

if solution(S, T):
  print(1)
else:
  print(0)