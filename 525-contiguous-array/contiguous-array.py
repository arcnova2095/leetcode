class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n= len(nums)
        s,l=0,0
        mp={}

        for i ,n in enumerate(nums):
            if n==1:
                s+=1
            else :
                s-=1
            if s==0:
                l=i+1
            elif s in mp:
                l= max(l,i-mp[s])
            else:
                mp[s]=i
        return l
        