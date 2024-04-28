class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            rob=0
            rob2=0
            for i in nums:
                robb= max(rob+i,rob2)
                rob=rob2
                rob2=robb
            return rob2
        return max(nums[0],helper(nums[:-1]),helper(nums[1:]))