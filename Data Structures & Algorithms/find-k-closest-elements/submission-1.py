class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr)==k:
            return arr
        else:       
            mins = sum([abs(x-arr[i]) for i in range(k)])
            current_sum = sum([abs(x-arr[i]) for i in range(k)])
            for l in range(len(arr)-k):
                current_sum=current_sum - abs(x-arr[l])+abs(x-arr[l+k])
                mins = min(mins, current_sum )
            cro = arr[0:k]
            sums = sum([abs(x-arr[i]) for i in range(k)])
            j=0
            while j<=len(arr)-k:
                if sums==mins:
                    return cro
                    break
                else:
                    cro.pop(0)
                    cro.append(arr[j+k])
                    sums = sums - abs(x-arr[j]) +abs(x-arr[j+k])
                    j+=1