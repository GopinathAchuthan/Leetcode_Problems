'''
Time Complexity: O(n)
Space Complexity: O(1)

Topics: Array, String, Hash Table
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        dic = dict()

        def initializeDic():
            for key in string.ascii_lowercase:
                dic[key] = 0

        for text in strs:
            initializeDic()
            for char in text:
                dic[char] += 1
            
            key = "".join([char+str(val) for char, val in dic.items() if val>0])
            
            if key not in result:
                result[key] = []
            result[key].append(text)
        
        return result.values()
