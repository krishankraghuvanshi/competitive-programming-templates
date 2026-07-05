def f2(x):
  best = float("-inf")
  current = 0
  for num in nums:

      val = (num if num % x == 0 else -num)

      if current+val < val:
          current = val
      else:
          current += val    
      best = max(best, current)
  return best            
