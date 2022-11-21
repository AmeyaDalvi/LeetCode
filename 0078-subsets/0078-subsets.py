class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subset = []
        
        for i in nums:
            if not subset:
                subset.append([])
                subset.append([i])
            else:
                subs2 = []
                for subs in subset:
                    sub = copy.deepcopy(subs)
                    sub.append(i)
                    subs2.append(sub)
                subset.extend(subs2)
        
        return subset
            