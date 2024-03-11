class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = [0]*26
        for i in s:
            count[ord(i)-ord('a')] += 1
        n = ''
        for i in order:
            while count[ord(i)-ord('a')] > 0:
                n += i
                count[ord(i)-ord('a')] -= 1
        for i in range(26):
            while count[i] > 0:
                n += chr(i + ord('a'))
                count[i] -= 1
        return n
