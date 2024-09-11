class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm={}
        
        for i in magazine:
            hm[i]= 1+ hm.get(i,0)
        for i in ransomNote:
            if i in hm and hm[i]>0:
                hm[i]-=1
            else:
                return False
        return True
                 