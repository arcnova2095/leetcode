class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            i= abs(i)
            if nums[i-1]<0:
                ans.append(i)
            nums[i-1]*=-1
        return ans
        