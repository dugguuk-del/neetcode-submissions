class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = False
        if len(nums)==1:
            return False
        if k>=len(nums):
            hash = set()
            for j in nums:
                hash.add(j)
            if len(hash)<=k:
                c = True
        else:
            for i in range(len(nums)-k):
                hash = set()
                for j in nums[i:i+k+1]:
                    hash.add(j)
                    #print(len(hash))
                if len(hash)<=k:
                    c = True
                    break
        return c
