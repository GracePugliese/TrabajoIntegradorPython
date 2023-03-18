#Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
#● Un constructor, donde los datos pueden estar vacíos.
#● Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#● mostrar(): Muestra los datos de la persona.
#● es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona():
     def __intit__(self, name, age, doc):
            self._nombre=name
            self._edad=age
            self._dni=doc

#Getters
     def get_nombre(self):
        return self._nombre

     def get_edad(self):
          return self._edad
     
     def get_dni(self):
          return self._dni
     
#Setters
     def set_nombre(self, name):
            if name:
                if name.isalpha():
                   self._nombre=name
                else:
                      raise ValueError("La cadena debe ser solo  letras")
            else:
                        raise ValueError("La cadena está vacia.")

     def set_edad(self, age):
            #if  age.isdigit() and age>0:#TypeError: '>' not supported between instances of 'str' and 'int' PS C:\Users\Graciela\OneDrive\Documentos\Programacion\Cursos\Codo a codo\repasoPython>
             if isinstance(age, int) and age >= 0:  
                 self._edad=age
             else:
                   raise ValueError("El dato ingresado no es un número")
    
     def set_dni(self, doc):
        if doc:
             if doc.isdigit():
                 self._dni=doc
             else:
                   raise ValueError("La cadena debe ser de digitos")
        else:
                   raise ValueError("La cadena está vacia.") 
    
     def es_mayor_de_edad(self):
            if(edad>=18):
                return True
            else:
                return False
     
     def mostrar(self):
            print(f"Nombre: {self._nombre}\n, Edad: {self._edad}\n, Nro. Documento: {self._dni}\n")
     
nombre=input("Ingrese su nombre\n")
edad=int(input("Ingreses su edad\n"))
documento=input("Ingrese su documento\n")

p1 =Persona()
p1.set_nombre(nombre)
p1.set_edad(edad)
p1.set_dni(documento)
p1.mostrar()
print(p1.es_mayor_de_edad())
          

         