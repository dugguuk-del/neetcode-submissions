class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join(char for char in s if char.isalnum())
        t = t.lower()
        #print(int((len(t)-1)/2))
        if len(t)%2!=0:
            i = 0
            b = 0
            a=int((len(t)-1)/2)
            while i<=a-1:
                if t[i]==t[-(i+1)]:
                    i+=1
                    b+=1
                if t[i]!=t[-(i+1)]:
                    return False
                    break
            if b==a:
                return True
        if len(t)%2==0:
            i=0
            b=0
            a=int(len(t)/2)
            while i<=a-1:
                if t[i]==t[-(i+1)]:
                    i+=1
                    b+=1
                if t[i]!=t[-(i+1)]:
                    return False
                    break
            if b==a:
                return True
            