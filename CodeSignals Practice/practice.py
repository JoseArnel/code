# in preperation for Captial One Assessment 

def checkPalindrome(inputString):
    for i in range(0,int(len(inputString))//2):
        if inputString[i] != inputString[len(inputString)-i-1]:
            return False
    return True

def largestProduct(inputArray):
    large = -100000
    for i in range(len(inputArray)-1):
        if (large <= (inputArray[i]*inputArray[i+1])):
            large = inputArray[i]*inputArray[i+1]
    return large

def stringPairs(a, b, k):
    count = 0
    for i in range(0,len(a)):
        x = str(a[i]) + str(b[len(a)-i-1])
        if int(x) < k:
            count += 1
    return count

##a: [1, 2, 3]
##b: [1, 2, 3]
##k: 31