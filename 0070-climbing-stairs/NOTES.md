this can be solved in 4 ways:
​
1.  Brute force recursion: base condition is if i == n then return 1 path found, else if we jump over n (i > n) return 0 path found. Do this for i+1 and i+2 starting from 0. Time: O(2^n) as branching factor for the tree is 2 and size of recursion tree will be 2^n.
​
2.  Recursion with memoization: no need to calculate result for every step, instead calculate it once and store i in a *memo* . Helps pruning the recursion tree.
​
3.  DP with memoization: a bottom up approach where we divide the problems into sub-problems, optimal soln could be created from optimal solns of subproblems.
One can reach i th step in one of the two ways:
​
Taking a single step from (i−1) th step.
​
Taking a step of 2 from (i−2) th step.
​
Let dp[i] denotes the number of ways to reach on i th step:
dp[i] = dp[i-1] + dp[i-2]
Let dp[i] denotes the number of ways to reach on i