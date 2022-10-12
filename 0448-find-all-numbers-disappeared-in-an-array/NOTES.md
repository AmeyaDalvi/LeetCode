2 ways to solve
​
1. Hash Map: use a dictionary/set to store all the integers that appear in the array. Then iterate over a range of 1,N to find elements that are not present as a key in the hashmap. T: O(n), S: O(n)
​
2. Inplace replace: For a number num in the array, negate the value at nums[num-1] position. Keep doing that for all the values in the array. Finally, iterate over the array to find indexes with values >0. T: O(n), S:O(n)