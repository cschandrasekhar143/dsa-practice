class MaxPriorityQueue:
    
    def __init__(self,array):
        self.array = array
        self.length = len(array)


    def build_heap_insertion(self):
        if self.length < 0:
            raise IndexError(f"Empty list")
        n = self.length
        old_array = self.array[:]
        self.array = []

        self.array.append(old_array[0])
        self.length = 1
        for i in range(1,n):
            self.max_heap_insert(old_array[i])

    def max_heap_increase_key(self,x,k):

        if(x >= self.length or x < 0):
            raise IndexError(f"Passed index out of bounds")
        

        if(self.array[x] > k):
            raise ValueError(f"Passed key is smaller than existing key")
        
        self.array[x] = k

        while x > 0:
            parent = (x - 1) // 2
            if(self.array[parent] < self.array[x]):
                self.array[parent],self.array[x] = self.array[x],self.array[parent]
                x = parent
            else:
                break

    def max_heap_insert(self,k):
        self.length += 1
        self.array.append(float('-inf'))
        self.max_heap_increase_key(self.length -1, k)

    def max_heap_increase_key_optimized(self,x,k):
        if(x >= self.length or x < 0):
            raise IndexError(f"Passed index out of bounds")
        
        if(self.array[x] > k):
            raise ValueError(f"Passed key is smaller than existing key")
        
        while x > 0:
            parent = (x - 1) // 2
            if(self.array[parent] < k):
                self.array[x] = self.array[parent]
                x = parent
            else:
                break
        
        self.array[x] = k

