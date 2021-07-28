class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def move(current, move):
            dx, dy = move
            cx, cy = current
            cx += dx
            cy += dy
            return (cx, cy)
 
        def chg_position(p):
            return (p+1) % 4
    
        m = len(matrix)
        n = len(matrix[0])
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        dp = -1
        current = (0, -1)
        result = []

        while 0<n and 0<m:
            dp = (dp+1) % 4
            for _ in range(n):
                current = move(current, direction[dp])
                cx = current[0]
                cy = current[1]
                result.append(matrix[cx][cy])
            m -= 1

            dp = (dp+1) % 4
            for _ in range(m):
                current = move(current, direction[dp])
                cx = current[0]
                cy = current[1]
                result.append(matrix[cx][cy])
            n -= 1
            
        return result
