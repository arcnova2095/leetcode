class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
       k= k%sum(chalk)
       for i,n in enumerate(chalk):
        if k<n:
            return i
        k-=n
       return 0
        