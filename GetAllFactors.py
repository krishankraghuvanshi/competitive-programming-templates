'''all'''
def f(i):
  x = set()

  j = 2

  while j * j <= i:
      if i%j == 0:
          x.add(j)
          x.add(i//j) 
      j += 1
  if i > 1:
      x.add(i)

  return x

'''prime'''


maxn = 100005


x = defaultdict(list)

primes = [True]*maxn

primes[0], primes[1] = False, False

for i in range(2, maxn):
    if not primes[i]:
        continue
   
        
    j = i
    while j < maxn:
        if i != j:
            primes[j] = False
        x[j].append(i)
        
        
        j += i
      
  
