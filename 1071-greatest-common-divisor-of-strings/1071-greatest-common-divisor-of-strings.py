class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        count=0
        if len(str1)>=len(str2):
            for i in range(1,len(str2)+1):
                tmp1,tmp2=str1,str2
                repl=tmp2[:i]
                if len(tmp1.replace(repl, '')) == 0 and len(tmp2.replace(repl, '')) == 0:
                    count=i
        else:
            for i in range(1,len(str1)+1):
                tmp1,tmp2=str1,str2
                repl=tmp1[:i]
                if len(tmp1.replace(repl,''))==0 and len(tmp2.replace(repl,''))==0:
                    count=i
        if count==0:
            return ""
        else:
            return str1[:count]