# Project-Euler-Solutions
|Python 3|

Here are the solutions to problems taken from projecteuler.net



# 603. Substring sums of prime concatenations
> https://projecteuler.net/problem=603
This problem combines three functions. First we will find a basic solution which explains each function and the way it works.
Then we will find a solution which can handle larger numbers. 


### The Problem:
Let S(n) denote the sum of all contiguous integer-substrings that can be formed from the integer n. The substrings need not be distinct. 
For example: 

   *S(2024) = 2 + 0 + 2 + 4 + 20 + 02 + 24 + 202 + 024 + 2024 = 2304*

Let P(n) be the integer formed by concatenating the first n primes together.	 
For example: 

   *P(7) = 2357111317*

Let C(n,k) be the integer formed by concatenating k copies of P(n) together. 	
For example:

   *C(7,3) = 235711131723571113172357111317*

Evaluate S(C([10]^6,[10]^12 ))  MOD ([10]^9+7)


### The S(n) Function:
We need to find a way to extract all the adjacent integer substrings of the given number n. The number of substrings is dependent on the number of digits which make up the value n. 

For smaller values we may use a list separating the digits inside the value n. Then use a pointer and an incrementing variable (which denotes the size of the substring) to generate all the possible substrings.

Take the example *2024*:



inc = 1

pointer = 0

| 2 | 0 | 2 | 4 |
|---|---|---|---|
| ^ | 	|   |   |

pointer = 1

| 2 | 0 | 2 | 4 |
|---|---|---|---|
|   | ^ |   |   |

pointer = 2

| 2 | 0 | 2 | 4 |
|---|---|---|---|
|   | 	| ^ |   |

pointer = 3

| 2 | 0 | 2 | 4 |
|---|---|---|---|
|   | 	|   | ^ |

inc = 2

pointer = 0

| 2 | 0 | 2 | 4 |
|---|---|---|---|
| ^ | ^ |   |   |

pointer = 1

| 2 | 0 | 2 | 4 |
|---|---|---|---|
|   | ^ | ^ |   |

pointer = 2

| 2 | 0 | 2 | 4 |
|---|---|---|---|
|   | 	| ^ | ^ |

inc = 3

pointer = 0

| 2 | 0 | 2 | 4 |
|---|---|---|---|
| ^ | ^ | ^ |   |

pointer = 1

| 2 | 0 | 2 | 4 |
|---|---|---|---|
|   | ^ | ^ | ^ |

inc = 4

pointer = 0

| 2 | 0 | 2 | 4 |
|---|---|---|---|
| ^ | ^ | ^ | ^ |

My solution for this:

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
    
    return sum(intsubstr)
    
```
