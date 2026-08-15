def fatorial(n):
    fatorial = n
    for i in range (n-1, 1, -1):
        fatorial *= i

    return fatorial

print(fatorial(5))