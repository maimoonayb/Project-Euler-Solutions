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
    

print (S(2024))


def isPrime(number):
    prime = True
    for i in range (1,number):  
        if i<>1 and number % i == 0:
            prime = False
    return prime

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



def C(n,k):
    nPrimes = str(P(n))
    newval = ''
    for i in range(k):
        newval = newval + nPrimes
    return int(newval)

print (C(7,3))


#print (S(C(10**6,10**12)) % (10**9+7))
# Try to avoid the long stuff by using numpy instead of for loops!!
