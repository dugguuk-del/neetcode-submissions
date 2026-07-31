class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min = len(nums)
        l,r=0,1
        while l<r and r<=len(nums):
            if sum(nums[l:r])>=target:
                if len(nums[l:r])<min:
                    min = len(nums[l:r])
                    l+=1
                else:
                    l+=1
            elif sum(nums[l:r])<target:
                r+=1
        if min==len(nums):
            if sum(nums)>=target:
                return min
            if sum(nums)<target:
                return 0
        if min!=len(nums):
            return min