# 603. Substring sums of prime concatenations
> https://projecteuler.net/problem=603

This problem was taken from Project Euler, Problem 603. The solution requires us to combine three functions. First we will find a basic solution which explains each function and the way it works.
Then we will find a solution which can handle larger numbers. 


### The Problem:
Let S(n) denote the sum of all contiguous integer-substrings that can be formed from the integer n. The substrings need not be distinct. 
For example: 

   $S(2024) = 2 + 0 + 2 + 4 + 20 + 02 + 24 + 202 + 024 + 2024 = 2304$

Let P(n) be the integer formed by concatenating the first n primes together.	 
For example: 

   $P(7) = 2357111317$

Let C(n,k) be the integer formed by concatenating k copies of P(n) together. 	
For example:

   $C(7,3) = 235711131723571113172357111317$

Evaluate $S(C([10]^6,[10]^12 ))  MOD ([10]^9+7)$


### The S(n) Function:
We need to find a way to extract all the adjacent integer substrings of the given number n. The number of substrings is dependent on the number of digits which make up the value n. 

For smaller values we may use a list separating the digits inside the value n. Then use a pointer and an incrementing variable (which denotes the size of the substring) to generate all the possible substrings.

Take the example *2 0 2 4*:

| Inc | Pointer | 2 | 0 | 2 | 4 |
| --- |  ---    |---|---|---|---|
|  1  |    0    | ^ | 	|   |   |
|  1  |    1    |   | ^ |   |   |
|  1  |    2    |   | 	| ^ |   |
|  1  |    3    |   | 	|   | ^ |
|  2  |    0    | ^ | ^ |   |   |
|  2  |    1    |   | ^ | ^ |   |
|  2  |    2    |   |   | ^ | ^ |
|  3  |    0    | ^ | ^ | ^ |   |
|  3  |    1    |   | ^ | ^ | ^ |
|  4  |    0    | ^ | ^ | ^ | ^ |

First solution implementing for and while loops:

```python
def S(n):
    digits = []
    digits.extend(str(n)) #digits are put in as a string
    
    r = len(digits)
    intsubstr = []
    
    for substrsize in range (1,r+1):

        pointer = 0 #This should always become zero again
        
        while pointer + substrsize < r+1:

            number = ''
            for i in range (substrsize):
                number = number + digits[pointer + i]

            intsubstr.append(int(number))
            pointer += 1  #increment the pointer
    
    return sum(intsubstr) #This adds all elements in the list
    
print (S(2024))
```

Output:
```
2034
```
This result is as expected. We next we will try to develop ways in which to optimize this code in order be able to better handle large inputs of n.


### The P(n) Function:
We want to generate a function which lists the first n prime numbers. First we must look into identifying a prime number. Prime numbers only have two factors:
- One
- Itself

Using this criteria, we will write a function to identify a prime:

```python
def isPrime(number):
    prime = True
    for i in range (1,number):  
        if i<>1 and number % i == 0:
            prime = False
    return prime
```

Then using the function above, we can generate another function to calculate n primes:

```python
def P(n):
    index = 2
    primes = []

    while len(primes)<n:
        if isPrime(index) == True:
            primes.append(index)
        index += 1

    output = [str(i) for i in primes]
    return int(''.join(output))

print (P(7))
```

Output:
```
2357111317
```

### The C(n,k) Function:
This is a simple function which concatenates the solution to P(n), k times.

```python
def C(n,k):
    nPrimes = str(P(n))
    newval = ''
    for i in range(k):
        newval = newval + nPrimes
    return int(newval)

print (C(7,3))
```
Output:
```
235711131723571113172357111317
```

### Evaluating S(C(10^6,10^12 ))  MOD (10^9+7)
To break down this statement:
1. We first use the P(n) function to find the first 1,000,000 primes, and display them as a single value.
2. This value is then repeated 10^12 times to produce an extremely long value.
3. We then use the S(n) function on this result to add up all the integer substrings of the value.
4. We give the modulus of the result against (10^9)+7 because often the number is too large to be stored on the system running it.

We will use the following rule:

