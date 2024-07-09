class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        slow, fast= 0,0
        while True:
            slow= arr[slow]
            fast= arr[arr[fast]]
            if slow== fast:
                break
        slow2=0
        while True:
            slow= arr[slow]
            slow2= arr[slow2]
            if slow==slow2:
                return slow
        
            
        