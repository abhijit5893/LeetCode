# https://leetcode.com/problems/count-primes/
class Solution:
    def countPrimes(self, n: int) -> int:

        if n == 0 or n == 1: return 0
        prime_list = [True] * n
        prime_list[0] = False
        prime_list[1] = False
        i = 2
        while i < n ** 0.5:
            j = 2
            while i * j < n:
                if prime_list[i * j] == True:
                    prime_list[i * j] = False
                j += 1
            i += 1
        count = 0
        for i in prime_list:
            if i == True:
                count += 1
        return count
        '''
        TLE Solution (499979) O(n^2)
        prime_list = [i for i in range(2,n)]
        for i in range(2, int(math.sqrt(n))+1):
            temp = []
            for r,v in enumerate(prime_list):
                if v !=i and v % i == 0:
                    temp.append(v)
            for j in temp:
                prime_list.remove(j)

        return len(prime_list)
        '''