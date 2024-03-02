class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output=[]
        for i in nums:
            i= i*i
            output.append(i)
        
        return sorted(output)