## Use set to store elements and use random.choices with weights and k=1


import random
class RandomizedSet(object):

    def __init__(self):
        self.random_set = set()
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.random_set:
            return False
        else:
            self.random_set.add(val)
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.random_set:
            self.random_set.remove(val)
            return True
        else:
            return False
        
        
    def getRandom(self):
        """
        :rtype: int
        """
#         p = 1//len(self.random_set)
#         if p == 0:
#             return random.choices(list(self.random_set), k=1)[0]
        
#         return random.choices(list(self.random_set), weights = [p]*len(self.random_set), k=1)[0]
        return random.choice(list(self.random_set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()