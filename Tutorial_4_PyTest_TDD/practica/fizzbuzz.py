def fizzBuzz(n):
    salida = []
    for x in range(1,n+1):
        aux = ""
        if (x % 3 == 0) and (x % 5) == 0:
            aux +="fizzbuzz"
        elif (x % 3) == 0:
            aux += "fizz"
        elif (x % 5) == 0:
            aux += "buzz"
        if aux == "":
            salida.append(str(x))
        else:
            salida.append(aux)
    return salida
    
print(fizzBuzz(21))