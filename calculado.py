class Calculadora:
    def __init__(self):
        self.resultado = 0

    def sumar(self, a, b):
        self.resultado = a + b
        return self.resultado

    def restar(self, a, b):
        self.resultado = a - b
        return self.resultado

    def multiplicar(self, a, b):
        self.resultado = a * b
        return self.resultado

    def dividir(self, a, b):
        if b == 0:
            return "Error: división entre cero"
        self.resultado = a / b
        return self.resultado

# Crear una instancia de la calculadora
calc = Calculadora()

# Menú de operaciones
print("Calculadora Básica POO")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Selecciona una opción (1-4): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == "1":
    print("Resultado:", calc.sumar(num1, num2))
elif opcion == "2":
    print("Resultado:", calc.restar(num1, num2))
elif opcion == "3":
    print("Resultado:", calc.multiplicar(num1, num2))
elif opcion == "4":
    print("Resultado:", calc.dividir(num1, num2))
else:
    print("Opción inválida")
    #Para evitar que se cierre al hacer doble clic

input("presionar enter para salir")