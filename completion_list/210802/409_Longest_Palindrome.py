# O(len(s)+(A~z ascii 개수))
class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer = 0

        lower, upper = ord('A'), ord('z')
        ascii_table = [0] * (upper - lower + 1)

        for i in range(len(s)):
            c = ord(s[i]) - lower
            ascii_table[c] += 1

        calodd = False
        for i in ascii_table:
            if i % 2 == 1:
                if calodd:
                    i -= 1
                else:
                    calodd = True
            answer += i

        return answer
