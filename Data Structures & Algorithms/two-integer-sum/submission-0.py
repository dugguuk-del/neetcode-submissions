class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        power=[[nums[i],nums[j]] for i in range(len(nums)) for j in range(len(nums)) if j>i]
        lpower = [[i,j] for i in range(len(nums)) for j in range(len(nums)) if j>i]
        i=0
        while sum(power[i]) != target:
            i=i+1
        else:
            return lpower[i]