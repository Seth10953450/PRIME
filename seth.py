def factor(f):
    a = [i for i in range(1, f+1) if f % i == 0]
    return(a)


def primes(x):
    c = []
    for b in range(2, x+1):
        if len(factor(b)) == 2:
            c.append(b)
    return c


def sumPrimes(n):
    thePrimes = primes(n)
    return sum(thePrimes)


Input = int(input("Enter a number: "))
print("The sum of the prime numbers up to " +
      str(Input) + " is " + str(sumPrimes(Input)))
