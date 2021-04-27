class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        temp = []
        currWordsWidth = 0
        res = []
        
        for word in words:
            temp.append(word)
            currWordsWidth+=len(word)
            
            if currWordsWidth+len(temp)-1 > maxWidth:
                currWordsWidth -= len(word)
                temp.pop()
                totalSpace = maxWidth-currWordsWidth
                
                if len(temp) == 1:
                    line = temp[0]+' '*totalSpace
                else:
                    spaceBetweenTwoWords, extraSpace = divmod(totalSpace,len(temp)-1)
                    line = temp[0]
                    for tempWord in temp[1:]:
                        if extraSpace > 0:
                            line += ' '*(spaceBetweenTwoWords+1) + tempWord

                            extraSpace -= 1
                        else:
                            line += ' '*spaceBetweenTwoWords + tempWord
                res.append(line)
                
                temp = [word]
                currWordsWidth = len(word)
        
        # for last line
        if len(temp) == 1:
            totalSpace = maxWidth - currWordsWidth
            res.append(temp[0]+' '*totalSpace)
            
        elif len(temp) > 1:
            totalSpace = maxWidth - currWordsWidth
            
            line = temp[0]
            for word in temp[1:]:
                line += ' '+word
                totalSpace -= 1
            line += ' '*totalSpace
            res.append(line)
            
        return res
                
            
            