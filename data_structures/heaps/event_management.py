
import heapq
class EventManager:

    def __init__(self, events: list[list[int]]):
        self.events = [[-1*x[1],x[0]] for x in events]
        heapq.heapify(self.events)
        self.hash_map = {}
        for i in range(len(events)):
            self.hash_map[self.events[i][1]] = self.events[i][0]
        
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        
        self.hash_map[eventId] = -1*newPriority
        heapq.heappush(self.events,[-1*newPriority,eventId])

    def pollHighest(self) -> int:
        if(len(self.events) == 0):
            return -1
        val = heapq.heappop(self.events)    
        
        while True:
            if(self.hash_map[val[1]] != val[0]):
                if(len(self.events) == 0):
                    return - 1
                val = heapq.heappop(self.events)
                
            else:
                self.hash_map[val[1]] = float('-inf')
                break
        
        return val[1]



# Your EventManager object will be instantiated and called as such:
obj = EventManager([[20,6],[13,2],[14,7],[17,2]])
#param_2 = obj.pollHighest()
#print(param_2)

obj.updatePriority(13,8)
obj.updatePriority(13,1)
obj.updatePriority(13,8)



#print(obj.events)
param_2 = obj.pollHighest()
print(param_2)
#print(obj.events)
#print(obj.events)
#print(obj.hash_map)


param_2 = obj.pollHighest()
print(param_2)
#param_2 = obj.pollHighest()
#print(param_2)
