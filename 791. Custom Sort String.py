class Solution:
    def partition(self,left,right,array,priority):
        pivot = array[right]
        i = left
        for idx in range(left,right):
            if priority[array[idx]]<priority[pivot]:
                array[idx], array[i] = array[i],array[idx]
                i+=1
        array[i], array[right] = array[right],array[i]
        return i
        
    def quickSort(self,left,right,array,priority):
        if left<right:
            p = self.partition(left,right,array,priority)
            self.quickSort(left,p-1,array,priority)
            self.quickSort(p+1,right,array,priority)
            
    def customSortString(self, order: str, string: str) -> str:
        orderMem = defaultdict(lambda: 26)
        for i,letter in enumerate(order):
            orderMem[letter] = i
        string = [letter for letter in string]
        self.quickSort(0,len(string)-1, string, orderMem)
        return "".join(string)
        