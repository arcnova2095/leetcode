class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res= nums[0]
        rmax,rmin=1,1
        
        for i in nums:
            temp= rmax*i
            rmax= max(temp,i*rmin,i)
            rmin= min(temp,i*rmin,i)
            res= max(rmax,res)
        return res
                

            