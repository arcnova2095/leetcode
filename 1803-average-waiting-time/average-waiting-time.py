class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait=0
        res=0

        for a ,f in customers:
            wait= max(wait,a)+f
            res+= wait-a
        return res/len(customers)
