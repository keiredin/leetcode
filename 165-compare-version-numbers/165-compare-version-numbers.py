class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        
        diff = abs(len(version1) - len(version2))
        if diff != 0:
            if len(version1) > len(version2):
                version2.extend([0]*diff)
            else:
                version1.extend([0]*diff)
        
        for i in range(len(version1)):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
            
        
        return 0
        