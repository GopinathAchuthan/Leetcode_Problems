# Minimize number of students to be removed

def removeStudents(H, N):
    # code here
    L = [0 for i in range(N)]

    for i in range(N):
        for j in range(i):
            if H[j]<=H[i] and L[j]>L[i]:
                L[i] = L[j]
        L[i]+=1

    return N-max(L)


if __name__ == '__main__':
 
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(len(A), A)
    print(removeStudents(A, len(A)))