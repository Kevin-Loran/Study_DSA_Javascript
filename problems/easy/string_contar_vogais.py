from soupsieve.util import lower

def contadorDeVogais(string):
    palavra = string.replace(" ", '').lower()
    contador = 0

    for letras in palavra:
        if letras in 'aeiou':
            contador += 1

    return contador

print(contadorDeVogais("Engenharia de Software"))