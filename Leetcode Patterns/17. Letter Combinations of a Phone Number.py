# Time Complexity: O(N*4^N)
# Space Complexity: O(N)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                 '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'}
        digits.replace('0','').replace('1','')
        res = []
        if len(digits)>0:
            self.__helper(digits, 0, phone, '', res)
        return res
    def __helper(self, digits, i, phone, slate, res):
        if i==len(digits):
            res.append(slate)
            return
        for char in phone[digits[i]]:
            self.__helper(digits, i+1, phone, slate+char, res)
        