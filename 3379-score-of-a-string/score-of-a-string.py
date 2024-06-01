class Solution:
    def scoreOfString(self, s: str) -> int:
        arr=[]
        res=0
        for i in s:
            arr.append(ord(i))
        for i in range(len(arr)-1):
            res+=abs(arr[i]-arr[i+1])
            
        return res
            
        