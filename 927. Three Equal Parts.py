class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        numOnes = 0 
        heap = {}
        for i, val in enumerate(arr):
            numOnes+=val
            if val==1:
                heap[numOnes] = i
        
        if numOnes == 0:
            return [0,len(arr)-1]
        elif numOnes%3==0:
            T = numOnes//3
            z = len(arr)-heap[3*T]-1 # (arr.length-1) - 1's last appearance
            i1,j1 = heap[1],heap[T]+z
            i2,j2 = heap[T+1],heap[2*T]+z
            i3,j3 = heap[2*T+1], len(arr)-1
            if j1<i2 and j2<i3 and arr[i1:j1+1]==arr[i2:j2+1]==arr[i3:j3+1]:
                return [j1,j2+1]
         
        return [-1,-1]
            