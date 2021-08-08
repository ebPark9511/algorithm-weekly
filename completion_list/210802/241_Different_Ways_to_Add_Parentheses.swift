
class Solution {
    private enum CalculationError: Error {
        case notDefinedOperation
    }
    
    private enum Operator: Character {
        case multiply   = "*"
        case plus       = "+"
        case subtract   = "-"
        
        func calculate<T: Numeric>(lhs: T, rhs: T) -> T {
            switch self {
            case .multiply: return lhs * rhs
            case .plus:     return lhs + rhs
            case .subtract: return lhs - rhs
            }
            
        }
    }
    
    private var visited: [String: [Int]]
    
    init() {
        visited = [:]
    }
    
    func diffWaysToCompute(_ expression: String) -> [Int] {
        let results = dfs(expression)
        return results
    }
    
    private func dfs(_ str: String) -> [Int] {
        if let results = visited[str] {
            return results
        }
        
        if let num = Int(str) {
            return [num]
        }
        
        var results: [Int] = []
        
        str.enumerated().forEach { item in
            let char: Character = item.element
            let index: Int = item.offset
            
            guard let oper = Operator(rawValue: char) else {
                return
            }
            
            let leftList = dfs(str[0..<index])
            let rightList = dfs(str[index+1..<str.count])
            
            leftList.forEach { left in
                rightList.forEach { right in
                    results.append(oper.calculate(lhs: left, rhs: right))
                }
            }
        }
        
        visited[str] = results
        return results
    }
}


extension String {
    subscript(bounds: CountableRange<Int>) -> Self {
        let start = index(startIndex, offsetBy: bounds.lowerBound)
        let end = index(startIndex, offsetBy: bounds.upperBound)
        return String(self[start..<end])
    }
}


