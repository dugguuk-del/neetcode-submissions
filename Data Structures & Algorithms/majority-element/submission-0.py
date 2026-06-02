class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import math
        plums = list(set(nums))
        freq={x:nums.count(x) for x in plums}
        for i in plums:
            if freq.get(i) > math.floor((len(nums))/2):
                return i