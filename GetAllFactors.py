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
  
