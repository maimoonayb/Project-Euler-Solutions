# 512. Sums of totients of powers
> projecteuler.net/problem=512

### The Problem

Let φ(n) be Euler's totient function.

Let *f(n) = (∑φ(n^i)) mod (n+1)*

Let *g(n) = ∑f(i)*

**NOTE:** All sums are taken from i = 1 to n

g(100) = 2007

Find g(5 × 10^8)

### The Totient Function φ(n)

The Totient function, φ(n), is defined by the number of positive integers <= n, which are *co-prime* to n.
Two integers are co-prime if they share no common factors.
*For example, 14 and 15 are relatively prime.*
1 is considered to be relatively prime to all numbers. A number which is <= n, and relatively prime to n is defined as a totative. So φ(n) = number of totatives of n.

 For example,  φ(14):

  *Consider the values <= 14. Totatives are: 1, 3, 5, 9, 11 and 13.*
  
  *Therefore φ(14) = 6*
  
First, we require a function to determine whether or not two values are coprime. There is a built in function that can be imported from the 'math' module. But for the purpose of understanding the mathematics behind the solution, we will code the function ourselves.

*Euclid's Algorithm*

This is an algorithm which can determine the Highest Common Factor (HCF) of two integers. Note that if the HCF of two values is 1, then that implies that the two numbers are coprime.



```python
#Using Euclid's Algorithm
def coprime(a,b):
    temp = 1
    while temp <> 0:
        temp = a % b
        a = b
        b = temp
    if a == 1:
        return True
    else:
        return False

#Find the number of totatives
def phi(n):
    noOfTotatives = 0
    for i in range (1,n):
        if coprime(i, n) == True:
            noOfTotatives += 1
    return noOfTotatives
```



