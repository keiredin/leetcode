class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()  
        arr[0] = 1 
        maxEle = 1

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1] + 1
            maxEle = max(maxEle, arr[i])

        return maxEle
        