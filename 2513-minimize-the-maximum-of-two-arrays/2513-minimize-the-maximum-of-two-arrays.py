class Solution:
    def minimizeSet(self, d1: int, d2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        low,high = 1, 1e17
        while high > low + 1:
            mid = (low + high) // 2
            if (self.check(d1, d2, uniqueCnt1, uniqueCnt2, mid)):
                high = mid 
            else:
                low = mid
        
        return int(high - 1)
    
    def check(self,d1,d2,u1,u2,x):
        A = x / d1;  # A = # of numbers divisible by d1
        A_ = x - A;  # A' = # of numbers not divisible by d1
        B = x / d2;	 # B = # of numbers divisible by d2
        B_ = x - B;	 # B' = # of numbers not divisible by d2
        AIB = x / lcm(d1, d2); # A Intersection B = # of numbers divisible by BOTH d1 AND d2
        AuB = A + B - AIB;	# A Union B = # of numbers divisible by EITHER d1 OR d2
        A_I_B_ = x - (AuB);	# (A' Union B') = (A Intersection B)' = # of numbers not divisible by NEITHER OF THEM

        # needA = # of numbers needed to have atleast u1 numbers of set1, these numbers
        # don't include (A' Union B')
        
        needA = 0 if (A_ - A_I_B_ >= u1) else u1 - (A_ - A_I_B_);

        # needB = # of numbers needed to have atleast u2 numbers of set2, these numbers
        # don't include (A' Union B')
        
        needB = 0 if (B_ - A_I_B_ >= u2) else u2 - (B_ - A_I_B_);

        '''
            Why not consider (A' Union B') ?
            -> I will assign those numbers to whichever set needs it.
        '''
        

        # Available (A' Union B') value should be more than the needed # of values to make sets
        return (A_I_B_ >= needA + needB);
        
    