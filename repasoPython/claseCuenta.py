# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
#opcional. Crear los siguientes métodos para la clase:
#● Un constructor, donde los datos pueden estar vacíos.
#● Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
#● mostrar(): Muestra los datos de la cuenta.
#● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta:

    def __intit__(self,titular, cantidad):
        self._titular=titular
        self._cantidad=cantidad

    def get_titular(self):
       return self._titular
    
    def get_cantidad(self):
        return self._cuenta
    
    def set_titular(self, titular):
        self._titular=titular
    
    def set_cuenta(self,cta):
        self.set_cuenta=cta

    def retirar_dinero(self, cant):
        return self._cantidad-cant
    
    def ingresar_dinero(self,cant):
        return self._cantidad+cant
    
    def pedir_titular(self):
     
         while not titular:
            print("Debe ingresar un titular\n")
            titular=input()

    def mostrar_informacion(self):
        print(f"El titular es {self._titular}\n y el saldo de la cuenta es {self._cantidad}\n")

cta = Cuenta()
print("Debe ingresar un titular\n")
cta.pedir_titular()
cta.ingresar_dinero(5000)
cta.mostrar_informacion()

		