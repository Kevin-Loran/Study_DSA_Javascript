def ePalindromo(string):
    palindromo = []
    i = 0
    for letra in range(len(string) -1, -1 , -1):
        palindromo.append(string[letra])
    return "".join(palindromo) == string


print(ePalindromo('radar'))
