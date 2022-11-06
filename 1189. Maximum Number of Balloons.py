'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array, Hashmap
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        mem = set("balon")
        
        for char in text:
            if char in mem:
                dic[char] += 1
        
        maxCount = min(dic['b'], dic['a'], dic['l']//2, dic['o']//2, dic['n'])
        
        return maxCount