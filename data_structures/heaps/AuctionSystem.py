import heapq
class AuctionSystem:

    def __init__(self):
        self.item_dict = {}
        self.amount_dict = {}
    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        if itemId not in self.amount_dict:
            self.amount_dict[itemId] = {}
        
        self.amount_dict[itemId][-1*userId] = -1*bidAmount
        if itemId in self.item_dict:
            heapq.heappush(self.item_dict[itemId],(-1*bidAmount,-1*userId))
        else:
            self.item_dict[itemId] = [(-1*bidAmount,-1*userId)]

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.amount_dict[itemId][-1*userId] = -1*newAmount
        heapq.heappush(self.item_dict[itemId],(-1*newAmount,-1*userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        if itemId not in self.amount_dict:
            return 
        self.amount_dict[itemId][-1*userId] = float('inf')

    def getHighestBidder(self, itemId: int) -> int:
        if itemId not in self.amount_dict:
            return -1
        while True:
            if len(self.item_dict[itemId]) == 0:
                return -1
            out = self.item_dict[itemId][0]
            amount = self.amount_dict[itemId][out[1]] 
        
            if(amount == out[0]):
                return -1*out[1]
            else:
                heapq.heappop(self.item_dict[itemId])
        

asys = AuctionSystem()

asys.addBid(8,10,9)

asys.removeBid(8,10)
print(asys.getHighestBidder(10))

asys.addBid(10,10,7)
#[2,7,6]