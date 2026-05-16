from typing import List
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if(k < 0 or k > n):
            raise IndexError(f"k out of bounds")        
        return self.quickSelect(nums,0,n,k,n)
        
    def quickSelect(self,nums,start,end,k,n):
        if(start != (end -1)):    
            pivot = random.randint(start,(end-1))
        elif(end - start == 1):
            pivot = start
        nums[pivot],nums[end-1] = nums[end-1],nums[pivot]
        i = start - 1
        for j in range(start,end-1,1):
            if(nums[j] < nums[end-1]):
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
        nums[i+1],nums[end-1] = nums[end-1],nums[i+1]
        if((n-k) == (i+1)):
            return nums[i+1]
        elif( (n - k) < (i+1)):
            return self.quickSelect(nums,start,i +1 ,k,n)
        else:
            
            return self.quickSelect(nums,i+2,end ,k,n)


sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4],2))