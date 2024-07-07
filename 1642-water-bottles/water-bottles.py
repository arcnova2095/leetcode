class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res= numBottles
        curr_empty= numBottles

        while curr_empty//numExchange:
            full_drink=curr_empty//numExchange
            left= curr_empty-full_drink*numExchange
            res+= full_drink
            curr_empty= left+full_drink
        return res
