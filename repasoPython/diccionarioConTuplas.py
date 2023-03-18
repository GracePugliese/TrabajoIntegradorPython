#Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
#palabra que contiene y la cantidad de veces que aparece (frecuencia). 
#Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la
#palabra más repetida y su frecuencia.
def palabra_mas_repetida(diccionario):
    mas_repeticiones=max(zip(diccionario.values(), diccionario.keys()))
    print(mas_repeticiones)


def frecuencia_de_palabras(cadena_de_palabras):
    diccionario = {}    
    palabras_separadas_por_espacios=cadena_de_palabras.lower().split()

    for  ps in palabras_separadas_por_espacios:
        if(ps in diccionario):  
            diccionario[ps]+=1  # diccionario[ps] es la posicion de la palabra
        else:
             diccionario[ps]=1 # en caso de que no este en el diccionario la agrego

# recorro el diccionario y lo imprimo
    for ps in diccionario:
        cantidad_coincidencias=diccionario[ps]
        print(f"La palabra:  {ps}  se encuentra: {cantidad_coincidencias} en el dicionario.\n")
    
    palabra_mas_repetida(diccionario)







frecuencia_de_palabras(input("Ingrese una cadena de caracteres:\n\n"))

