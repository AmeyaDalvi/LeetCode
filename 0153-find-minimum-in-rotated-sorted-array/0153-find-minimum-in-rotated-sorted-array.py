class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        first = 0
        last = len(nums)-1
        
        while first < last:
            mid = first + (last-first)//2
            
            if nums[last] < nums[mid]:
                first = mid + 1
            else:
                last = mid
            
        return nums[first]