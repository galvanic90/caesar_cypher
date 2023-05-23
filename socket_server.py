import socket
import config

from cifrado import descifrado_cesar
#host = socket.gethostname() # Esta función nos da el nombre de la máquina
# Usamos un número pequeño para tener una respuesta rápida 

host = config.HOST
port = config.PORT
BUFFER_SIZE = config.BUFFER_SIZE

'''Los objetos socket soportan el context manager type
así que podemos usarlo con una sentencia with, no hay necesidad
de llamar a socket_close()
'''
# Creamos un objeto socket tipo TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:

    socket_tcp.bind((host, port)) 
    socket_tcp.listen(5) # Esperamos la conexión del cliente 
    conn, addr = socket_tcp.accept() # Establecemos la conexión con el cliente 
    print(host)
    with conn:
        print('[*] Conexión establecida') 
        while True:
            # Recibimos bytes, convertimos en str
            data = conn.recv(BUFFER_SIZE)
            # Verificamos que hemos recibido datos
            if not data:
                break
            else:
                msg = data.decode('utf-8')
                print('[*] Datos recibidos: {}'.format(msg))
                descifrado_msg = descifrado_cesar(msg, config.CLAVE)
                print('[*] Mensaje descifrado: {}'.format(descifrado_msg))
            conn.send(data) # Hacemos echo convirtiendo de nuevo a bytes

