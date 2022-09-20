class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = float(balance)

    def __str__(self):
        print(f'El {self.nombre} {self.apellido} numero de cuenta: {self.numero_cuenta} tiene balance: {self.balance}')

    def depositar(self, dinero):
        print(type(dinero))
        print(type(self.balance))
        self.balance = self.balance + dinero

    def retirar(self, dinero):
        if self.balance - dinero >= 0:
            self.balance = self.balance - dinero


class Programa:
    def crear_cliente(self):
        nombre = input("Ingresa el nombre del cliente: ")
        apellido = input("Ingresa el apellido del cliente: ")
        numero_cuenta = input('Ingrese el numero de cuenta: ')
        balance = 0.00
        return Cliente(nombre,apellido, numero_cuenta, balance)

    def inicio(self):
        opcion = 1
        cliente = self.crear_cliente()
        while opcion != 0:
            print('[0] presione 0 para salir del sistema. ')
            print('[1] presione 1 para depositar en su cuenta. ')
            print('[2] presione 2 para retirar en su cuenta. ')
            opcion = input("Ingrese la opcion: ")
            if opcion == '1':
                dinero = float(input('Ingrese el monto que desea depositar: '))
                if dinero > 0:
                    cliente.depositar(dinero)
                    print(f'Ha depositado {dinero} exitosamente, su saldo es {cliente.balance}')
                else:
                    print("La cantidad de dinero debe ser mayor a cero.")
            if opcion == '2':
                dinero = float(input('Ingrese el monto que desea retirar: '))
                if dinero > 0:
                    cliente.retirar(dinero)
                    print(f'Ha retirado {dinero} exitosamente, su saldo es {cliente.balance}')
                else:
                    print("La cantidad de dinero debe ser mayor a cero.")
            if opcion == '0':
                print("Chao!")
                break

programa = Programa()
programa.inicio()