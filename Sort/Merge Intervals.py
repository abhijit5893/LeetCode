#https://leetcode.com/problems/merge-intervals/submissions/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        '''
        Just Brilliant - Not my solution
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            print(i,out)
            if out and i[0]<=out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], i[-1])
            else: out+=[i]
        return out
        '''
        if not intervals: return []
        arr = sorted(intervals, key =lambda x: x[0])
        print(arr)
        result =[]
        last = arr[0]
        for item in arr:
            if item[0] == last[0]:
                last[1] = max(item[1], last[1])
            elif item[0] ==  last[1]:
                last[0] = min(item[0], last[0])
                last[1] = max(item[1], last[1])
            elif item[0] < last[1] and last[1] < item[1]:
                last[1] = item[1]
            elif item[0] > last[0] and item[0] < last[1]:
                last[0] = min(item[0], last[0])
                last[1] = max(item[1], last[1])
            else:
                print(item,last)
                result.append(last)
                last = item
        result.append(last)
        print(result)
        return result