class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        #Greedy algorithm. 
        # To optimize the total costs, let's sort the persons by price_A - price_B and then send the first n persons to the city A, 
        # and the others to the city B, because this way the company costs are minimal.
        
        costs.sort(key= lambda x: x[0] - x[1])
        
        cost = 0
        
        n = len(costs)//2
        
        for i in range(n):
            cost += costs[i][0] + costs[i + n][1]
        
        return cost