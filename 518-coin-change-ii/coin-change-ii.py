class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        for i in range(len(coins)-1,-1,-1):
            newRow= [0]*(amount+1)
            newRow[0]=1
            for j in range(1,amount+1):
                newRow[j]= dp[j]
                if j-coins[i]>=0:
                    newRow[j]+= newRow[j-coins[i]]
            dp= newRow
        return dp[amount]

            

            