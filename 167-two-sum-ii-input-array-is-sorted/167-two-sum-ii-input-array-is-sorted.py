# two pointer approach
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0, len(numbers)-1
        
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
                
        return [0,0]



# binary search approach
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             low = i+1
#             high = len(numbers)-1
#             while (low <= high):
#                 mid = (low + high) // 2
#                 if numbers[mid] == target - numbers[i]:
#                     return [i + 1, mid+1]
                
#                 elif numbers[mid] > target - numbers[i]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
                    
#         return [-1,-1]
         
        