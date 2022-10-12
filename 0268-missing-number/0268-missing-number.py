class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        total_sum = int(n*(n+1)/2)
        arr_sum = sum(nums)

        return total_sum - arr_sum
        
        
        