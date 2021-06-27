class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        heap = set()
        for char in sentence:
            heap.add(char)
        return len(heap) == 26
        
        