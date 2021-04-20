import socket as sk

host = "localhost"
port = 6000

sCliente =  sk.socket()
sCliente.connect((host, port))
print("Conectado - Escribir 'Salir' para desconectarse.")

while True: 
    inp = input("Texto para enviar: ")
    print("Enviar:", inp)
    salida = inp.encode("UTF8")
    print("Salida antes de enviar:", salida.decode("utf8"))
    lene = sCliente.send(salida)  
    #print("Se han enviado: {} bytes al servidor.".format(lene))   
    ins = sCliente.recv(512)
    insd = ins.decode("UTF8")
    print("Servidor retorna:", insd)
    if inp == "salir":
        break

sCliente.close()
print("Terminado")
