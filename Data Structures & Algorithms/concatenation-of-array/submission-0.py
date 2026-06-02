class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list1 = [i for i in nums]
        list2 = [i for i in nums]
        list3 = list1 + list2
        return list3
        