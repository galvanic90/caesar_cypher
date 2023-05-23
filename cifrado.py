def cifrado_cesar(texto, clave):
    resultado = ''
    for caracter in texto:
        if caracter.isalpha():
            # Obtener el código ASCII del caracter y calcular la clave
            codigo = ord(caracter)
            codigo_desplazado = (codigo - ord('a') + clave) % 26 + ord('a')
            # Convertir el código desplazado de vuelta a caracter
            caracter_desplazado = chr(codigo_desplazado)
            resultado += caracter_desplazado
        else:
            resultado += caracter
    return resultado


def descifrado_cesar(texto_cifrado, clave):
    resultado = ''
    for caracter in texto_cifrado:
        if caracter.isalpha():
            # Obtener el código ASCII del caracter y calcular la clave inverso
            codigo = ord(caracter)
            codigo_desplazado = (codigo - ord('a') - clave) % 26 + ord('a')
            # Convertir el código desplazado inverso de vuelta a caracter
            caracter_desplazado = chr(codigo_desplazado)
            resultado += caracter_desplazado
        else:
            resultado += caracter
    return resultado


