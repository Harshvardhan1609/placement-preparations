#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = max(nums)
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<nums[low]:
                high  = mid-1
                ans = min(ans,nums[mid])
            else:
                ans = min(ans,nums[low])
                low = mid+1
        return ans