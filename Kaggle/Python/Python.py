# 1. Hello, Python

print(5 / 2)
print(6 / 2)
2.5
3.0

print(5 // 2)
print(6 // 2)
2
3


print(abs(32))
print(abs(-32))
32
32

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = (alice_candies + bob_candies + carol_candies)%3 

# Check your answer
q4.check()

# 2. Functions and Getting Help
help(round)

Docstrings
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

help(least_difference)

# Help on function least_difference in module __main__:

# least_difference(a, b, c)
#     Return the smallest difference between any two numbers
#     among a, b and c.
    
#     >>> least_difference(1, 5, -5)
#     4

print(1, 2, 3, sep=' < ')
#1 < 2 < 3


def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)
# Which number is biggest?
# 100
# Which number is the biggest modulo 5?
# 14

#ndigits
print(round(2001, ndigits=0))
# 2001
print(round(2001, ndigits=-1))
# 2000

def to_smash(total_candies, num_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % num_friends

# Check your answer
q3.check()