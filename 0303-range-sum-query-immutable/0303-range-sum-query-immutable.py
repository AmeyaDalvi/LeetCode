class NumArray:
    
    sum_arr = []

    def __init__(self, nums: List[int]):
        self.nums = nums
        if len(self.nums) > 1:
            self.sum_arr = self.calc_sum(self.nums)
        
    
    def calc_sum(self, nums):
        sum_arr = [nums[0]]
        
        for i in range(1, len(nums)):
            temp = sum_arr[i-1] + nums[i]
            sum_arr.append(temp)
        print(sum_arr)
        return sum_arr
        
    
    def sumRange(self, left: int, right: int) -> int:
        
        if left == right:
            return self.nums[left]
        
        if left == 0:
            return self.sum_arr[right]
        
        else:
            return self.sum_arr[right] - self.sum_arr[left - 1]
        
        
#         nums_sum = 0
        
#         if left == right:
#             return self.nums[left]
        
#         if (left,right) in NumArray.left_right_dict.keys():
#             return self.left_right_dict[(left, right)]
        
#         elif (left, right) not in NumArray.left_right_dict.keys():
#             for i in range(left, right+1):
#                 nums_sum+=self.nums[i]
#                 print(nums_sum)
#             NumArray.left_right_dict[(left, right)] = nums_sum
#             print("------------")
            
#         return nums_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)