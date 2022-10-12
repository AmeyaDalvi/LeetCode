class Solution: 
    # hash-map solution
        
    # def singleNumber(self, nums: List[int]) -> int:
    #    
    #     nums_dict={}
    #     for num in nums:
    #         if num not in nums_dict:
    #             nums_dict[num] = 1
    #         else:
    #             nums_dict[num] += 1
    #     return [i for i in nums_dict if nums_dict[i] == 1][0]
    
    
     # math solution
        
    # def singleNumber(self, nums: List[int]) -> int:  
    #          
    #      # formula = 2 * (a + b + c) - (a + a + b + b + c) = c
    #
    #     return 2*sum(set(nums)) - sum(nums)
          
    # XOR solution
      def singleNumber(self, nums: List[int]) -> int:
            
            res = 0
            for num in nums:
                res ^= num
            return res