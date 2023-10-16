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

def countDigits(a):
    alldigits = ''.join(map(str,a)) # cuts all digits into one string 
    counts = [0] * len(alldigits)
    for digit in alldigits:
        counts[int(digit)] += 1
    maxcount = max(counts)  
    return [digit for digit, count in enumerate(counts) if count == maxcount]

# dictionary / map
def countDigits(a):
    alldigits = ''.join(map(str,a)) # cuts all digits into one string 
    dict = {} # dictionary 

    for i in alldigits: 
        try: 
            dict[i] += 1
        except:
            dict[i] = 1
    print(dict)
    
    max = 0 
    for i in dict: 
        if(dict[i] > max):
            max = dict[i]
    l=[int(k) for k,v in dict.items() if v==max]
    return (sorted(l)) 

##a: [1, 2, 3]
##b: [1, 2, 3]
##k: 31