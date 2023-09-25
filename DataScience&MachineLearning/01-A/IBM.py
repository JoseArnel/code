
#One of them was about binary numbers in a linked-list and ordering them in some arrays and the other was about subsets and ordering those in arrays as well. No sql stuff

#Udemy should have a number of Python algorithms courses that should explain that one. Leetcode.com
#hackerrank & leetcode, data structures and leetcode

# 2 leetcode easy-medium problems
# a dummy dataset they ask you to clean, build a model,
# and make some visualizations. I used python for this

# how to fit into this role

# Write a program to find HCF of 2 numbers without recursion 
#include<iostream>
int gcd(int,int);;
int main()
{
    int m,n,ans;
    scanf("%d",&m);
    scanf("%d",&n);
    while(m!=n)
    {
        if(m>n)
        {
            m=m-n;
        }
        else
        {
            n=n-m;
        }
    }
    printf("%d",m);
    return 0;
}

#Q2. Consider a string, S, that is a series of characters, each followed by its frequency as an integer. The string is not compressed correctly, so there may be multiple occurrences of the same character. A properly compressed string will consist of one instance of each character in alphabetical order followed by the total count of that character within the string.
#include<iostream>
import java.util.*;

public class Main {
    public static String properCompression(String s) {
        StringBuilder compressedStr = new StringBuilder();

        for (int i = 0; i < s.length(); i += 2) { char c = s.charAt(i); int count = Character.getNumericValue(s.charAt(i + 1)); while (count > 0) {
                compressedStr.append(c);
                count--;
            }
        }

        return compressedStr.toString();
    }

    public static void main(String[] args) {
        String inputStr = "a3b5c2a2";
        String compressedResult = properCompression(inputStr);
        System.out.println(compressedResult);  // Output: "aaabbbbbcc"
    }
}
#Q3. Write a  C++ Program to Change Decimal Number to Binary?
include<iostream>
namespace std;
int main ()
{
  int a[10], n, i;
  cout << "Enter the number to convert: ";
  cin >> n;
  for (i = 0; n > 0; i++)
    {
      a[i] = n % 2;
      n = n / 2;
    }
  cout << "Binary of the given number= ";
  for (i = i - 1; i >= 0; i--)
    {
      cout << a[i];
    }
}

#4.C++ Program to generate Fibonacci Triangle
#include<iostream>  
using namespace std;  
int main()  
{  
    int a=0,b=1,i,c,n,j;    
    cout<<"Enter the limit: ";   
    cin>>n;    
    for(i=1; i<=n; i++)    
    {    
        a=0;    
        b=1;    
        cout<<b<<"\t";   
        for(j=1; j<i; j++)   
        {    
            c=a+b;    
          cout<<c<<"\t";    
            a=b;    
            b=c;  
        }    
        cout<<"\n";    
    }  
    return 0;  
}  

#https://prepinsta.com/ibm/coding/
# leetcode easy to medium coding questions.
# SQL quetion to fetch data
# python is algorithm
# How do you think your background aligns with IBM 

#binary tree versal code, binanry numbers in a link-list and order them in some array 
# other was subsets and odering those in arrays

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range (i + 1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
