class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        l = 0
        r = n
        s = n * (n+1)//2
        while l < r:
            m = l + (r-l)//2
            if m * m < s:
                l = m + 1
            elif m * m > s:
                r = m - 1
            else:
                return m
        return -1
        