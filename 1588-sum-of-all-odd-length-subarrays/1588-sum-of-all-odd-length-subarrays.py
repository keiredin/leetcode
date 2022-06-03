class Solution:
	def sumOddLengthSubarrays(self, arr: List[int]) -> int:
		result = 0
		for i in range(len(arr)):
			for j in range(i + 1, len(arr) + 1, 2):
				# print(i,j)
				result += sum(arr[i:j])

		return result
            
        