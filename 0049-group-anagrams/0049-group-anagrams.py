class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        
        for word in strs:
            sort_wrd = sorted(word)
            sort_wrd = ''.join(sort_wrd)
            group[sort_wrd].append(word)
        
        return group.values()