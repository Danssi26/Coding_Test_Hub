N = int(input())
T = 2
while N!=1: 
  if N%T==0: 
    print(T) 
    N = N//T
  else:
    T += 1