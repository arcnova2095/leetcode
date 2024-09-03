class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hs,ht={},{}
        if len(s)!=len(t):
            return -1
        for i in range(len(s)):
            hs[s[i]]=1+ hs.get(s[i],0)
            ht[t[i]]=1+ ht.get(t[i],0)
        res=0
        
        for i in hs:
            if i in ht:
                res+= max(0,hs[i]-ht[i])
            else:
                res+=hs[i]
            
        return res

