class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.n,self.k= nums,k
        heapq.heapify(self.n)
        while (len(self.n)>k):
            heapq.heappop(self.n)

    def add(self, val: int) -> int:
        heapq.heappush(self.n,val)
        if len(self.n)>self.k:
            heapq.heappop(self.n)
        return self.n[0]      


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)