# Day 0: Hello, World.
# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')
print(input_string)

# Day 1: Data Types
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
x = 0 
y = 0.00
z = ''
# Read and save an integer, double, and String to your variables.
x = int(input())
y = float(input())
z = input()

print(i+x)
print(d+y)
print(s+z)

# Day 2: Operators
import math
import os
import random
import re
import sys
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip_val = tip_percent/100 * meal_cost
    tax_val = tax_percent/100 * meal_cost
    print (round(meal_cost + tip_val + tax_val))
   
if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    solve(meal_cost, tip_percent, tax_percent)


#Day 3: Intro to Conditional Statements
if __name__ == '__main__':
    N = int(input().strip())
    if(N%2 == 1):
        print("Weird")
    elif(N%2 == 0 and (N >= 2 and N <= 5)):
        print("Not Weird")
    elif(N%2 == 0 and (N >= 6 and N <= 20)):
        print("Weird")
    else:
        print("Not Weird")

#Day 4: Class vs. Instance 
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if(initialAge > 0):
            self.age = initialAge
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")
            
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if (self.age < 13):
            print ("You are young.")
        elif (self.age >= 13 and self.age < 18):
            print ("You are a teenager.")
        else: 
            print("You are old.")
            
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

#Day 5: Loops
if __name__ == '__main__':
    n = int(input().strip())

for i in range(1, 11):
    print(n, "x", i,  "=", n*i)

#Day 6: Review
T = int(input())
for i in range(0,T):
    S = input()
    even = ""
    odd = ""
    for j in range(0, len(S)):
        if (j % 2 == 0):
            even += S[j]
        else:
            odd += S[j]
    print(even, odd) 

#Day 7: Arrays
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    x = ""
    for i in reversed(range(0, n)):
        x += (str(arr[i]) + " " )
    print(x)

#Day 8: Dictionaries and Maps
N = int(input())
dict_sample = {}
for i in range(0,N):
    name,number = input().split()
    dict_sample[name] = number

try:
    while True:
        x = input()
        if x != "":
            if (dict_sample.get(x) != None):
                print(x + "=" + str(dict_sample.get(x))) 
            else:
                print("Not found")
        else: 
            break
except EOFError as e:
    print ("")

#Day 9: Recursion
def factorial(n):
    # Write your code here
    if (n <= 1):
        return 1
    else:
        return (n*factorial(n-1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())

    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()

#Day 10: Binary Numbers
# 125, 1 2 4 8 16 32 64 128
# 125 % 2 == 1, max  = 1, 125//2 = 62, 3 %2 == 1, max = 1
# 62 % 2 == 0, 62 // 2 = 31, 31/2, 15 % 2 == 1, max = 1,
maximum = 0
count = 0
while (n > 0):
    if(n % 2 == 1):
        count += 1;
        if count >= maximum:
            maximum = count
    else:
        n = n//2
        count = 0
        
print(maximum)

#Day 11: 2D Arrays
if __name__ == '__main__':

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    maximum = -10000000
    sum = 0
    for i in range(4):
        for j in range(4):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            if sum > maximum:
                maximum = sum
            
    print(maximum) 
        
#Day 12: Inheritance
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):    
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.score = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sum = 0
        for i in range(len(self.score)):
            sum += self.score[i]
        avg = sum/numScores
        if (avg <= 100 and avg >= 90):
            return('O')
        elif(avg >= 80 and avg < 90):
            return('E')
        elif(avg >= 70 and avg < 80):
            return('A')
        elif(avg >= 55 and avg < 70):
            return('P')
        elif(avg >= 40 and avg < 55):
            return('D')
        else:
            return('T')
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

# Day 13: Inheritance
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook:
    #Write MyBook class
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price

    def display(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Price: " + str(self.price))
        
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

# Day 14: Scope
class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
        self.maximumDifference = 0
    
    def computeDifference(self):
        max = 0
        min = 100
        for element in self.__elements:
            if (element > max):
                max = element
            if (element < min):
                min = element
                
        self.maximumDifference = max - min
            
# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

# Day 15: Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        new = Node(data)
        
        if head is None: 
            return new
            
        current = head
        while(current.next):
            current = current.next
        current.next = new
        
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  

# Day 16: Exception - Strings to Integer
S = input()
try: 
    print (int(S))
except ValueError: 
    print ("Bad String")

# Day 17: More Exceptions 
class Calculator:
    def power(self, n, p):
        try:
            assert n >= 0 and p >= 0
            return n**p
        except AssertionError:
            return("n and p should be non-negative")

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   

# other solution
class Calculator:
    def power(self,n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return pow(n,p)

# Day 18: Queues & Stacks
import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []
    
    def pushCharacter(self, ch):
        self.stack.append(ch)
    
    def enqueueCharacter(self, ch):
        self.queue.insert(0, ch)
    
    def popCharacter(self):
        return self.stack.pop()    
    
    def dequeueCharacter(self):
        return self.queue.pop()
    
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    

# Day 19: Interfaces
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        for i in range(1, n+1):
            if(n%i == 0):
                sum += i
        return sum

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

# Day 20: Bubble Sort
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    # Write your code here  
    numSwaps = 0
    for i in range(0, n):
        for j in range(0, n-1):
            if(a[j] > a[j +1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                numSwaps += 1
        if (numSwaps == 0):
            break
        
    print("Array is sorted in " +str(numSwaps)+ " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[n-1]))
            
# Day 22: Binary Search Trees
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if (root == None):
            return -1
        if (root.left == None and root.right == None):
            return 0
        if self.getHeight(root.left) >= self.getHeight(root.right):
            return self.getHeight(root.left) + 1 
        else:  
            return self.getHeight(root.right) + 1

# Day 23: BST Level-Order Traversal
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue = []
        final = ''
        queue.append(root)

        while len(queue) != 0:
            r = queue.pop(0)
            if (r.left != None):
                queue.append(r.left)
            if (r.right != None):
                queue.append(r.right)
            final += str(r.data) + ' '

        print(final)

T=int(input())
    
# Day 24: More Linked Lists
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #W
        current = head
        first = current.data
        final = str(current.data) + " "
        
        if head is None:
            print("Empty")
        
        while (current.next):
            current = current.next
            if current.next != None:
                if current.data != current.next.data :
                    final += str(current.data) + " "
        
        if(first != current.data):
            final += str(current.data)
        print(final)

    def removeDuplicates(self,head):
        if not head: 
            return None
        current = head
        while current.next:
            if current.next.data == current.data:
                current.next = current.next.next
            else:
                current = current.next
        return head


mylist= Solution()

# Day 25: Running Time and Complexity
n_input = int(input())

for x in range (n_input):
    n =int(input())
    flag = True
    for i in range(2, n):
        if(i/n == 0):
            flag = False

    if(flag == False):
        print("Not prime")
    else: 
        print("Prime")

for x in range (n_input):
    n =int(input())
    flag = False
    if n == 1: 
        flag = True 
    for i in range(2, int(n**1/2)+1):
        if (n%i == 0):
            flag = True 
                
    if(flag == True):
        print("Not prime")
    else: 
        print("Prime")

for x in range (n_input):
    n =int(input())
    if n == 1: 
        print("Not prime")
    else:
        if(n%2 == 0 and n > 2):
            print ("Not prime")
        else: 
            for i in range(2, int(n**(1/2))+1):
                if (n%i == 0):
                    print("Not prime")
                    break
            else: 
                print("Prime")


# Day 26: Nested Logic 
returned = input().split()
due = input().split()

d1 = int(returned[0])
d2 = int(due[0])

m1 = int(returned[1])
m2 = int(due[1])

y1 = int(returned[2])
y2 = int(due[2])

fine = 0
diff = y1 - y2
if (diff <0):
    print(fine)
elif(y1 == y2):
    diff = m1 - m2
    if (m1 == m2 or diff < 0):
        diff = d1 - d2
        if (d1 == d2 or diff < 0): 
            print(fine)
        else: 
            print(15 * diff)
    else: 
        print(500*diff)
else: 
    print(10000)


# Day 27: Testing 
def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

class TestDataEmptyArray(): 
    def get_array():
        return ([])
    
class TestDataUniqueValues():  
    def get_array():
        return [3,1,2]
    def get_expected_result():
        return 1
    
class TestDataExactlyTwoDifferentMinimums():
    def get_array():
        return [3,1,1]
    def get_expected_result():
        return 1
    
def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False

def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")


# Day 28: RegEx
if __name__ == '__main__':
    N = int(input().strip())

    names = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]
        
        emailID = first_multiple_input[1]
        
        if (re.search( "@gmail\.com", emailID)):
            names.append(firstName)
            
    names.sort()
    for name in names:
        print (name)


# Day 29: Bitwise AND
# works but time inefficient 
def bitwiseAnd(N, K):
    # Write your code here
    # range(start index, stop index, step) 
    max = 0
    for x in range(N-1, 0, -1):
        for y in range(N, 1, -1):
            if (x == y):
                continue
            andd = x & y
            if (andd == 0):
                y += 1
            if (andd == K - 1):
                return(andd)
            if (andd < K and andd > max):
                max = andd
    return (max)
        
def bitwiseAnd(N, K):
    # Write your code here
    # range(start index, stop index, step) 
    max = 0
    yrange = 2
    for x in range(1, N):
        for y in range(yrange, N+1):
            if (x == y): 
                continue
            A = format(x, "b")
            B = format(y, "b")
            andd = x & y
            print ("A = " + str(int(A,2)) + ",B = " + str(int(B,2)) + "; A & B = " + str(andd))
            if (andd < K and andd > max):
                max = andd
            if (andd == 0):
                y += 1
        yrange += 1
    print(max)
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)
