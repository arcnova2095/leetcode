class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        max_curr,min_curr=1,1
        for n in nums:
            tmp= max_curr*n
            max_curr= max(n*min_curr, max_curr*n,n)
            min_curr= min(n*min_curr,tmp,n)
            res= max(res, max_curr)
        return res

            