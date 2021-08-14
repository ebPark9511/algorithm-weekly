class Solution: 
    def is_peak(self, nums, n):
        is_left, is_right = True, True
        
        if 0 <= n-1:
            is_left = nums[n-1] < nums[n]
        
        if n+1 < len(nums):
            is_right = nums[n+1] < nums[n]
        
        return is_left and is_right
        
        
    def binary_search(self, nums, left, right):
        while left <= right:
            mid = (right + left) // 2
            is_peak_mid = self.is_peak(nums, mid)
            if is_peak_mid:
                return mid
            
            # 가장 큰 peak 고르기
            if nums[mid-1] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
        
    def findPeakElement(self, nums) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[1] < nums[0]:
                return 0
            return 1
        
        left = 0
        right = len(nums) - 1
        
        peak = self.binary_search(nums, left, right)
        
        return peak
