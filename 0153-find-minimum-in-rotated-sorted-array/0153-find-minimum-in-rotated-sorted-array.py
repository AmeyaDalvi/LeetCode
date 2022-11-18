#binary search
# num[last] < num[mid]: first = mid + 1, return nums
# use last as your pivot point for comparison with mid

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