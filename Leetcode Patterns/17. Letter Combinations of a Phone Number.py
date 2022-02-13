'''
Topics: Recursion, Backtracking

Time Complexity: O(n*4^n)
Auxiliary Space: O(n)
Call Stack Space: O(n)
Space Complexity: O(n)
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # base case
        if len(digits)==0:
            return []
        
        phone = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        def func(i,n,slate,res):
            # base case
            if i==n:
                res.append(''.join(slate))
                return
            
            # calling recursive function
            for char in phone[digits[i]]:
                slate.append(char)
                func(i+1,n,slate, res)
                slate.pop()
        
        res = []
        func(0,len(digits),[],res)
        return res
        