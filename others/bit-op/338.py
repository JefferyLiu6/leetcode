class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(n+1):
            dp[i] = dp[i>>1] + (i&1)

        return dp 
    

# i >> 1 is the bitwise right shift operator
"""
For example, 
if i = 6, binary is:
    6 = 110 
Now shift right by 1:
    110 >> 1 = 11 = 3

so 6 >> 1 = 3



example:
if n = 5:

1. i = 0 (0)
    i >> 1 = 0
    i & 1 = 0
    dp[0] = dp[0] + 0 = 0

2. i = 1 (1)
    i >> 1 = 0
    i & 1 = 1
    dp[1] = dp[0] + 1 = 1

3. i = 2 (10)
    i >> 1 = 1
    i & 1 = 0
    dp[2] = dp[1] + 0 = 1

4. i = 3 (11)
    i >> 1 = 1
    i & 1 = 1
    dp[3] = dp[1] + 1 = 2

5. i = 4 (100)
    i >> 1 = 10 = 2 
    i & 1 = 0
    dp[4] = dp[2] + 0 = 1 

6. i = 5 (101)
    i >> 1 = 10 = 2 
    i & 1 = 1
    dp[4] = dp[2] + 1 = 2
"""