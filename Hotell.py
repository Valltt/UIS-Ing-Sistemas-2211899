class Node:
    def __init__(self, cedula, nombre, numhab):
        self.cedula = cedula
        self.nombre = nombre
        self.numhab = numhab
        self.siguiente = None
       
class Hotel:
    def __init__(self):
        self.cabecera = None
        self.habdisponible = set(range(1, 10))

    def check_in(self, cedula, nombre, numhab):
   
        if numhab not in self.habdisponible:
            print(f"Habitacion {numhab} ocupada")
           
            return

        nuevo_nodo = Node(cedula, nombre, numhab)
        nuevo_nodo.siguiente = self.cabecera
        self.cabecera = nuevo_nodo
        self.habdisponible.remove(numhab)
        print(f"El usuario {nombre} ha sido registrado en la habitacion {numhab}.")
       
    def check_out(self,cedula):
   
        actual= self.cabecera
        anterior= None
   
        while actual:
            if actual.cedula == cedula:
                if actual.numhab not in self.habdisponible:
                    self.habdisponible.add(actual.numhab)
                if anterior:
                    anterior.siguiente= actual.siguiente
                else:
                    self.cabecera = actual.siguiente
                print(f"El usuario {actual.nombre} se ha retirado del hotel")
                return
            anterior = actual
            actual = actual.siguiente

        print(f"El usuario con la cedula {cedula} no se encuentra registrado")
   
    def consulta_huesped(self, cedula):
   
        actual= self.cabecera
        while actual:
            if actual.cedula == cedula:
               
                print(f"Nombre del usuario: {actual.nombre}")
                print(f"Cedula del uuario: {actual.cedula}")
                print(f"Numero de Habitacion: {actual.numhab}")
               
                return
            actual = actual.siguiente

        print(f"El usuario con la cedula {cedula} no se encuentra disponible")
     
    def hab_disponible(self):
   
       print("Habitaciones que se encuentram disponibles:")
       for habitacion in self.habdisponible:
           print(habitacion)

    def hab_ocupada(self):
        print("Habitaciones que se encuentran ocupadas:")
        actual = self.cabecera
        while actual:
            print(f"Numero de habitacion {actual.numhab}  Usuario {actual.nombre}")
            actual = actual.siguiente  
           
    def Disponible (self, consultacedula=False):
   
        if consultacedula:
       
         print("Lista de huespedes por cedula:")
        disp = {}
        actual = self.cabecera
        while actual:
                disp[actual.cedula] = actual.nombre
                actual = actual.siguiente
        for cedula, nombre in disp.items():
                print(f"Cedula: {cedula} Usuario: {nombre}")
        else:
            print("Lista de huespedes por orden de llegada:")
            actual = self.cabecera
            while actual:
                print(f"Usuario: {actual.nombre} Habitacion: {actual.numhab}")
                actual = actual.siguiente

hotel = Hotel()
hotel.check_in(562413, "Julian", 2)
hotel.check_in(555478, "Camilo", 5)
hotel.check_in(234527, "Felipe", 3)
hotel.hab_ocupada()
hotel.check_out(555478)
hotel.consulta_huesped(234527)
hotel.hab_disponible()
hotel.Disponible(consultacedula=True)