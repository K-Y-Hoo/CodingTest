t = 0
while True:
  stack = []
  t += 1
  s = list(input())
  if '-' in s:
    break

  count = 0
  
  for i in range(len(s)):
    if s[i] == '{':
      stack.append(s[i])
    elif s[i] == '}':
      if len(stack) == 0:
        stack.append('{')
        count += 1
      else:
        stack.pop()
  print('{}. {}'.format(t,len(stack)// 2+count))