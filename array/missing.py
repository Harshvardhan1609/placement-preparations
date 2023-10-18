class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        output = 0
        for i in range(0,len(nums)+1):
            if i in nums:
                print(i)
            else:
                output = i
        return output

        