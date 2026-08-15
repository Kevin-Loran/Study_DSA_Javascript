def ePrimo(n):
    ePrimo = n > 1 and n % n == 0 and n % 2 > 0
    return ePrimo

print(ePrimo(13))