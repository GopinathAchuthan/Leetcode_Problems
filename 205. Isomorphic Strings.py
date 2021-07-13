# Method using string
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def getPosStr(s):
            out = []
            heap = {}
            for i in range(len(s)):
                if s[i] not in heap:
                    heap[s[i]] = str(i)
                out.append(heap.get(s[i]))
            return "".join(out)
        
        if getPosStr(s) == getPosStr(t):
            return True
        else:
            return False
            

# Method using list of list
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def getLettersPosition(s):
            heap = {}
            for i in range(len(s)):
                if s[i] in heap:
                    heap[s[i]].append(i)
                else:
                    heap[s[i]] = [i]
            return sorted(heap.values())
        
        pos1 = getLettersPosition(s)
        pos2 = getLettersPosition(t)
        
        if len(pos1) == len(pos2):
            N = len(pos1)
            for i in range(N):
                if len(pos1[i]) == len(pos2[i]):
                    for j in range(len(pos1[i])):
                        if pos1[i][j] !=pos2[i][j]: return False
                else:
                    return False
            return True
        else:
            return False