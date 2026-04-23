import heapq
class Solution:
    def largestInteger(self, num: int) -> int:
        dummy_num = num
        parity_array = []
        even_numbers = []
        odd_numbers = []
        while(dummy_num > 0):
            reminder = dummy_num % 10
            dummy_num = dummy_num // 10
            if(reminder % 2 == 0):
                parity_array.append("Even")
                even_numbers.append(-1*reminder)
            else:
                parity_array.append("Odd")
                odd_numbers.append(-1*reminder)

        heapq.heapify(even_numbers)
        heapq.heapify(odd_numbers)
        out = 0
        for i in range(-1,-1*(len(parity_array)+1),-1):
            
            if(parity_array[i] == "Even"):
                val = -1*heapq.heappop(even_numbers)
            else:
                val = -1*heapq.heappop(odd_numbers)    
            
            #print(10**(len(parity_array)+i))
            out += val*10**(len(parity_array)+i)
        
        return out

s = Solution()
print(s.largestInteger(1234))
