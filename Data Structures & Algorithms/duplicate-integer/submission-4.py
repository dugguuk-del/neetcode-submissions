class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        y = False
        for i in range(len(nums)):
            x=nums[i]
            nums.pop(i)
            for j in range(len(nums)):
                if x==nums[j]:
                    return True
                else:
                    y=False
            nums.insert(i,x)
        return y