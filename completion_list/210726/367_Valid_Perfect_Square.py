class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = int(num**0.5)
        return sqrt ** 2 == num
