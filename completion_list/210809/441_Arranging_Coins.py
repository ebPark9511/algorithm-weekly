import math

class Solution:
 def square_root(self, n):
  return n**0.5

 def quadratic_formula(self,a,b,c):
  numerator = (-1 * b) + (self.square_root(b*b - 4*a*c))
  return numerator / (2*a)

 def arrangeCoins(self, n: int) -> int:
  if n <= 2:
   return 1
  
  a = 1
  b = -1
  c = (n*2) * -1

  answer = math.floor(self.quadratic_formula(a,b,c)) - 1

  return answer

# Test
a = Solution()

for i in range(20):
 print("i: ", i, a.arrangeCoins(i))

