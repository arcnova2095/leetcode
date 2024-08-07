class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        curr=nums[0]
        while (l<=r):
            m=l+(r-l)//2
            curr= min(curr,nums[m])
            if nums[m]>nums[r]:
                l= m+1
            else:
                r=m-1
        return curr

