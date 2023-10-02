

# easy. 389. Find the Difference 
def findTheDifference(self, s: str, t: str) -> str:
        n = len(t)
        sum = 0 
        sum2 = 0
        for i in range(len(s)):
          sum = ord(s[i]) + sum
        for i in range(len(t)):
            sum2 = ord(t[i]) + sum2

        c = sum2 - sum
        return(chr(c))

def isPalindrome(self, x: int) -> bool:
    reversed_num = 0
    original = x

    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    return x == reversed_num or x == reversed_num // 10