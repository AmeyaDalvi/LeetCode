class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = defaultdict(list)
        
        for word in words:
            if word in word_dict:
                word_dict[word][0] -= 1
            else:
                word_dict[word].append(-1)
                word_dict[word].append(word)
        
        heap = []
        
        for words in list(word_dict.values()):
            heappush(heap, words)
        
        ans = []

        for i in range(k):
            ans.append(heappop(heap)[1])
        
        return ans
        
        