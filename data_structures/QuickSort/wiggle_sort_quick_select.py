from typing import List
import random
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find median index position - completed
        n = len(nums)
        median_index = n // 2

        # find the element at that index - ongoing
        self.find_largest(nums,median_index)
        
        # do 3 way partition 
        low, high = self.dnf(nums,0,(n-1),median_index)

        # copy to output array
        output_array = [0] * n
        if(n > 1):
            if(n % 2 == 0):
                j = median_index - 1
            else:
                j = median_index

            k = n - 1
            for i in range(0,n):
                if(i%2 ==0):
                    output_array[i] = nums[j]
                    j -= 1
                else:
                    output_array[i] = nums[k]
                    k -= 1
            nums[:] = output_array
        
        return output_array
            
    def find_largest(self,nums,k):
        start_index = 0
        end_index = len(nums) - 1
        while True:
            if(end_index - start_index == 0):
                return nums[start_index]
            if(end_index - start_index < 0):
                break
            index_low,index_high = self.dnf(nums,start_index,end_index)
            if(index_low + 1 <= k and k < index_high):
                return nums[k]
            elif(k <= index_low):
                start_index = start_index
                end_index = index_low
            else:
                start_index = index_high
                end_index = end_index

    def dnf(self,nums,start,end,pivot = None):

        if pivot is None:
            pivot_index = random.randint(start,end)
        else:
            pivot_index = pivot

        nums[pivot_index],nums[start] = nums[start] , nums[pivot_index]
        pivot = nums[start]    
        low = start - 1
        high = end + 1 
        mid = start
        
        while True:
            if(mid == high):
                break
            if(mid > end):
                break
            if(nums[mid] == pivot):
                mid += 1
            elif(nums[mid] > pivot):
                high -= 1
                nums[high],nums[mid] = nums[mid],nums[high]
            else:
                low += 1
                nums[low],nums[mid] = nums[mid],nums[low]
                mid += 1
        return low,high
    
sol = Solution()
print(sol.wiggleSort([1,5,1,1,6,4]))