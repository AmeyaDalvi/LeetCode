class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_dict={}

        # for num in nums:
        #     if num not in duplicate_dict.keys():
        #         duplicate_dict[num] = 1
        #     elif duplicate_dict[num] == 1:
        #         return True
        #     else:
        #          duplicate_dict[num] += 1
        # return False

        for num in nums:
            if num not in duplicate_dict.keys():
                duplicate_dict[num] = 1
            else:
                duplicate_dict[num] += 1
        
        if len(duplicate_dict.keys()) == len(nums):
            return False
        return True