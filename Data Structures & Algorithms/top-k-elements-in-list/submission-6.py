class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #find distinct elements
        el = [nums[0]]
        for i in range(1,len(nums)):
            key = nums[i]
            j = i-1
            while j>=0:
                if key not in el:
                    el.append(key)
                if nums[j]!=key and nums[j] not in el:
                    el.append(nums[j])
                    j = j-1
                else:
                    j=j-1
        dict1 = {k:nums.count(k) for k in el}
        ans = []
        likky = list(dict1.values())
        while len(ans)<k:
            a = max(likky)
            ans = ans + [key for key, val in dict1.items() if val == a]
            if likky.count(a)!=1:
                for va in likky:
                    if va == a:
                        likky.remove(va)
                #likky.remove(a)
            if likky.count(a)==1:
                likky.remove(a)
        return ans
