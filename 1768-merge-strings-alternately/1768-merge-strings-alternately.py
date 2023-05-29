class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=0
        s=''
        while True:
            a=len(word1)
            b=len(word2)
            if a==left or b==left:
                if a==left and b==left:
                    break
                elif a==left:
                    s+=word2[left:]
                    break
                else:
                    s+=word1[left:]
                    break
            else:
                s+=word1[left]+word2[left]
            left+=1
        return s
                