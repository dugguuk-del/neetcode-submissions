class Solution:
    def reverseString(self, s: List[str]) -> None:
        n=len(s)
        if n%2==0:
            for i in range(int(n/2)):
                a=s[n-1-i]
                s[n-1-i]=s[i]
                s[i]=a
        if n%2!=0:
            for i in range(int((n-1)/2)):
                a=s[n-1-i]
                s[n-1-i]=s[i]
                s[i]=a
        return s

        
       
        