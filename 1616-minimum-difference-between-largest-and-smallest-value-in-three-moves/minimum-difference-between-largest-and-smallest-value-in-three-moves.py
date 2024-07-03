class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        nums.sort()
        n= len(nums)-3
        ans=max(nums)-min(nums)
        for i in range(n-1,len(nums)):
            ans= min(ans,nums[i]-nums[i-n+1])
        return ans