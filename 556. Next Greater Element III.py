class Solution:
    def nextGreaterElement(self, n: int) -> int:
        numList = []
        
        # converting to the list of integers
        temp = n
        while(temp!=0):
            numList.insert(0,temp%10)
            temp //=10
            
        lenN = len(numList)
        i = lenN-1
        while(i>=0):
            j = i+1
            smallMax = numList[i]
            smallMaxIndex = i
            
            # find the small integer starting index
            while(j<lenN):
                if numList[i] < numList[j]:
                    if smallMax == numList[i]:
                        smallMax = numList[j]
                        smallMaxIndex = j
                    elif smallMax > numList[j]:
                        smallMax = numList[j]
                        smallMaxIndex = j
                j+=1
            
            # rearranging the list to obtain next greater element
            if smallMax > numList[i]:
                numList[i], numList[smallMaxIndex] = numList[smallMaxIndex], numList[i]
                tempList = numList[i+1:]
                tempList.sort()
                index = i+1
                for value in tempList:
                    numList[index] = value
                    index+=1
                break
            
            i-=1
        # converting list to interger
        n2=numList[0]
        for i in numList[1:]:
            n2*=10
            n2+=i
            
        # checking the condition and constraint
        if n2>n and n2<=math.pow(2,31)-1:
            return n2
        else:
            return -1