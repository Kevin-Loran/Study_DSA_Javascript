def emaior(x, y, z):

    if x == y == z:
        return "iguais"
    elif x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z


print(emaior(120, 120, 120))