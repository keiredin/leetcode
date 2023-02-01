class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,0,len(nums)-1)
        return nums
        
        
    def mergeSort(self,arr,start,end):
        if end - start + 1 <= 1:
            return arr
        
        middle = (end + start) // 2
        
        #sortLeft
        self.mergeSort(arr, start, middle)
        
        #sort right half
        self.mergeSort(arr, middle + 1, end)
        
        #merge the two half
        self.mergeArray(arr, start, middle, end)
        
    def mergeArray(self,arr, start, middle, end):
        leftSubArray = arr[start: middle+1]
        rightSubArray = arr[middle+1: end + 1]
        i,j = 0,0
        k = start
        
        while i < len(leftSubArray) and j < len(rightSubArray):
            if leftSubArray[i] <= rightSubArray[j]:
                arr[k] = leftSubArray[i]
                i += 1
            else:
                arr[k] = rightSubArray[j]
                j += 1  
                
            k += 1
            
            
        # One of the halfs will have elements remaining
        while i < len(leftSubArray):
            arr[k] = leftSubArray[i]
            i += 1
            k += 1
        while j < len(rightSubArray):
            arr[k] = rightSubArray[j]
            j += 1
            k += 1
        
        