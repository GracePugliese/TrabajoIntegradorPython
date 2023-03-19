#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva 
#de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe
#guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
#● Un constructor.
#● Los setters y getters para el nuevo atributo.
#● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear
#un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
#● Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

from claseCuenta import Cuenta
from clasePersona import Persona

class cuentaJoven(Cuenta, Persona):

    def __init__(self, titular, cantidad=0, bonificacion=0 ): # sobre escribo el constructor
        super().__init__(titular, cantidad)      # ayuda a heredar el constructor de la clase padre. 
        self._bonificacion = bonificacion
    
    def get_bonificacion(self):
       return self._bonificacion
    
    def set_bonificacion(self, bonificacion):
        self._bonificacion=bonificacion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Cuenta Joven, con bonificacion: {self._bonificacion} %.\n")

    def es_titular_valido(self):
        if super.es_mayor_de_edad() and  self._edad<25:
            return True
        else:
            return False
        
    def retirar_dinero(self, cantidad):
       if  self.es_titular_valido():
            super().retirar(cantidad)
       else:
            print("Titular no valido")


ctajoven= cuentaJoven(cuentaJoven.pedir_titular, cuentaJoven.retirar_dinero, bonificacion=15)



      