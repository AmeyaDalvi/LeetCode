class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum1 = 0
        count = 0
        num_dict = defaultdict(int)
        
        num_dict[0] = 1
        
        for i in range(len(nums)):
            sum1 += nums[i]
            if sum1-k in num_dict:
                count += num_dict[sum1-k]
            num_dict[sum1] += 1
        
        return count
                
            
        
        
        
                
        
        