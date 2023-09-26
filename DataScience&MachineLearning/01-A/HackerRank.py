
def reverseArray(a):
    arr = []
    for i in range(len(a)-1, -1, -1):
        arr.append(a[i])
    return(arr)
    