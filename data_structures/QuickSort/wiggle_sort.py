from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums,key = lambda x:x,reverse=True)
        
        n = len(nums)
        out_array = [0]*n
        j = 0
        for i in range(1,n,2):
            out_array[i] = arr[j]
            j += 1
        
        for i in range(0,n,2):
            out_array[i] = arr[j]
            j += 1
        nums[:] = out_array
        

sol = Solution()
print(sol.wiggleSort([1,5,1,1,6,4]))