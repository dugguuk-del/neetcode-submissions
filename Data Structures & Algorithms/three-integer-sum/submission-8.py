class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        hash = set()
        hash1 = set()
        bro=[]
        while i<len(nums)-2:
            if nums[i] in hash:
                i+=1
            if nums[i] not in hash:
                hash.add(nums[i])
            a=nums[i]
            l,r=i+1,len(nums)-1
            while l<r:
                if a+nums[l]+nums[r]>0:
                    r=r-1
                elif a+nums[l]+nums[r]<0:
                    l+=1
                elif a+nums[l]+nums[r]==0:
                    if [a,nums[l],nums[r]] in bro:
                        l+=1
                    elif [a,nums[l],nums[r]] not in bro: 
                        bro.append([a,nums[l],nums[r]])
                        l+=1
        i+=1
        return bro
        