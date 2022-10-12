3 ways to solve this.
​
1. Hash Map: Basic, check for key == 1 T: O(n) S: O(n)
2. Math: Formula 2 * (a + b + c) - (a + a + b + b + c) = c T: O(n) S: O(n) set needs space for  elems in nums
3. XOR: a ^ 0 = a; a ^ a = 0; a^b^a = b T: O(n) S: O(1)