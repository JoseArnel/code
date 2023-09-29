
def reverseArray(a):
    arr = []
    for i in range(len(a)-1, -1, -1):
        arr.append(a[i])
    return(arr)
    
def miniMaxSum(arr):
    arr.sort()
    max = 0
    min = 0
    for i in range(0, len(arr)-1):
        min += arr[i]
    for j in range(1, len(arr)):
        max += arr[j]
    print(min, max)
