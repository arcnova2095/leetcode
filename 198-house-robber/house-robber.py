class Solution:
    def rob(self, nums: List[int]) -> int:
        rob,ber=0,0
        for i in nums:
            temp= max(rob+i,ber)
            rob= ber
            ber= temp
        return ber