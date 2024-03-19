class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        freq= max(count.values())
        maxCount=0
        for key,val in count.items():
            if val==freq:
                maxCount+=1
        space= (freq
        -1)*max(0,n-maxCount+1)
        remainder= max(0,len(tasks)- (freq*maxCount)-space)
        return freq*maxCount+space+remainder

            
        