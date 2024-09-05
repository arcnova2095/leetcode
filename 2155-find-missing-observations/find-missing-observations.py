class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s=mean*(n+len(rolls))
        
        s-= sum(rolls)
        arr=[]
        while(n):
            x=(math.floor(s/n))
            if x>6 or x<1:
                return []
            arr.append(x)
            s-=x
            n-=1
        if (s):
            arr[0]+=1
        return arr