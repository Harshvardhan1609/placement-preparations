class Solution:
    def sortColors(self, nums: List[int]) -> None:
        e , f = 0, 0
        k = len(nums)-1
        while e!=k+1:
            if nums[e] == 1:
                e+=1
            elif nums[e] == 0:
                nums[e] , nums[f] = nums[f] , nums[e]
                e+=1
                f+=1
            else:
                nums[e] , nums[k] = nums[k] , nums[e]
                k-=1
        return nums
        