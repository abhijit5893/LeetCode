#https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table ={}
        for word in strs:
            count = [0]*26
            for token in word:
                count[ord(token)-ord('a')] += 1
            k = tuple(count)
            table[k] = table.get(k, []) + [word]
            #print(k, table[k])
        return table.values()


        '''
        Sorting Method - Feels like cheating

        table = {}
        for word in strs:
            sword = ''.join(sorted(word))
            if sword not in table:
                table[sword] = [word]
            else:
                table[sword].append(word)
        return list(table.values())
        '''