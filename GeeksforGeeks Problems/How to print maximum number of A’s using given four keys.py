# Special Keyboard
# How to print maximum number of A’s using given four keys
# https://www.geeksforgeeks.org/how-to-print-maximum-number-of-a-using-given-four-keys/

'''
Imagine you have a special keyboard with the following keys: 

Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Find maximum numbers of A's that can be produced by pressing keys on the special keyboard N times. 
'''

class Solution:
    def optimalKeys(self, N):
        # code here
        heap = [i+1 for i in range(N)]
        
        for i in range(6,N):
            heap[i] = max(2*heap[i-3],3*heap[i-4],4*heap[i-5])
        
        return heap[N-1]