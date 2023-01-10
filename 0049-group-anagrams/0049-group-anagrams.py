class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        
        for s in strs:
            s_sort = ''.join(sorted(s))
            group_dict[s_sort].append(s)
        
        return list(group_dict.values())
            
                