class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = 0
        while(i<len(nums) and nums[i]==0):
            i+=1
        if i>=len(nums):
            return 0
        
        positiveWindow = 0
        negativeWindow = 0
        negaStart, negaEnd = 0, 0
        startWindow, endWindow = 0, 0
        result = float('-inf')
        
        for num in nums:
            # if num is positive
            if num>0:
                if not positiveWindow:
                    positiveWindow = num
                else:
                    positiveWindow *= num
            # if num is zero        
            elif num==0:
                result = max(result, 0)
                if positiveWindow:
                    result = max(result, positiveWindow)
                if negativeWindow:
                    endWindow = positiveWindow if positiveWindow>0 else 1
                    if negativeWindow>0:
                        result = max(result, startWindow*negativeWindow*endWindow)
                    else:
                        negaEnd = 1 if negaEnd == 0 else negaEnd
                        if negaStart == negativeWindow:
                            result = max(result, negativeWindow)
                        else:
                            result = max(result, startWindow*(negativeWindow//negaEnd),
                                         (negativeWindow//negaStart)*endWindow)
                positiveWindow = 0
                negativeWindow = 0
                negaStart, negaEnd = 0, 0
                startWindow, endWindow = 0, 0
                        
            # if num is negative            
            else:
                if positiveWindow:
                    result = max(result, positiveWindow)
                    
                if not negativeWindow:
                    negativeWindow = num
                    negaStart = num
                    startWindow = positiveWindow if positiveWindow>0 else 1
                else:
                    negaEnd = num
                    negativeWindow *= num
                    negativeWindow *= positiveWindow if positiveWindow>0 else 1
                
                positiveWindow = 0
        
        # Final check        
        if positiveWindow:
            result = max(result, positiveWindow)
        if negativeWindow:
            endWindow = positiveWindow if positiveWindow>0 else 1
            if negativeWindow>0:
                result = max(result, startWindow*negativeWindow*endWindow)
            else:
                if not negaEnd:
                    result = max(result, negativeWindow)
                else:
                    result = max(result, startWindow*(negativeWindow//negaEnd),
                                 (negativeWindow//negaStart)*endWindow)
                
        return result