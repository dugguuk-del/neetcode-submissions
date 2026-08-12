class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        bro=[]
        i=0
        while i <= len(nums)-1:
            if i>0:
                while nums[i]==nums[i-1]:
                    i+=1
                    if i>=len(nums):
                        break
            j=i+1
            while j<=len(nums)-1:
                if j>i+1:
                    while nums[j]==nums[j-1]:
                        j+=1
                        if j>=len(nums):
                            break
                l=j+1
                r=len(nums)-1
                while l<r:
                    if nums[i]+nums[j]+nums[l]+nums[r]>target:
                        r=r-1
                    elif nums[i]+nums[j]+nums[l]+nums[r]<target:
                        l+=1
                    elif nums[i]+nums[j]+nums[l]+nums[r]==target:
                        bro.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        while nums[l]==nums[l-1]:
                            l+=1
                            if l>=len(nums):
                                break
                j+=1
            i+=1
        return bro       