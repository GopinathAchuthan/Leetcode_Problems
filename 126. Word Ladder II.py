class Solution:
    def __init__(self):
        self.nextWords = {}
        self.ans = []
        
    def generateNextWord(self, word):
        letters = string.ascii_lowercase
        word = [i for i in word]
        out = set()
        for i in range(len(word)):
            temp = word[i]
            for letter in letters:
                word[i] = letter
                out.add("".join(word))
            word[i] = temp
        out.discard("".join(word))
        return out
    
    def getTransformationSeq(self, layers, idx, seq):
        if idx == len(layers):
            self.ans.append(seq)
            return
        currWord = seq[-1]
        for word in layers[idx]:
            if word in self.nextWords[currWord]:
                self.getTransformationSeq(layers,idx+1,seq+[word])
        
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        if beginWord in wordList:
            wordList.remove(beginWord)
            
        layers = []
        queue = [beginWord]
        
        while(queue):
            temp = set()
            for curr_word in queue:
                self.nextWords[curr_word] = set()
                neighbor_words = self.generateNextWord(curr_word)
                
                for word in wordList:
                    if word in neighbor_words:
                        self.nextWords[curr_word].add(word)
                temp.update(self.nextWords[curr_word])
            for word in temp:
                wordList.remove(word)
            
            if endWord in temp:
                queue = [endWord]
                layers.append(queue)
                break
            else:
                queue = list(temp)
                layers.append(queue)
        
        self.getTransformationSeq(layers, 0, [beginWord])
        
        return self.ans
