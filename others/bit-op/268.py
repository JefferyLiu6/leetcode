class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        number_set = set(nums)
        n = len(nums)

        for i in range(n+1):
            if i not in number_set:
                return i
            

class Solution:
    def missingNumber(self, nums: List[int]) -> int:   
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]


        return res