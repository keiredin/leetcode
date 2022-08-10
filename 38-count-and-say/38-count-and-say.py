class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        
        res = self.countAndSay(n-1)
        count = 1
        idx = 0
        answ = ""

        for i in range(1,len(res)):
            count += 1
            if res[i] != res[idx]:
                count -= 1
                answ += str(count)+res[idx]
                idx = i
                count = 1
        if count > 0:
            answ += str(count)+res[idx]
        return answ
                
        # count = Counter(res)
        # print(n,count,res)
        # res = ""
        # for key in count:
        #     res += (str(count[key])+key)
        # return res
        