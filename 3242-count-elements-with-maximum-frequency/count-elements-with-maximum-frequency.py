class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=[0]*101
        maxf=0
        f=0
        for i in nums:
            freq[i]+=1
            if freq[i]==maxf:
                f+=1 
            if freq[i]>maxf:
                f=1
                maxf= freq[i]

        return f*maxf



        