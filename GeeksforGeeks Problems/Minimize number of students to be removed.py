'''
**Minimize number of Students to be removed**

N Students of different heights are attending an assembly. 
The heights of th students are represented by an array H[].
The problem is that if a student has less or equal height 
than the students standing in front of him, then he/she 
cannot see the assembly. Find the minimum number of students 
to be removed such that maximum possible numbers of students
can see the assembly.

Expected Time Complexity: O(N log N)
Expected Auxiliary Space: O(N)

Constraints:
1<=N<=10^5
1<=H[i]<=10^5

'''


def removeStudents(H, N):
    # code here
    L = [H[0]]
    
    for curr in H[1:]:
        if L[-1]<curr:
            L.append(curr)
        else:
            index = findSmallestBigNumberIndex(curr,L)
            print(index)
            L[index] = curr

    return N-len(L)


def findSmallestBigNumberIndex(key, arr):
    left = 0
    right = len(arr)

    while(left<=right):
        mid = (right+left)//2
        if arr[mid] == key:
            return mid
        elif arr[mid]<key:
            if mid+1<len(arr) and arr[mid+1]>key:
                return mid+1
            else:
                left = mid+1
        else:
            if mid-1>0 and arr[mid-1]<key:
                return mid
            else:
                right = mid-1
    return mid

if __name__ == '__main__':
 
    A = [1, 8, 4, 4, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    
    print(len(A), A)
    print(removeStudents(A, len(A)))