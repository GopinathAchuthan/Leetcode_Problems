class Solution:
    def __init__(self):
        self.alpha = list(string.ascii_lowercase)
        
    def nextPossibleWords(self,word):
        charList = list(word)
        res = []
        
        for i in range(len(charList)):
            temp = charList[i]
            for char in self.alpha:
                charList[i] = char
                res.append("".join(charList))
            charList[i] = temp
        return res
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        queue = [beginWord]
        if beginWord in wordList:
            wordList.remove(beginWord)
        
        level = 0
        
        while(queue):
            newQueue = []
            level+=1
            for currWord in queue:
                if currWord == endWord: return level
                neighbors = self.nextPossibleWords(currWord) 
                for word in neighbors:
                    if word in wordList:
                        newQueue.append(word)
                        wordList.remove(word)
            queue = newQueue
            
        return 0
        
        