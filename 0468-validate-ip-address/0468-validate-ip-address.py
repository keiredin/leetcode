class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:
            return "IPv4" if self.isIPv4(queryIP) else "Neither"
        elif queryIP.count(':') == 7:
            return "IPv6" if self.isIPv6(queryIP) else "Neither"
        else:
            return "Neither"
        
        
    def isIPv4(self,query):
        temp = query.split(".")
        if len(temp) > 4:
            return False
        
        for num in temp:
            if num.isdigit():
                if (not (0 <= int(num) < 256)) or (len(num) > 1 and num[0] == "0"):
                    return False
            else:
                return False
        return True
    
    def isIPv6(self, IP):
        temp = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for num in temp:
            if len(num) == 0 or len(num) > 4 or not all(c in hexdigits for c in num):
                return False
        return True
    
    
        
        