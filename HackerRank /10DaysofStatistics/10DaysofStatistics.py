# Enter your code here. Read input from STDIN. Print output to STDOUT

#Day 0: Mean, Median, Mode
size = int(input())
numbers = list(map(int, input().split()))

#mean
average = 0
for i in numbers:
    average += i
mean = average/size

#median
sort = numbers.sort()
if(size % 2 != 0):
    middle = size/2
    median = numbers[int(middle)]
else:
    middle = size/2
    median = (numbers[int(middle)] + numbers[int(middle-1)])/2

#mode
counter = 0
for i in numbers:
    curr_freq = numbers.count(i)
    if(curr_freq > counter):
        counter = curr_freq
        mode = i
    
print(str(mean) + "\n" + str(median) + "\n" + str(mode))


#more efficient using libraries
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))

#Day 0: Weighted Mean
import math
import os
import random
import re
import sys

def weightedMean(X, W):
# Write your code here
    weight = 0; ssum = 0
    for i in range(len(X)):
        weight += W[i]
        ssum += X[i]*W[i]
    print("%.1f" % float(ssum/weight))

if __name__ == '__main__':

    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)

# Day 1: Quartiles
import math
import os
import random
import re
import sys

def median(arr):
    mid = len(arr)//2
    if len(arr)%2 != 0:
        return arr[mid]
    else:
        return (arr[mid] + arr[mid-1])/2
    
def quartiles(arr):
    arr.sort()
    size = len(arr)
    mid = size//2
    result = []
    
    if size%2 !=0:
        q1 = median(arr[0: mid])
        m = arr[mid]
        q3 = median(arr[mid+1: size])
    else:
        q1 = median(arr[0:mid])
        m = (arr[mid] + arr[mid-1])/2
        q3 = median(arr[mid: size])
        
    return [int(x) for x in [q1, m, q3]]
    
if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

# Day 1:Interquartile Range
import math
import os
import random
import re
import sys

def median(arr):
    n = len(arr)
    mid = n//2
    if n % 2 != 0:
        return arr[mid]
    else:
        return (arr[mid] + arr[mid-1]) /2
        
def interQuartile(values, freqs):
    arr = []
    for i in range(len(values)):
        for j in range(freqs[i]):
            arr.append(values[i])
    n = len(arr)
    arr.sort()
    mid = n // 2
    if (n%2 != 0):
        q1 = median(arr[0:mid])
        q3 = median(arr[mid+1: n])
    else:
        q1 = median(arr[0:mid])
        q3 = median(arr[mid:n])
    result = q3 - q1
    print("{:.1f}".format(result))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)

#Day 1: Standard Deviation
import math
import os
import random
import re
import sys

def stdDev(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i]
    mean = sum / n

    ssum = 0
    for i in range(n):
        ssum += int(((arr[i] - mean)**2))
    print("{:.1f}".format(math.sqrt(ssum/n)))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)


# Day 4: Binomial Distribution I
# P(x) = (n / x) p**x q**(n-x)
# n = 6
# x = 3

# 1.09 : 1
# P(x) = 
# 1.09 + 1 = 2.09
# P(0.521) = p = 1.09/2.09
# q = 1 - p = 0.479

# (n / x) = nCr = 6C3 = 20
# = 20 *((0.521)**3) *(0.479**(6-3))

# 0.696

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def fact(n):
    return 1 if n == 0 else n*(fact(n-1))

def comb(n , r):
    return fact(n) / (fact(r) * (fact(n - r)))

def B(x, n, p):
    q = 1-p
    return (comb(n, x) * p**x * (q)**(n-x))

# atleast 3, x > 3
def BinomialDistrubution(a, b):
    p = a / (a+b)
    total = 0
    for i in range(3, 7):
        total += B(i, 6, p)
    print(round(total,3))
    

if __name__ == '__main__':
    a, b = list(map(float, input().split(" ")))
    BinomialDistrubution(a,b)

# Day 4: Binomial Distribution II
# 12% rejected
# 10 pistions

# No more than 2 rejects 
# Or atleast 2 rejects
def fact(n):
    return 1 if n == 0 else n*(fact(n-1))

def comb(n , r):
    return fact(n) / (fact(r) * (fact(n - r)))

def B(x, n, p):
    q = 1-p
    return (comb(n, x) * p**x * (q)**(n-x))

def BinomialDistrubution(p, n):
    total = 0
    for i in range(0, 3):
        total += B(i, n, p)
    print(round(total,3))
    total2 = 0
    for i in range(2,10):
         total2 += B(i, n, p)
    print(round(total2,3))
    
        
if __name__ == '__main__':
    m, n = list(map(int, input().split(" ")))
    m = m / 100
    BinomialDistrubution(m,n)

# Day 4: Geometric Distribution I
# p(d) = 1/3, 1st defect is 5th item produced
# s, s, s, s, d 
# p(s) = 2/3
# p(X = x) = q**(x-1) * p

def GeometricDistribution(p):
    q = 1 - p
    print(round(q**(5 - 1)*p, 3))

if __name__ == '__main__':
    n, d = list(map(int, input().split(" ")))
    p = n/d
    GeometricDistribution(p)

# Day 4: Geometric Distribution II
# d, s, s, s, s
# s, d, s, s, s
def GeometricDistribution(p, o):
    q = 1 - p
    summ = 0
    for i in range(1, 6):
        summ += (q**(i-1)*p)
    print(round(summ, 3))
    
if __name__ == '__main__':
    n, d = list(map(int, input().split(" ")))
    o = int(input())
    p = n/d
    GeometricDistribution(p, o)
#0.868

#Day 5: Poisson Distribution I
# P(x) = (mean ** x e ** - mean ) / x!
# mean = 2.5, P(x) = 5
import math

def factorial(n):
    return 1 if n == 0 else n*(factorial(n-1))
    
def PoissonDistribution(m, x):
    total = ((m ** x) * (math.e)**(-m))/factorial(x)
    # for i in range(0, x+1):
    #     total += ((m ** i) * (math.e)**(-m)) / factorial(i)
    print(round(total, 3))
    
if __name__ == '__main__':
    m = float(input())
    x = int(input())
    PoissonDistribution(m, x)
# 0.067

# P(x) = (mean ** x e ** - mean ) / x!

if __name__ == '__main__': 
    x, y = list(map(float, input().split(" ")))
    print(160 + (40*(x + x**2)))
    print(round(128 + (40*(y + y**2)), 3))
    
#226.176
#286.100

# E(Ca) = E(160 + 40 * X**2)
# = 160 + 40 * E(X**2)
# = 160 + 40 * (V(X) + [E(X)]**2)
# = 160 + 40 * (0.96 + 0.96 **2)


#Day 5: Normal Distribution I
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mean,sd=map(float,raw_input().split())
x=input()
y1,y2=map(float,raw_input().split())

def normalDistribution(x,mean,sd):
    return round(0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5)))),3)

print normalDistribution(x,mean,sd)
print normalDistribution(y2,mean,sd)-normalDistribution(y1,mean,sd)

# mean = 20, s.d. = 2, less than 19.5, between 20 and 22
import numpy as np

x = np.linespace(20,25)

def NormalDistribution(x, mean, sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    print(prob_density)


if __name__ == '__main__':
    m, sd = list(map(int, input().split(" ")))
    f = float(input())
    x, y = list(map(int, input().split(" ")))   
    NormalDistribution(x, m, sd)
    
# 0.401
# 0.341

#Day 5: Normal Distribution II
# mean = 70, sd = 10,  what is % 
# grade > 80, grade >= 60, grade < 60
import math

def NormalDistribution(x, m, sd):
    result = (0.5 * (1 + math.erf((x - m) / (sd * (2 ** 0.5))))*100)
    return(round(result, 2))
    
if __name__ == '__main__':
    m, sd = list(map(int, input().split(" ")))
    x = int(input())
    y = int(input())
    
    print(NormalDistribution(y, m, sd))
    print(NormalDistribution(x, m, sd))
    print(NormalDistribution(y, m, sd))
    
#15.87
#84.13
#15.87

#Day 6: The Central Limit Theorem I
# max = 9800 pounds, 49 boxes, mean = 205 pounds, and s.d = 15 pounds.
import math

def CentralLimit(max, num, mean, sd):
    mean_sum = num * mean
    sd_sum = math.sqrt(num) * sd 
    Z = (max - mean_sum) / sd_sum
    result = (0.5 * (1 + math.erf(Z / math.sqrt(2))))
    print(round(result, 4))

if __name__ == '__main__':
    max = int(input())
    num = int(input())
    mean = int(input())
    sd = int(input())

    CentralLimit(max, num, mean, sd)
    
# 0.0098

#Day 6: The Central Limit Theorem II
# mean = 2.4,  sd = 2.0, n = 100, max = 250
import math

def CentralLimit(x, n, m, sd):
    m_sum = m * n
    sd_sum = math.sqrt(n) * sd 
    Z = (x - m_sum)/ sd_sum
    result = (0.5 * (1 + math.erf(Z / math.sqrt(2))))
    print(round(result, 4))

if __name__ == '__main__':
    x = int(input())
    n = int(input())
    m = float(input())
    sd = float(input())
    
    CentralLimit(x, n, m, sd)
    
# 0.6915

# Day 6: The Central Limit Theorem III
# n = 100, mean = 500, sd = 80, P(A < x < B).= 0.95,  z = 1.96 
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    sd = int(input())
    p = float(input())
    z = float(input())
    
    sdS = sd / (100**0.5)
    
    A = m - (z * sdS)
    B = m + (z *sdS)
    
    print(round(A, 2))
    print(round(B, 2))

# 484.32
# 515.68

# Day 7: Pearson Correlation Coefficient I
import math

def mean(lst):
    llen = len(lst)
    ssum = 0
    for i in range(0, llen):
        ssum += lst[i]
    return(ssum/llen)

def sd(lst, mean):
    llen = len(lst) 
    ssum = 0
    for i in range(0, llen):
        ssum += (lst[i]-mean)**2
    # var = ssum / llen
    return(ssum)
    # return(math.sqrt(var))

def combined(lst1, lst2, xmean, ymean):
    llen = len(lst1)
    ssum = 0
    for i in range(0, llen):
        ssum += ((lst1[i]-xmean) * (lst2[i]-ymean))
    return (ssum)
    
if __name__ == '__main__':
    n = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
     
    xmean = mean(x)
    ymean = mean(y)
    xsd = sd(x, xmean)
    ysd = sd(y, ymean)
    combined = combined(x, y, xmean, ymean)
    
    r = combined / math.sqrt(xsd* ysd)
    
    print(round(r, 3))

# INPUT
# 10
# 10 9.8 8 7.8 7.7 7 6 5 4 2 
# 200 44 32 24 22 17 15 12 8 4
# OUTPUT
# 0.61

# Day 7: Spearman's Rank Correlation Coefficient
def Spearman(n, x, y):
    xSort, ySort = sorted(x), sorted(y)
    xRank, yRank = {}, {}
    
    for i in xSort:
        xRank[i] = xSort.index(i)+1
    for i in ySort:
        yRank[i] = ySort.index(i)+1
    
    d = []
    for i in range(n):
        temp = xRank[x[i]] - yRank[y[i]]
        d.append(temp**2)
        
    numerator = 6 * sum(d)
    denominator = n**3 - n    
    return(round(1-(numerator/denominator), 3))
    
if __name__ == '__main__':
    n = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
    
    print(Spearman(n, x, y))
    
# INPUT
# 10
# 10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 
# 200 44 32 24 22 17 15 12 8 4
# OUTPUT
# 0.903

#Day 8: Least Square Regression Line
xlist, ylist, x2list, xylist = [], [], [], []
for i in range(0,5):
    x, y = input().split()
    xlist.append(int(x))
    ylist.append(int(y))
    x2list.append(int(x)**2)
    xylist.append(int(x) * int(y))

xsum = sum(xlist)
ysum = sum(ylist)
x2sum = sum(x2list)
xysum = sum(xylist)

m = ((5* xysum) - (xsum * ysum)) / ((5*x2sum) - (xsum**2))
b = (ysum - (m * xsum)) / 5

y = m*(80) + b

print(y)

# 95 85
# 85 95
# 80 70
# 70 65
# 60 70
# 78.288

# Day 9: Multiple Linear Regression

#import data
import numpy as np
m,n = [int(i) for i in input().strip().split(' ')]
X = []
Y = []
for i in range(n):
    data = input().strip().split(' ')
    X.append(data[:m])
    Y.append(data[m:])
q = int(input().strip())
X_new = []
for x in range(q):
    X_new.append(input().strip().split(' '))
X = np.array(X,float)
Y = np.array(Y,float)
X_new = np.array(X_new,float)

#center
X_R = X-np.mean(X,axis=0)
Y_R = Y-np.mean(Y)

#calculate beta
beta = np.dot(np.linalg.inv(np.dot(X_R.T,X_R)),np.dot(X_R.T,Y_R))

#predict
X_new_R = X_new-np.mean(X,axis=0)
Y_new_R = np.dot(X_new_R,beta)
Y_new = Y_new_R + np.mean(Y)

#print
for i in Y_new:
    print(round(float(i),2))

from sklearn import linear_model

m, n = [int(x) for x in input().strip().split(' ')]
data = [[float(x) for x in input().strip().split(' ')] for i in range(n)]

q = int(input().strip())
inp = [[float(x) for x in input().strip().split(' ')] for i in range(q)]