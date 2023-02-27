class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = []
        for log in logs:
            birth_year, death_year = log
            years.append((birth_year, 1))
            years.append((death_year, -1))
            

        max_count = 0
        max_year = 0
        count = 0
        years.sort()
        for year,val in years:
            count += val
            if count > max_count:
                max_count = count
                max_year = year

        return max_year
    
    
    
                
        