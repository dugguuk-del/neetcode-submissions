class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l =sorted(strs, key=sorted)
        s=[sorted([i[j] for j in range(len(i))]) for i in l]
        list1=[s.count(i) for i in s]
        final=[]
        while len(list1)!=0:
            count = list1[0]
            list2=[l[i] for i in range(count)]
            final.append(list2)
            l = l[count:]
            s = s[count:]
            list1=list1[count:]
        return final