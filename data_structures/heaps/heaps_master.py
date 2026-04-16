class MaxPriorityQueue:
    
    def __init__(self,array):
        self.array = array
        self.length = len(array)

    def _max_heapify(self):
        pass

    def _build_heap(self):
        pass

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

    def max_heap_insert(self):
        pass

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

    def max_heap_delete(self,x):
        if(x < 0 or x >= self.length):
            raise IndexError(f"Index out of bounds")
        
        self.max_heap_increase_key(x,float('inf'))
        self._max_heapify(x)
        self.length -= 1

class MinPriorityQueue:
    
    def __init__(self,array=None):
        if array is None:
            self.length = 0
            self.array = []
        else:
            self.array = list(array)
            self.length = len(array)
            self._build_min_heap()

    def _min_heapify(self,index):
        if (index < 0 or index >= self.length):
            raise IndexError(f"Index out of bounds")
        
        smallest = index
        left_index = 2*index + 1
        right_index = 2*index + 2

        if(left_index < self.length  and self.array[left_index] < self.array[smallest]):
            smallest = left_index
        
        if(right_index < self.length and self.array[right_index] < self.array[smallest]):
            smallest = right_index

        if(smallest != index):
            self.array[index],self.array[smallest] = self.array[smallest],self.array[index]
            self._min_heapify(smallest)

    def _build_min_heap(self):
        start_index = self.length // 2 - 1
        for i in range(start_index,-1,-1):
            self._min_heapify(i)

    def min_heap_decrease_key(self,x,k):
        if(x < 0 or x >= self.length):
            raise IndexError(f"Index out of bounds")
        
        if(self.array[x] < k):
            raise ValueError(f"New value is greater than old value")

        while x > 0:
            parent = (x - 1) // 2
            if (self.array[parent] > k):
                self.array[x] = self.array[parent]
                x = parent
            else:
                break
        self.array[x] = k

    def min_heap_insert(self,k):
        self.array.append(float('inf'))
        self.length+=1
        self.min_heap_decrease_key(self.length - 1,k)

    def min_heap_extract_min(self):
        pass


