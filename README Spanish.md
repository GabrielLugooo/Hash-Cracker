<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# Cracker de Hashes

<a href="https://github.com/GabrielLugooo/Hash-Cracker/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Cracker%20Hash%20Español-000000" alt="Cracker Español" /></a>
<a href="https://github.com/GabrielLugooo/Hash-Cracker" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Cracker%20Hash%20Inglés-green" alt="Cracker Inglés" /></a>

### Objetivos

El proyecto HashCracker tiene como objetivo permitir el descifrado de hashes utilizando un diccionario de contraseñas. El usuario puede cargar un archivo de diccionario y realizar "ataques" paralelos para encontrar la contraseña correspondiente al hash proporcionado.

El propósito de este proyecto es ayudar a comprender cómo se pueden utilizar técnicas de fuerza bruta y diccionarios de contraseñas comunes para descifrar contraseñas cifradas.

Además, proporciona una base para experimentar con algoritmos de hash populares como SHA-256, MD5, SHA-1, bcrypt y scrypt, demostrando cómo pueden ser vulnerables a ataques cuando no se implementan las medidas de seguridad adecuadas.

A través de este proyecto, el objetivo es mejorar la comprensión de la seguridad en criptografía, mostrando la debilidad de los métodos de cifrado cuando se utilizan contraseñas simples o predecibles.

También sirve como una introducción práctica al trabajo con archivos de texto y al manejo de diccionarios grandes en proyectos de piratería ética y ciberseguridad.

### Habilidades Aprendidas

- Trabajo con algoritmos hash: Implementación de técnicas para trabajar con algoritmos hash como SHA-256, MD5, SHA-1, bcrypt y scrypt
- Manipulación de archivos en Python: Carga de diccionarios y gestión de combinaciones hash utilizando Python.
- Optimización del rendimiento: Mejora del rendimiento al procesar archivos de texto grandes y manejo eficiente de diccionarios extensos.
- Ciberseguridad y hacking ético: Entender cómo los sistemas de seguridad pueden ser vulnerables a ataques de diccionario y fuerza bruta.
- Principios de criptografía: Aplicación de conocimientos de criptografía para entender la protección de contraseñas y sus debilidades.
- Uso de librerías como `hashlib`, `bcrypt` y `scrypt` para trabajar con algoritmos hash.
- Implementación de ataques de diccionario en paralelo utilizando `ThreadPoolExecutor`.
- Creación de interfaces gráficas de usuario con `tkinter` para interacción del usuario.
- Integración de mensajes de alerta y resultados con `messagebox`.

### Herramientas Usadas

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)

- Python: el lenguaje principal utilizado para desarrollar el script de descifrado.
- Diccionarios de contraseñas: archivos .txt utilizados para intentar hacer coincidir las contraseñas con los hashes.
- Algoritmos de hash: algoritmos de hash como MD5, SHA1 y SHA256, utilizados para el cifrado de contraseñas.
- Bibliotecas: `hashlib`, `bcrypt`, `scrypt`, `tkinter`, `concurrent.futures`.

### Proyecto

#### Hash Cracker Full Vista Previa

<img align="center" src="https://i.imgur.com/6qRwOtq.jpeg" alt="HashCracker_Full" />

#### HashCracker_Full Código con Comentarios (Español)

```python
# HashCracker
# Importar las librerías necesarias
import hashlib
import bcrypt
import scrypt
import tkinter as tk
from tkinter import filedialog, messagebox
from concurrent.futures import ThreadPoolExecutor

# Hash a descifrar como ejemplo un SHA-256 "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
# la libreria es diccionario.txt, la ubicacion esta en la carpeta del proyecto

# Función para abrir el diálogo de selección de archivo
def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Seleccionar archivo de diccionario")
    return file_path

# Función para leer el diccionario desde el archivo seleccionado
def read_dictionary(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file]

# Función para verificar si la contraseña coincide con el hash utilizando el algoritmo especificado
def check_hash(password, hash_to_crack, algorithm):
    if algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest() == hash_to_crack
    elif algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest() == hash_to_crack
    elif algorithm == "sha1":
        return hashlib.sha1(password.encode()).hexdigest() == hash_to_crack
    elif algorithm == "bcrypt":
        return bcrypt.checkpw(password.encode(), hash_to_crack.encode())
    elif algorithm == "scrypt":
        salt = b"saltsalt"
        return scrypt.hash(password.encode(), salt, 16384, 8, 1, 32).hex() == hash_to_crack
    return False

# Función para realizar el ataque de descifrado en paralelo utilizando un ThreadPoolExecutor
def crack_hash_parallel(hash_to_crack, dictionary, algorithm, result_text):
    with ThreadPoolExecutor() as executor:
        result = executor.map(lambda word: (word, check_hash(word, hash_to_crack, algorithm)), dictionary)

        for word, is_match in result:
            result_text.insert(tk.END, f"Probando: {word}\n")
            if is_match:
                messagebox.showinfo("Contraseña encontrada", f"La contraseña original es: {word}")
                return
    messagebox.showinfo("Resultado", "No se encontró ninguna coincidencia.")

# Función para iniciar el ataque
def start_attack():
    hash_to_crack = hash_entry.get()
    algorithm = algo_var.get()
    if not hash_to_crack or not dictionary:
        messagebox.showerror("Error", "Por favor ingrese un hash y seleccione un diccionario.")
        return

    result_text.delete(1.0, tk.END)
    crack_hash_parallel(hash_to_crack, dictionary, algorithm, result_text)

# Función para seleccionar el diccionario a usar
def select_dictionary():
    global dictionary
    file_path = open_file_dialog()
    if file_path:
        dictionary = read_dictionary(file_path)
        dic_label.config(text=f"Diccionario cargado: {file_path}")

# Inicialización de la interfaz gráfica
dictionary = []
root = tk.Tk()
root.title("HashCracker")
root.geometry("500x400")

# Elementos de la interfaz
tk.Label(root, text="Ingrese el hash a descifrar:").pack()
hash_entry = tk.Entry(root, width=50)
hash_entry.pack()

tk.Label(root, text="Seleccione el algoritmo de hash:").pack()
algo_var = tk.StringVar(value="sha256")
algo_menu = tk.OptionMenu(root, algo_var, "sha256", "md5", "sha1", "bcrypt", "scrypt")
algo_menu.pack()

dic_label = tk.Label(root, text="No se ha seleccionado un diccionario")
dic_label.pack()

tk.Button(root, text="Seleccionar Diccionario", command=select_dictionary).pack()
tk.Button(root, text="Iniciar Ataque", command=start_attack).pack()

result_text = tk.Text(root, height=10, width=50)
result_text.pack()

root.mainloop()
```

### Limitaciones

HashCracker_Full es solo para fines educativos bajo la licencia MIT.
El código de la versión HashCracker_Lite también está disponible en el repositorio.

---

<h3 align="left">Conecta Conmigo</h3>

<p align="left">
<a href="https://www.youtube.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=55200&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="http://www.tiktok.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=118638&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="https://instagram.com/lugooogabriel" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=32309&format=png" alt="lugooogabriel" height="40" width="40" /></a>
<a href="https://twitter.com/gabriellugo__" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=phOKFKYpe00C&format=png" alt="gabriellugo__" height="40" width="40" /></a>
<a href="https://www.linkedin.com/in/hernando-gabriel-lugo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=8808&format=png" alt="hernando-gabriel-lugo" height="40" width="40" /></a>
<a href="https://github.com/GabrielLugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=80&id=AngkmzgE6d3E&format=png" alt="gabriellugooo" height="34" width="34" /></a>
<a href="mailto:lugohernandogabriel@gmail.com"> <img align="center" src="https://img.icons8.com/?size=50&id=38036&format=png" alt="lugohernandogabriel@gmail.com" height="40" width="40" /></a>
<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://simpleicons.org/icons/linktree.svg" alt="gabriellugooo" height="40" width="40" /></a>
</p>

<p align="left">
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Español-000000" alt="Versión Español" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Inglés-Green" alt="Versión Inglés" /></a>

</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Créditos-Gabriel%20Lugo-green" alt="Créditos" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Vistas%20del%20Perfil&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
