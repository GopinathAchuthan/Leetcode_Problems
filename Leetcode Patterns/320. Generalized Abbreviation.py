'''
Topics: Backtracking

Time Complexity: O(n*2^n)
Auxiliary Space: O(n)
Call Stack Space: O(n)
Space Complexity: O(n)
'''
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def func(i,n,state,slate,res):
            # base case
            if i==n:
                res.append(''.join(slate))
                return
            
            # calling recursion function
            # if state is true, we can swap str with number
            if state:
                for num in range(n-i,0,-1):
                    slate.append(str(num))
                    func(i+num,n,False,slate,res)
                    slate.pop()
            # include str in the slate
            slate.append(word[i])
            func(i+1,n,True,slate,res)
            slate.pop()
            return
        
        
        res = []
        func(0,len(word),True,[],res)
        return res