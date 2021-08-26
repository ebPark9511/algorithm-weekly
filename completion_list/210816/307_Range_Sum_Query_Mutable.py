import math

# 세그먼트 트리
class SegmentTree:
    def __init__(self, nums: [int]):
        self.size = self._tree_size(len(nums))
        self.tree = [0 for _ in range(self.size)]
        self._init_sum_range(nums, 0, len(nums)-1, 1)

    def _tree_size(self, length):
        log2_height = math.log(length, 2)
        height = int(math.ceil(log2_height))
        return 2 ** (height + 1)

    # 이진탐색으로 구간합을 구하면서 올라간다
    def _init_sum_range(self, origin, start, end, node):
        if end <= start:
            self.tree[node] = origin[start]
            return self.tree[node]

        mid = (start+end) // 2

        # 재귀로 구간합 구하기 (왼쪽+오른쪽 = 가운데)
        self.tree[node] = self._init_sum_range(origin, start, mid, node*2) + self._init_sum_range(origin, mid+1, end, node*2+1)
        return self.tree[node]

    # 구간합 구하기
    def sum(self, start, end, left, right, node):
        if end < left or right < start:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2

        return self.sum(start, mid, left, right, node*2) + self.sum(mid+1, end, left, right, node*2+1)

    # 인덱스가 구간에 포함되면 업데이트 하기
    def update(self, start, end, index, diff, node):
        if index<start or end<index:
            return
        
        print(self.tree, node, diff)
        self.tree[node] += diff

        if start == end:
           return

        mid = (start + end) // 2
        self.update(start, mid, index, diff, node*2)
        self.update(mid+1, end, index, diff, node*2+1)

class NumArray:

    def __init__(self, nums: [int]):
        self.nums = nums
        self.tree = SegmentTree(nums)
        self.size = len(self.nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(0, self.size-1, index, val-self.nums[index], 1)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.sum(0, self.size-1, left, right, 1)





b = [9,-8]

array = NumArray(b)

array.update(0,3)
print(array.sumRange(1,1))
