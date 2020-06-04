#https://leetcode.com/problems/flatten-nested-list-iterator/
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.flatList = []
        self.flatten(self.nestedList)

    def flatten(self, nList: [NestedInteger]):
        while nList:
            item = nList.pop()
            if item.isInteger():
                self.flatList.append(item.getInteger())
            else:
                self.flatten(item.getList())

    def next(self) -> int:
        item = self.flatList.pop()
        return item

    def hasNext(self) -> bool:
        if self.flatList:
            return True
        else:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())