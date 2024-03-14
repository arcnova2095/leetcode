class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res= defaultdict(int)
        res[0]=1
        ans=0
        prefix_sum=0
        for i in nums:
            prefix_sum+=i
            ans+=res[prefix_sum-goal]
            res[prefix_sum]+=1
        return ans
    
    


        