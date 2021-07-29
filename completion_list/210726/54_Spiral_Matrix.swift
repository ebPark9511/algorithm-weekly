func zip<T>(_ sequnce: [[T]]) -> [[T]] {
    guard let count = sequnce.first?.count else { return sequnce}
    return (0..<count).map { idx in sequnce.map { $0[idx] } }
}


class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        var matrix = matrix
        
        var answer: [Int] = []
        
        while !matrix.isEmpty {

            answer.append(contentsOf: matrix.remove(at: 0))
            matrix = zip(matrix).reversed()
            print(matrix)
        }
        
        
        return answer
    }
    
}
