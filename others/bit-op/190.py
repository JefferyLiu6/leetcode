class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32): # since 32bits
            bit = (n >> i) & 1
            res += (bit << (31 - i))

        return res 
    
"Goal: 1011 -> 1101"
"""

<< operator:
x << k means: shift the bits of x left by k
For example, 
1 << 0 = 1 -> 0001
1 << 2 = 4 -> 0100
1 << 3 = 8 -> 1000



Taking a 4-bit as example 

let's say n = 13 (1101):

1.
    i = 0, 
    n >> 0 = 1101
    bit = 1101 & 1 = 1

    n - i = 3 - 0 = 3 
    1 << 3 = 1000
    res = 0000 + 1000


2.
    i = 1,
    n >> 1 = 0110
    bit = 110 & 1 = 0

    n - i = 3 - 1 = 2 
    0 << 2 = 0000

    res = 1000 + 0000 = 1000

3.  i = 2,
    n >> 2 = 0011
    bit = 0011 & 1 = 1

    n - i = 3 - 2 = 1
    1 << 1 = 0010
    res = 1000 + 0010 = 1010
    

4.  i = 3,
    n >> 3 = 0001
    bit = 0001 & 1 = 1 

    n - i = 3 - 3 = 0
    1 << 0 = 0001
    res = 1010 + 0001 = 1011
"""