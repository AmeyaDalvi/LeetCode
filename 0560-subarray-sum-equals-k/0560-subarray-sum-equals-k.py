class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cum_sum = []
        sum = 0
        count = 0
        hash_map = {0:1}
        
        for i in range(len(nums)):
            sum += nums[i]
            cum_sum.append(sum)
            
        for i in range(len(cum_sum)):
            if cum_sum[i] - k in hash_map:
                count+= hash_map[cum_sum[i] - k]
            if cum_sum[i] not in hash_map:
                hash_map[cum_sum[i]] = 1
            elif cum_sum[i] in hash_map:
                hash_map[cum_sum[i]] += 1
        
        
        return count
            
            