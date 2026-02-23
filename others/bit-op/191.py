class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        while n:
            n &= n-1
            res += 1

        return res
    
"""
Count how many 1s

Taking 13 as example:

13 in binary is 1101, which has 3 ones,
The problem can be solved by the following steps:
1. Start n = 13 (1001), r = 0
2. 1st loop: n = 1001 & 1000 = 1100(12), res = 1
3. 2nd loop: n = 1100 & 1011 = 1000 (8), res = 2
4. 3nd loop: n = 1000 & 0111 = 0000 (0), res = 3

return 4 

"""