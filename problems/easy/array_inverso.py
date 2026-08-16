def inverter(array):
    inverso = []
    contadorInverso = len(array) - 1
    for i in range(len(array)):
        inverso.append(array[contadorInverso])
        contadorInverso -= 1
    return inverso

array = [4, 4, 18, 4, 6]
inverso = inverter(array)
print(inverso)