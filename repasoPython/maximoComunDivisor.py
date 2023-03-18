#1. Escribir una función que calcule el máximo común divisor entre dos números.
def maximoComunDivisor (numero1, numero2) :
    maxcd=1 
    if numero1% numero2 ==0:
        return numero2
    
    for i in range(int(numero2/2),0,-1):
        if numero1%i==0 and numero2%i==0:
            maxcd=i
            break

    return maxcd

print(maximoComunDivisor(24,6))