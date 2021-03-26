import socket
import os


print("\n\t\tTaller 4 \nServidor intermedio listado dinamico con hilos\n")

# Direccion y puerto local
host = "localhost"
puerto = 9999

# Creamos los socket
socket1 = socket.socket()
# Establecemos conexion con servidor intermedio
socket1.connect((host, puerto))


def menu():
   print("___________________________________________________")
   print("\t\t*MENU DE OPERACIONES*")
   print("1. SUMA")
   print("2. RESTA")
   print("3. MULTIPLICACION")
   print("4. DIVICION")
   print("5. POTENCIACION")
   print("6. LOGARITMACION")
   print("0. PARA SALIR")


# Funcion que recibe los datos digitados
def digitarNumero():
   x = (input("ingrese el primer numero: "))
   y = (input("Ingrese el segundo numero: "))

   return x, y


# Funcion que conecta con el servidor intermedio
def conexionSerInter(op):
   # Enviamos el socket con los datos de operacion a servidor intermedio
   socket1.send(op.encode("UTF-8"))
   # Recibimos la direccion del servidor suma del servidor intermedio
   dirServidorE = socket1.recv(1024).decode("UTF-8")

   # Convertimos a lista
   listaDir = dirServidorE.split()
   host1 = listaDir[0]
   # Convertimos el puerto a entero
   puerto1 = int(listaDir[1])

   return host1, puerto1


def conexionSerFinal(n1, n2, nh, np):
   # Conectamos con el servidor suma
   socket2 = socket.socket()
   socket2.connect((nh, np))

   listaN = []
   # Agregamos a lista
   listaN.append(n1)
   listaN.append(n2)
   # Convertimos de lista a string
   listaStringN = ' '.join(listaN)

   # Enviamos los 2 valores a operar al servidor suma
   socket2.send(listaStringN.encode("UTF-8"))
   # Recibimos el resultado de la suma del servidor Suma
   res = str(socket2.recv(1024).decode("UTF-8"))

   return res


# Principal
if __name__ == "__main__":

   menu()
   while True:
      opcion = (input("Digite la operacion a realizar: "))

      if opcion == "1":
         # Llamamos la funcion que nos enterga los numeros digitados
         numero1, numero2 = digitarNumero()

         # Llamamos la funcion conexion con Servidor Intermedio
         nuevoHost, nuevoPuerto = conexionSerInter(opcion)
         print("\nLa direccion del servidor suma es: ", nuevoHost, nuevoPuerto)

         # Llamamos la funcion conexion con Servidor Final
         resultadoSuma = conexionSerFinal(numero1, numero2, nuevoHost, nuevoPuerto)
         print("\nNumero 1 = "+ numero1 + ", Numero 2 = " + numero2 + ", Operacion = ", opcion)
         print("\nEl resultado de la suma es =", resultadoSuma)

         print("\n Que tengas un buen dia, si deseas realizar otra operacion ejecute de nuevo el cliente. ")
         break

      elif opcion == "2":
         # Llamamos la funcion que nos enterga los numeros digitados
         numero1, numero2 = digitarNumero()

         # Llamamos la funcion conexion con Servidor Intermedio
         nuevoHost, nuevoPuerto = conexionSerInter(opcion)
         print("\nLa direccion del servidor resta es: ", nuevoHost, nuevoPuerto)

         # Llamamos la funcion conexion con Servidor Final
         resultadoResta = conexionSerFinal(
             numero1, numero2, nuevoHost, nuevoPuerto)
         print("\nNumero 1 = ", numero1, ", Numero 2 = ",
               numero2, ", Operacion = ", opcion)
         print("\nEl resultado de la resta es =", resultadoResta)

         print("\n Que tengas un buen dia, si deseas realizar otra operacion ejecute de nuevo el cliente. ")
         break

      elif opcion == "3":
         # Llamamos la funcion que nos enterga los numeros digitados
         numero1, numero2 = digitarNumero()

         # Llamamos la funcion conexion con Servidor Intermedio
         nuevoHost, nuevoPuerto = conexionSerInter(opcion)
         print("\nLa direccion del servidor multiplicacion es: ", nuevoHost, nuevoPuerto)

         # Llamamos la funcion conexion con Servidor Final
         resultadoMulti = conexionSerFinal(
             numero1, numero2, nuevoHost, nuevoPuerto)
         print("\nNumero 1 = ", numero1, ", Numero 2 = ",
               numero2, ", Operacion = ", opcion)
         print("\nEl resultado de la multiplicacion es =", resultadoMulti)

         print("\n Que tengas un buen dia, si deseas realizar otra operacion ejecute de nuevo el cliente. ")
         break

      elif opcion == "4":
         # Llamamos la funcion que nos enterga los numeros digitados
         numero1, numero2 = digitarNumero()

         # Llamamos la funcion conexion con Servidor Intermedio
         nuevoHost, nuevoPuerto = conexionSerInter(opcion)
         print("\nLa direccion del servidor division es: ", nuevoHost, nuevoPuerto)

         # Llamamos la funcion conexion con Servidor Final
         resultadoDiv = conexionSerFinal(
             numero1, numero2, nuevoHost, nuevoPuerto)
         print("\nNumero 1 = ", numero1, ", Numero 2 = ",
               numero2, ", Operacion = ", opcion)
         print("\nEl resultado de la division es =", resultadoDiv)

         print("\n Que tengas un buen dia, si deseas realizar otra operacion ejecute de nuevo el cliente. ")
         break

      elif opcion == "5":
         # Llamamos la funcion que nos enterga los numeros digitados
         numero1, numero2 = digitarNumero()

         # Llamamos la funcion conexion con Servidor Intermedio
         nuevoHost, nuevoPuerto = conexionSerInter(opcion)
         print("\nLa direccion del servidor potenciacion es: ", nuevoHost, nuevoPuerto)

         # Llamamos la funcion conexion con Servidor Final
         resultadoPot = conexionSerFinal(
             numero1, numero2, nuevoHost, nuevoPuerto)
         print("\nNumero 1 = ", numero1, ", Numero 2 = ",
               numero2, ", Operacion = ", opcion)
         print("\nEl resultado de la potenciacion es =", resultadoPot)

         print("\n Que tengas un buen dia, si deseas realizar otra operacion ejecute de nuevo el cliente. ")
         break 

      elif opcion == "6":
         # Llamamos la funcion que nos enterga los numeros digitados
         numero1, numero2 = digitarNumero()

         # Llamamos la funcion conexion con Servidor Intermedio
         nuevoHost, nuevoPuerto = conexionSerInter(opcion)
         print("\nLa direccion del servidor logaritmo es: ", nuevoHost, nuevoPuerto)

         # Llamamos la funcion conexion con Servidor Final
         resultadoLog = conexionSerFinal(
             numero1, numero2, nuevoHost, nuevoPuerto)
         print("\nNumero 1 = ", numero1, ", Numero 2 = ",
               numero2, ", Operacion = ", opcion)
         print("\nEl resultado del logaritmo es =", resultadoLog)

         print("\n Que tengas un buen dia, si deseas realizar otra operacion ejecute de nuevo el cliente. ")
         break
      else:
         pass
