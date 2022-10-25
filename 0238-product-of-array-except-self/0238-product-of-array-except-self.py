class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        count = 0
        answer = [0]*len(nums)
        for i in nums:
            if i == 0:
                count+=1
                continue
            else:
                res*=i
                
        if count > 1:
            return [0]*len(nums)
        
        for i in range(len(answer)):
            if nums[i] == 0:
                answer[i] = res
            else:
                if count == 1:
                    answer[i] = 0
                else:
                    answer[i] = res//nums[i]
        
        return answer
        