class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        glit=[]
        for i in range(len(nums)):
            c=1
            a=nums[i]
            nums.pop(i)
            j=0
            while j< len(nums):
                c=c*nums[j]
                j+=1
            glit.append(c)
            nums.insert(i,a)
        return glit