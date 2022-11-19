class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def getPower(n):
            if n == 1:
                return 0
            if n%2 == 0:
                return 1 + getPower(n/2)
            elif n%2!=0:
                return 1 + getPower(3*n+1)
        
        
        ans = defaultdict(int)
        for i in range(lo, hi+1):
            power = getPower(i)
            ans[i] = power
        
        print(ans)
        ans_list = sorted(ans.items(), key=lambda x:x[1])
        print(ans_list)
        
        return ans_list[k-1][0]