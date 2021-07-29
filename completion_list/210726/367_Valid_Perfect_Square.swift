infix operator **: MultiplicationPrecedence
func **(_ lhs: Double, _ rhs: Double) -> Double {
    return pow(lhs, rhs)
}

class Solution {
    func isPerfectSquare(_ num: Int) -> Bool {
        return (floor(Double(num)**0.5))**2 == Double(num)
    }
}
