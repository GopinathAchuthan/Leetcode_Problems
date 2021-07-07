class Solution:
    def __init__(self):
        self.allPossibleChars = list(string.ascii_lowercase)
    
    def nextAllPossibleWords(self, word):
        charList = list(word)
        res = []
        for i in range(len(charList)):
            temp = charList[i]
            for char in self.allPossibleChars:
                charList[i] = char
                res.append("".join(charList))
            charList[i] = temp
        return res
    
    def allPossibleSequence(self, levelWords, heap, endWord):
        res = []
        numLevel = len(levelWords)
            
        def dfs(seq,level,endWord,numLevel):
            word = seq[-1]
            nextWords = heap[word]
            if endWord in nextWords:
                res.append(seq+[endWord])
                
            level+=1
            for nextWord in nextWords:
                if level<numLevel and nextWord in levelWords[level]:
                    dfs(seq+[nextWord],level,endWord,numLevel)
        
        dfs(levelWords[0],0,endWord, numLevel)
        
        return res
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        
        heap = {}
        queue = [beginWord]
        if beginWord in wordList:
            wordList.remove(beginWord)
        levelWords = []
        levelWords.append(queue)
        found = False
        
        while(queue):
            newQueue = []
            for currWord in queue:
                if endWord == currWord:
                    found = True
                nextWords = self.nextAllPossibleWords(currWord)
                heap[currWord] = set()
                for nextWord in nextWords:
                    if nextWord in wordList:
                        heap[currWord].add(nextWord)
                        newQueue.append(nextWord)
            
            # check whether the endword is found or not
            if found:
                levelWords[-1] = [endWord]
                break
            else:
                queue = newQueue
                levelWords.append(queue)
            
            # remove words from wordList
            for word in newQueue:
                wordList.discard(word)
        
        
        # Final Check
        if found:
            res = self.allPossibleSequence(levelWords,heap,endWord)
            return res
        else:
            return []
            
            
        