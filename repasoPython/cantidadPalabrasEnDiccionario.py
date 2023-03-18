#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
diccionario = {}
cadena=input("Ingrese una cadena de caracteres:\n\n")
cadena=cadena.lower()  # las voy a convertir todas a miniscula para poder contarlas en caso de que sean iguales
palabras_separadas_por_espacios=cadena.split()

for  ps in palabras_separadas_por_espacios:
    if(ps in diccionario):  
        diccionario[ps]+=1  # diccionario[ps] es la posicion de la palabra
    else:
         diccionario[ps]=1 # en caso de que no este en el diccionario la agrego

# recorro el diccionario y lo imprimo
for ps in diccionario:
    cantidad_coincidencias=diccionario[ps]
    print(f"La palabra:  {ps}  se encuentra: {cantidad_coincidencias} en el dicionario.\n")





