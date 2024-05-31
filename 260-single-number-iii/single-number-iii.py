class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic={i:0 for i in nums}
        res=[]
        for i in nums:
            dic[i]+=1
        for i in nums:
            if dic[i]==1:
                res.append(i)
        return res