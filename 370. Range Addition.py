class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0]*length
        for startIdx, endIdx, val in updates:
            arr[startIdx] += val
            if endIdx+1<length:
                arr[endIdx+1] -= val
        
        for i in range(1,length):
            arr[i] += arr[i-1]
        
        return arr