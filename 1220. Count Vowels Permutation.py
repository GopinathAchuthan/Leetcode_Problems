class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9+7
        aCount = 1
        eCount = 1
        iCount = 1
        oCount = 1
        uCount = 1
        
        for _ in range(1,n):
            aCountNew = (eCount+iCount+uCount)%MOD
            eCountNew = (aCount+iCount)%MOD
            iCountNew = (eCount+oCount)%MOD
            oCountNew = iCount
            uCountNew = (oCount+iCount)%MOD
            
            aCount = aCountNew
            eCount = eCountNew
            iCount = iCountNew
            oCount = oCountNew
            uCount = uCountNew
        
        return (aCount+eCount+iCount+oCount+uCount)%MOD