def merge(A, B):
    if ((len(A) == 0) or (len(B) == 0)):
        return A+B
    else:
        if (A[0] < B[0]):
            return [A[0]] + merge(A[1:], B)
        else:
            return [B[0]] + merge(A, B[1:])

def mergesort(L):        
    if (len(L) < 2):
        return L
    else:
        mid = len(L)/2
        left = mergesort(L[:mid])
        right = mergesort(L[mid:])
        return merge(left, right)
