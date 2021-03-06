#https://leetcode.com/problems/insert-delete-getrandom-o1/
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.table.get(val, None):
            return False
        else:
            self.table[val] = 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self.table.get(val, False):
            if self.table[val] == 0:
                return False
            else:
                del self.table[val]
                return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(list(self.table.keys()))



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()