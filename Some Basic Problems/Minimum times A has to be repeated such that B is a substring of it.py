# Minimum times A has to be repeated such that B is a substring of it

'''
Given two strings A and B. Find minimum number of times A has to be 
repeated such that B is a Substring of it. If B can never be a substring
then return "-1"
'''

class Solution:
    def minRepeats(self, A, B):
        # code here 
        lenA = len(A)
        lenB = len(B)
        # if length of A is smaller than length of B
        if lenA<lenB:
            ans = 1
            i,j = 0,lenA
            while(i<lenA):  # check for first repeat match
                if A[i:]==B[:j]:
                    break
                i+=1
                j-=1
                
            if i<lenA:  
                i = j
                j = i+lenA
                while(j<=lenB): # check inbetween repeat match
                    if A == B[i:j]:
                        ans+=1
                        i = j
                        j = i+lenA
                    else:
                        return -1
                if i<lenB and j>lenB:   # check for last repeat match
                    if A[:lenB-i]==B[i:]:
                        return ans+1
                    else:
                        return -1
                return ans
            else:
                return -1
        # if length of A is greater than length of B
        else:
            i,j = 0,lenB
            while(j<=lenA):
                if A[i:j] == B:
                    return 1
                i+=1
                j+=1
            return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A,B))
