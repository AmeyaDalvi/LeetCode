class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hash-map solution
        nums_dict={}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        return [i for i in nums_dict if nums_dict[i] == 1][0]
        