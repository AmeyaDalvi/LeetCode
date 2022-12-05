class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
#         carry = 0
#         val = digits[-1] + 1
        
#         if val < 10:
#             digits[-1] += 1
#             return digits
        
#         for i in range(len(digits)-1, -1, -1):
#             val = val // 10
#             carry = val % 10
            
#             digits[i] = val
        
    
        str_num = ''
        for i in digits:
            str_num += str(i)
        ans = int(str_num) + 1
        
        
        ans_list = []
        while ans:
            ans_list.insert(0, ans%10)
            ans = ans//10
        
        return ans_list
            
            
            