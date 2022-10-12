class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[abs(nums[i])-1] =  -1* abs(nums[abs(nums[i])-1])
        
        res=[]
        
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res
        