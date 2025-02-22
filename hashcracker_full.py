# HashCracker_Full

# Importar las librerías necesarias
import hashlib
import bcrypt
import scrypt
import tkinter as tk
from tkinter import filedialog, messagebox
from concurrent.futures import ThreadPoolExecutor

# Hash a descifrar como ejemplo un SHA-256 "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
# El diccionario es "diccionario.txt", la ubicacion esta en la carpeta del proyecto

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
