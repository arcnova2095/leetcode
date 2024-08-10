class Solution:
    def rob(self, nums: List[int]) -> int:
        def help(nums):
            a,b=0,0
            for i in nums:
                temp= max(b,a+i)
                a=b
                b= temp
            return b
        return max(help(nums[1:]), help(nums[:-1]), nums[0])
