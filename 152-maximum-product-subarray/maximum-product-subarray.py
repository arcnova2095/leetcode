class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res= nums[0]
        rmax,rmin=1,1
        for i in nums:
            temp= rmin*i
            rmin= min(temp,rmax*i,i)
            rmax= max(temp,rmax*i,i)
            res= max(rmax,res)
        return res
                

            