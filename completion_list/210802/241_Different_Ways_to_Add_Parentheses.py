
class Solution:
  def __init__(self):
    self.operation = {}
    self.operation["*"] = lambda a, b: a*b
    self.operation["+"] = lambda a, b: a+b
    self.operation["-"] = lambda a, b: a-b
    self.visited = {}

  def calculate(self, lhs, rhs, op):
    return self.operation[op](lhs, rhs)

  def dfs(self, str):
    if str in self.visited:
      return self.visited[str]

    if str.isdigit():
        return [int(str)]
    
    results = []
    for i in range(len(str)):
        if str[i] not in self.operation:
            continue
        op = str[i]
        left = self.dfs(str[:i]) # 모든 연산 케이스
        right = self.dfs(str[i+1:]) 
        
        for l in left:
            for r in right:
                results.append(self.calculate(l,r,op))

    self.visited[str] = results
    return results

  def diffWaysToCompute(self, expression: str):
    self.visited = {}
    results = self.dfs(expression)
    return results



s = Solution() 
print(s.diffWaysToCompute("2*3-4*5"))
print(s.diffWaysToCompute("2-1-1"))

'''
틀렸던 이유

left, right의 한 case만 고려했었음.
모든 case를 고려했어야함.

'''

