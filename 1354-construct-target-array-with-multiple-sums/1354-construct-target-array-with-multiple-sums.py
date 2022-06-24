class Solution:
	def isPossible(self, target: List[int]) -> bool:

		heapq._heapify_max(target)
		s = sum(target)

		while target[0] != 1:
			sub = s - target[0]
			if sub == 0: return False
			n = max((target[0] - 1) // sub, 1)
			s -= n * sub
			target0 = target[0] - n * sub
			if target0 < 1: return False
			heapq._heapreplace_max(target, target0)

		return True



# class Solution:
#     def isPossible(self, target: List[int]) -> bool:
#         h = [-n for n in target]
#         total = sum(target)
#         heapify(h)
        
#         while h[0] != -1:
#             candidate = -heappop(h)
#             rest_of = total - candidate
            
#             if rest_of <= 0 or candidate <= rest_of: return False
#             prev = candidate % rest_of
            
#             heappush(h,-prev)
#             total -= candidate
#             total += prev
            
#         return True