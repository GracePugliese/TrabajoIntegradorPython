#Escribir una función que calcule el mínimo común múltiplo entre dos números
def minimoCmunDivisor (numero1, numero2) :
    z=max(numero1,numero2)
    while True:
        if(z% numero1==0) and (z% numero2==0):
            return z
        z+=1


print(minimoCmunDivisor(5,8))
    