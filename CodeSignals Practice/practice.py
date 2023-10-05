# in preperation for Captial One Assessment 

def checkPalindrome(inputString):
    for i in range(0,int(len(inputString))//2):
        if inputString[i] != inputString[len(inputString)-i-1]:
            return False
    return True