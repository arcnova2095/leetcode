class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        row= [0]* (amount+1)
        row[0]=1
        for i in range(len(coins)-1,-1,-1):
            newRow= [0]*(amount+1)
            newRow[0]=1
            for a in range(1,amount+1):
                newRow[a]= row[a]
                if (a-coins[i])>=0:
                    newRow[a]+=newRow[a-coins[i]]
            row= newRow
        return row[amount]


            

            