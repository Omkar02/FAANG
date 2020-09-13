import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Math', Difficult='Medium')

# Sieve of Eratosthenes


def countPrimes(n):
    primes = [True for _ in range(n)]
    primes[0], primes[1] = False, False

    i = 2
    while i**2 < n:
        if primes[i]:
            for j in range(i**2, n, i):
                # print(j)
                primes[j] = False
        i += 1

    return sum(primes)


n = 10
print(countPrimes(n))
