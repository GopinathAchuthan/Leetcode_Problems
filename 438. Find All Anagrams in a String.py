class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # base case
        if len(s)<len(p):
            return []
        
        # reference hash table
        pDict = dict()
        for value in p:
            if value not in pDict.keys():
                pDict[value] = 0
            pDict[value] += 1
        
        # window hash table
        pLength = len(p)
        windowDict = dict()
        
        for index in range(pLength):
            if s[index] not in windowDict.keys():
                windowDict[s[index]] = 0
            windowDict[s[index]] += 1
        
        # for first window
        result = []
        if pDict == windowDict:
            result.append(0)
        
        # for remaining window
        for index in range(1,len(s)-pLength+1):
            
            # remove first insertion in windowDict
            prevValue_S = s[index-1]
            if windowDict[prevValue_S] == 1:
                windowDict.pop(prevValue_S)
            else:
                windowDict[prevValue_S] -= 1
            
            # adding new item in the windowDict
            newValue_S = s[index+pLength-1] 
            if newValue_S not in windowDict.keys():
                windowDict[newValue_S] = 0
            windowDict[newValue_S] += 1
            
            # comparing two hash table
            if pDict == windowDict:
                result.append(index)
        
        return result
            