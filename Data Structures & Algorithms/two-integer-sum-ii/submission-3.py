class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            for j in range(1,len(numbers)-i):
                if numbers[i]+numbers[i+j]==target:
                    return [i+1,i+j+1]