# Python 3.7
import socketserver
import socket
import threading

host1 = ""
puerto1 = ""
operacion1 = ""

# Clase socket servidor qeu se conecta con el servidor especifico
class miHandler(socketserver.BaseRequestHandler):

	def handle(self):

		# Recibe datos de operacion que se debe realizar y convierte a String
		self.dirSerFinal = str(self.request.recv(1024).decode("UTF-8"))
		print("La direccion es =", self.dirSerFinal)
		# Convertimos a lista
		self.listaDir = self.dirSerFinal.split()
		global operacion1
		operacion1 = self.listaDir[2]

		if operacion1 == 'suma':
			global host1
			host1 = self.listaDir[0]
			global puerto1
			puerto1 = self.listaDir[1]

		elif operacion1 == 'resta':
			global host2
			host2 = self.listaDir[0]
			global puerto2
			puerto2 = self.listaDir[1]
		
		elif operacion1 == 'multiplicacion':
			global host3
			host3 = self.listaDir[0]
			global puerto3
			puerto3 = self.listaDir[1]	

		elif operacion1 == 'division':
			global host4
			host4 = self.listaDir[0]
			global puerto4
			puerto4 = self.listaDir[1]
		
		elif operacion1 == 'potenciacion':
			global host5
			host5 = self.listaDir[0]
			global puerto5
			puerto5 = self.listaDir[1]
		
		elif operacion1 == 'logaritmacion':
			global host6
			host6 = self.listaDir[0]
			global puerto6
			puerto6 = self.listaDir[1]
				
			

#Creando hilo para servidor
class serverThread2(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		print("\n\t\tTaller 4 \nServidor intermedio listado dinamico con hilos\n")
		print("\n\t Servidor intermedio escuchando...\n")
		print("Conexion establecida con servidor especifico...")
		host2 = "localhost"
		lspuerto2 = [9998, 9996, 9994, 9992, 9990, 9988]
		# Llamamos la clase socket servidor con los parametros de direccion y puerto
		server1 = socketserver.TCPServer((host2, lspuerto2[0]), miHandler)
		# Mantenemos al servidor en estado de escucha
		server1.handle_request()
		server2 = socketserver.TCPServer((host2, lspuerto2[1]), miHandler)
		server2.handle_request()
		server3 = socketserver.TCPServer((host2, lspuerto2[2]), miHandler)
		server3.handle_request()
		server4 = socketserver.TCPServer((host2, lspuerto2[3]), miHandler)
		server4.handle_request()
		server5 = socketserver.TCPServer((host2, lspuerto2[4]), miHandler)
		server5.handle_request()
		server6 = socketserver.TCPServer((host2, lspuerto2[5]), miHandler)
		server6.handle_request()
		


# # Clase socket servidor
class myHandler(socketserver.BaseRequestHandler):

	def handle(self):
		self.operacion = str(self.request.recv(1024).decode("UTF-8"))

		if self.operacion == '1':
			self.listaDir = []
			# Agregamos a lista
			self.listaDir.append(host1)
			self.listaDir.append(puerto1)
			# Convertimos de lista a string
			self.listaStringDir = ' '.join(self.listaDir)

			# Enviamos respuesta de datos de direccion al cliente
			self.request.send(self.listaStringDir.encode("UTF-8"))

		elif self.operacion == '2':
			self.listaDir1 = []
			# Agregamos a lista
			self.listaDir1.append(host2)
			self.listaDir1.append(puerto2)
			# Convertimos de lista a string
			self.listaStringDir1 = ' '.join(self.listaDir1)

			# Enviamos respuesta de datos de direccion al cliente
			self.request.send(self.listaStringDir1.encode("UTF-8"))

		elif self.operacion == '3':
			self.listaDir2 = []
			# Agregamos a lista
			self.listaDir2.append(host3)
			self.listaDir2.append(puerto3)
			# Convertimos de lista a string
			self.listaStringDir2 = ' '.join(self.listaDir2)

			# Enviamos respuesta de datos de direccion al cliente
			self.request.send(self.listaStringDir2.encode("UTF-8"))

		elif self.operacion == '4':
			self.listaDir3 = []
			# Agregamos a lista
			self.listaDir3.append(host4)
			self.listaDir3.append(puerto4)
			# Convertimos de lista a string
			self.listaStringDir3 = ' '.join(self.listaDir3)

			# Enviamos respuesta de datos de direccion al cliente
			self.request.send(self.listaStringDir3.encode("UTF-8"))	

		elif self.operacion == '5':
			self.listaDir4 = []
			# Agregamos a lista
			self.listaDir4.append(host5)
			self.listaDir4.append(puerto5)
			# Convertimos de lista a string
			self.listaStringDir4 = ' '.join(self.listaDir4)

			# Enviamos respuesta de datos de direccion al cliente
			self.request.send(self.listaStringDir4.encode("UTF-8"))	

		elif self.operacion == '6':
			self.listaDir5 = []
			# Agregamos a lista
			self.listaDir5.append(host6)
			self.listaDir5.append(puerto6)
			# Convertimos de lista a string
			self.listaStringDir5 = ' '.join(self.listaDir5)

			# Enviamos respuesta de datos de direccion al cliente
			self.request.send(self.listaStringDir5.encode("UTF-8"))	


		else:
			pass

# # Creando hilo para Clientes
class serverThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		# Direccion comunicacion cliente
		host7 = "localhost"
		puerto7 = 9999

		# Llamamos la clase socket servidor con los parametros de direccion y puerto
		serverCli = socketserver.TCPServer((host7, puerto7), myHandler)
		print("Conexion establecida con cliente")

		# Mantenemos al servidor en estado de escucha
		serverCli.serve_forever()


hiloServerEspecifico = serverThread2()
hiloServerEspecifico.start()
hiloServerCliente = serverThread()
hiloServerCliente.start()
# # hiloServerCliente.daemon = True
# # hiloServerCliente.join()
