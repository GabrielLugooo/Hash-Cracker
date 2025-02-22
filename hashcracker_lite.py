
# HashCracker_Lite

# Importar las librerías necesarias
import hashlib

# Definir el hash a descifrar (en este caso, un hash SHA-256)
hash_file = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"

# El diccionario es "diccionario.txt", la ubicacion esta en la carpeta del proyecto

# Solicitar al usuario la dirección del archivo del diccionario
dic_file = input("Ingrese la dirección del archivo del diccionario: ")

# Abrir el archivo del diccionario en modo lectura
with open(dic_file, 'r') as file:
    # Leer todas las líneas del archivo y eliminamos saltos de línea
    diccionario = [line.strip() for line in file]

    # Iterar sobre cada palabra del diccionario
    for password in diccionario: 
        # Calcular el hash SHA-256 de la palabra
        hash_calculado = hashlib.sha256(password.encode()).hexdigest()

        # Verificar si el hash calculado coincide con el hash dado
        if hash_calculado == hash_file:
            print("La contraseña original es: " + password)
            break  # Si encontramos la contraseña, salir del bucle
        else:
            print("La contraseña NO es: " + password)  # Si no coinciden, mostrar mensaje

