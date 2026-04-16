class MinHeap:
    def __init__(self,array:list):
        self.array = array[:]
        self.length = len(array)

    def _min_heapify(self,k):
        
        if( k < 0 or k >= self.length):
            raise IndexError(f"passed index out of bounds")
        left_child = 2*k + 1
        right_child = 2*k + 2
        least = k

        if(left_child < self.length and self.array[left_child][0] < self.array[least][0]):
            least = left_child

        if(right_child < self.length and self.array[right_child][0] < self.array[least][0]):
            least = right_child

        if(least != k):
            self.array[least],self.array[k] = self.array[k], self.array[least]
            self._min_heapify(least)
    
    def build_heap(self,array=None):
        if (array):
            self.array = array[:]
            self.length = len(array)

        start_index = (self.length // 2) - 1

        for i in range(start_index,-1,-1):
            self._min_heapify(i)

    def extract_min(self):
        self.array[0] = self.array[self.length-1]
        self.length -= 1
        self._min_heapify(0)

    
def merge_sorted_lists(k,lists,n):
    if(k <= 0):
        raise ValueError(f"need at least one sorted array to merge")
    if(len(lists) != k):
        raise ValueError(f"Please provide at least {k} lists")
    
    pointer_array = [0]*k
    heap_array = []
    for i in range(k):
        heap_array.append((lists[i][pointer_array[i]],i))
    min_heap_k = MinHeap(heap_array)
    
    # Build heap
    min_heap_k.build_heap()
    sorted_array = []
    for i in range(n): 
        old_root = min_heap_k.array[0]
        sorted_array.append(old_root[0])
        pointer_array[old_root[1]] += 1
        if(pointer_array[old_root[1]] < len(lists[old_root[1]])):
            new_root = lists[old_root[1]][pointer_array[old_root[1]]]
            min_heap_k.array[0] = (new_root,old_root[1])
            min_heap_k._min_heapify(0)
        else:
            min_heap_k.extract_min()
        




#pointer_array = [0]*5
#print(pointer_array)