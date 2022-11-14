class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        diff = nums[-1] - nums[0]
        if diff >= 0:
            return nums[0]
        
        for i in range(len(nums)-1):
            diff = nums[i] - nums[i+1]
            if diff >= 0:
                return nums[i+1]
        
        
            
        