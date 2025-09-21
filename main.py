num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
oper = input("Operación (+, -, *, /): ")
if oper == '+':
 result = num1 + num2
elif oper == '-':
 result = num1 - num2
elif oper == '*':
 result = num1 * num2
elif oper == '/':
 result = num1 / num2
else:
 result = "Inválida"
print(f"Resultado: {result}")




def suma(a, b):
 return a + b
def resta(a, b):
 return a - b
def multiplicacion(a, b):
 return a * b
def division(a, b):
 return a/b


# Menú interactivo
def   calculadora():
 print("  CALCULADORA PYTHON de Leonardo")
print("1. Sumar")
print("2.resta")
print("3.Multiplicacion")
print("4.division") 
print("5.salir del programa")
def main():
 while True:
  calculadora()

try:
  opcion = int(input("Ingresa un número entero: "))
 
  num1 =int(input("ingrse el primer numero:"))
  num2 =int(input("ingrse el segundo numero:"))

  match opcion:
    case 1:
      resultado = suma(num1,num2)

    case 2:
     resultado = resta(num1,num2)
    case 3:
     resultado = multiplicacion(num1,num2)
    case 4:
     resultado = division(num1,num2)
    case 5:
         print("saliendo del programa")
    break
    
    case _:
        print("La operacion ingresada no es existe ")

except ValueError:
  print("Error el valor no es valido.")
 
except ZeroDivisionError:
   print("no se puede dividir por cero")

else:
  print("el resulatdo es:{resultado}")

main() 

 