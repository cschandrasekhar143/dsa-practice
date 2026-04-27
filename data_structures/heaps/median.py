import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.median = 0
    def addNum(self, num: int) -> None:
        if(len(self.max_heap) == 0):
            self.max_heap.append(-1*num)
            self.median = num
            return 
        else:
            root = -1*self.max_heap[0]

            if(num < root):
                heapq.heappush(self.max_heap,-1*num)
            else:
                heapq.heappush(self.min_heap,num)

            if(len(self.max_heap) - len(self.min_heap) > 1):
                val = -1*heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap,val)    
            if(len(self.min_heap) - len(self.max_heap) > 1):
                val = -1*heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap,val)


            if(len(self.max_heap) - len(self.min_heap) == 0):
                self.median = (-1*self.max_heap[0] + self.min_heap[0]) / 2
            elif((len(self.max_heap) - len(self.min_heap)) == 1):
                self.median = -1*self.max_heap[0]
            elif((len(self.min_heap) - len(self.max_heap)) == 1):
                self.median = self.min_heap[0]
            

            
        
    def findMedian(self) -> float:
        
        return self.median


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(-1)
obj.addNum(-2)
obj.addNum(-3)
print(obj.findMedian())
