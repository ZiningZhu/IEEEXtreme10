import math
if __name__ == "__main__":
    f = open("primes.txt", "w")
    primeList = [2, 3, 5, 7]
    for n in xrange(2, 10**4 * 7):
        if (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
            continue
        divisible = False
        for p in primeList:
            if (p**2 > n):
                break
            if (n // p * p == n):
                divisible = True
                break
        if not divisible:
            primeList.append(n)

    primeList.sort()
    s = str(primeList)

    f.write(s)
    f.close()
