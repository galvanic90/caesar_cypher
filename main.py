from cifrado import cifrado_cesar

if __name__ == '__main__':
    texto_original = input('Ingrese el texto a cifrar: ')
    clave = 3
    texto_cifrado = cifrado_cesar(texto_original, clave)
    print("Texto original:", texto_original)
    print("Texto cifrado:", texto_cifrado)

