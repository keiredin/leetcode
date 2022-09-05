class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        students = deque(students)
        sandwiches = deque(sandwiches)
        count_st = Counter(students)
        count = 0
        
        while students:
            if students[0] == sandwiches[0]:
                count += 1
                count_st[students[0]] -= 1
                students.popleft()
                sandwiches.popleft()
            else:
                students.append(students.popleft())
            
            if sandwiches and count_st[sandwiches[0]] <= 0:
                return n - count
        return 0
                
                
            
        