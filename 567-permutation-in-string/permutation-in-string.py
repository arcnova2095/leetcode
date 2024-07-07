class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1,l2=len(s1),len(s2)
    
        if (len(s1)>len(s2)):
            return False
        hash1=[0]*26
        hash2=[0]*26

        for char in s1:
            hash1[ord(char) - ord('a')] += 1
        for i in range(l1):
            hash2[ord(s2[i]) - ord('a')] += 1

        for i in range(l2-l1+1):
            if hash1==hash2:
                return True
            if i+l1<l2:
                 hash2[ord(s2[i]) - ord('a')] -= 1
                 hash2[ord(s2[i+l1]) - ord('a')] += 1
        return False



        
        