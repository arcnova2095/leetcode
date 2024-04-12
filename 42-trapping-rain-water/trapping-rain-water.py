class Solution:
    def trap(self, h: List[int]) -> int:
        i,j=0,len(h)-1
        lm,rm= h[i],h[j]
        res=0
        while i<j:
            if (lm<rm):
                i+=1
                lm= max(lm,h[i])
                res+=lm-h[i]
            else:
                j-=1
                rm= max(rm,h[j])
                res+=rm-h[j]
        return res