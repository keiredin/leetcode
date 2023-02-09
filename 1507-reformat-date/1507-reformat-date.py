class Solution:
    def reformatDate(self, date: str) -> str:
        monthNumMap = {
            "Jan": "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun": "06", "Jul": "07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"
        }
        
        date = date.split(" ")
        answ = ""
        for i in range(len(date)-1,-1,-1):
            if i == 1:
                curMonth = monthNumMap[date[i]]
                answ += (curMonth + "-")
            elif i == 0:
                l = len(date[i])
                if l < 4:
                    answ += "0" + date[i][0]
                else:
                    answ += date[i][:l-2]
            else:
                answ += date[i] + "-"
                
        return answ
                
            
        