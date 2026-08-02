def calculaBase(n,elevado):
    if elevado == 0:
        return 1

    return n * calculaBase(n,elevado-1)

print(calculaBase(5,3))