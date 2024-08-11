class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res= nums[0]
        rmin,rmax=1,1
        for n in nums:
            tmp= rmin*n
            rmin= min(tmp,rmax*n,n)
            rmax= max(tmp,rmax*n,n)
            res= max(res,rmax)
        return res
                

            