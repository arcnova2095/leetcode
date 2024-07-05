class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        map= set()
        for r in range(len(s)):
            while s[r] in map:
                map.remove(s[l])
                l+=1
            map.add(s[r])
            res=max(res,r-l+1)
        return res