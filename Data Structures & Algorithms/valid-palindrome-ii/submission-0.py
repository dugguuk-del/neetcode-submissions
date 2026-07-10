class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        l = len(s)
        if s==s[::-1]:
            return True

        else:
            while s!=s[::-1] and i<=l-2:
                a = s[i]
                m = s[:i] + s[i+1:]
                print(m)
                if m==m[::-1]:
                    return True
                    break
                elif m!=m[::-1]:
                    i+=1
                if i>l-2:
                    return False