class Solution:
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            left, right = i+1, len(num) - 1
            while left < right:
                sum = num[i] + num[left] + num[right]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
            
        return result
        
        