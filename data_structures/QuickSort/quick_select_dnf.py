from typing import List
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if(k < 0 or k > n):
            raise IndexError(f"k out of bounds")        
        self.quickSelect(nums,0,n,k,n)
        return nums[n-k]
    def quickSelect(self,nums,start,end,k,n):
        
        if(start >= (end -1)):
            return    
        pivot = random.randint(start,(end-1))
        
        nums[pivot],nums[start] = nums[start],nums[pivot]
        low = start - 1
        mid = start
        high = end
        pivot_val = nums[start]
        while True:
            if(mid >= high):
                break
            if(mid >= end):
                break
            if(nums[mid] == pivot_val):
                mid += 1
            elif(nums[mid] < pivot_val):
                low += 1
                nums[low],nums[mid]=nums[mid],nums[low]
                mid += 1
            else:
                high -= 1
                nums[high],nums[mid] = nums[mid],nums[high] 
                
        if((n-k) >= start and (n-k) <= low ):
            self.quickSelect(nums,start,low + 1, k , n)
        elif( (n - k) >= (low+1) and (n - k) < high):
            return
        else:
            self.quickSelect(nums,high,end ,k,n)

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4],2))