class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        str_num = ''
        for i in digits:
            str_num += str(i)
        ans = int(str_num) + 1
        
        ans_list = []
        while ans:
            ans_list.insert(0, ans%10)
            ans = ans//10
        
        return ans_list
            
            
            