class Solution:
    def robber(self,nums):
        a,b=0,0
        for i in nums:
            temp= max(a+i,b)
            a=b
            b=temp
        return b
    def rob(self, nums: List[int]) -> int:
        return max(self.robber(nums[1:]),self.robber(nums[:-1]),nums[0])
        
        