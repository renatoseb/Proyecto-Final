def partition(A,low,high):
    i = low 
    pivot = A[low]
    for j in range(low + 1,high + 1):
        if A[j] <= pivot:
            i +=1
            if i != j:
                A[i] , A[j] = A[j] , A[i]
    A[i] , A[low] = A[low] , A[i]
    w = i
    return w
def quicksort(A,low,high):
    if low < high:
        w = partition(A,low,high)
        quicksort(A,low,w-1)
        quicksort(A,w+1,high)
    return A
