class Solution:
    def helper(self,n):
        a,b=0,0
        for i in n:
            rob=max(a+i,b)
            a=b
            b= rob
        return b

    def rob(self, nums: List[int]) -> int:
        return max(self.helper(nums[1:]), self.helper(nums[:-1]),nums[0])
        