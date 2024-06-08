class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones= [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x= heappop(stones)
            y= heappop(stones)
            if x==y:
                continue
            else:
                heappush(stones,-abs(y-x))
        stones.append(0)
        return abs(stones[0])