import socket
from cifrado import cifrado_cesar

texto_original = input('Ingrese el texto a cifrar: ')
clave = 4
texto_cifrado = cifrado_cesar(texto_original, clave)
print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)

# El cliente debe tener las mismas especificaciones del servidor
host = socket.gethostname()
port = 3000
BUFFER_SIZE = 1024
MESSAGE = texto_cifrado # Datos que queremos enviar

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.connect((host, port))
    # Convertimos str a bytes
    socket_tcp.send(MESSAGE.encode('utf-8'))
    data = socket_tcp.recv(BUFFER_SIZE)