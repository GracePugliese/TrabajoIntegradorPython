# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
#opcional. Crear los siguientes métodos para la clase:
#● Un constructor, donde los datos pueden estar vacíos.
#● Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
#● mostrar(): Muestra los datos de la cuenta.
#● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta:

    def  __init__(self,titular='',cantidad=0):      
        self._titular=titular
        self._cantidad=cantidad

    def get_titular(self):
       return self._titular
    
    def get_cantidad(self):
        return self._cantidad
    
    def set_titular(self, titular):
        self._titular=titular
    
    def set_cantidad(self,cantidad):
        self.set_cantidad=cantidad

    def __str__(self):
            return "{} {}".format( self._titular, self._cantidad)

    def retirar_dinero(self):
         print("Debe retirar una cantidad \n")
         cant=int(input())      
         self._cantidad-=cant
         return self._cantidad
    
    def ingresar_dinero(self):
        print("Debe ingresar una cantidad \n")
        cant=int(input())      
        self._cantidad+=cant
        return self._cantidad
       
    
    def pedir_titular(self):    
        sinTitular= True
        while sinTitular: 
            print ("Ingrese un titular.") 
            titular=input()
            self.set_titular(titular)
            if titular != "":
               sinTitular =False
       

    def mostrar_informacion(self):
        print(f"El titular es {self._titular}\n y el saldo de la cuenta es {self._cantidad}\n")

cta = Cuenta()
cta.pedir_titular()
cta.ingresar_dinero()
cta.retirar_dinero()
cta.mostrar_informacion()
		
