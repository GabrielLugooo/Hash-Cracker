<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1749686400&v=beta&t=hBmszzzG0Zu-m7ZxeCdU5VxgDWqIZuWB0vnrMycuqY4" alt="gabriellugo" />

# HASH CRACKER

<a href="https://github.com/GabrielLugooo/Hash-Cracker" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Hash%20Cracker-000000" alt="English Cracker" /></a>
<a href="https://github.com/GabrielLugooo/Hash-Cracker/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Hash%20Cracker-green" alt="Spanish Cracker" /></a>

### Objective

The HashCracker project aims to allow the decryption of hashes using a password dictionary. The user can load a dictionary file and perform parallel "attacks" to find the password corresponding to the provided hash.

The purpose of this project is to help understand how brute-force and common password dictionary techniques can be used to decipher encrypted passwords.

Additionally, it provides a foundation for experimenting with popular hash algorithms such as SHA-256, MD5, SHA-1, bcrypt and scrypt, demonstrating how they can be vulnerable to attacks when proper security measures are not implemented.

Through this project, the goal is to improve understanding of security in cryptography, showing the weakness of encryption methods when simple or predictable passwords are used.

It also serves as a practical introduction to working with text files and handling large dictionaries in ethical hacking and cybersecurity projects.

### Skills Learned

- Working with hash algorithms: Implementing techniques to work with hash algorithms such as SHA-256, MD5, SHA-1, bcrypt and scrypt
- File manipulation in Python: Loading dictionaries and managing hash combinations using Python.
- Performance optimization: Improving performance when processing large text files and efficiently handling extensive dictionaries.
- Cybersecurity and ethical hacking: Understanding how security systems can be vulnerable to dictionary and brute force attacks.
- Cryptography principles: Applying knowledge of cryptography to understand password protection and weaknesses.
- Use of libraries such as `hashlib`, `bcrypt`, and `scrypt` to work with hashing algorithms.
- Implementation of dictionary attacks in parallel using `ThreadPoolExecutor`.
- Creation of graphical user interfaces with `tkinter` for user interaction.
- Integration of alert messages and results with `messagebox`.

### Tools Used

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Bash%20CMD-000000?logo=bashcmd&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Thread%20Pool%20Excecutor-000000?logo=threadpool&logoSize=auto)
![Static Badge](https://img.shields.io/badge/concurrent%20futures-000000?logo=concurrent.futures&logoSize=auto)

![Static Badge](https://img.shields.io/badge/hashlib-000000?logo=hashlib&logoSize=auto)
![Static Badge](https://img.shields.io/badge/bcrypt-000000?logo=bcrypt&logoSize=auto)
![Static Badge](https://img.shields.io/badge/scrypt-000000?logo=scrypt&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Tkinter-000000?logo=tkinter&logoSize=auto)
![Static Badge](https://img.shields.io/badge/MessageBox-000000?logo=messagebox&logoSize=auto)

- Python: The main language used to develop the cracking script.
- Password Dictionaries: .txt files used to try matching passwords with hashes.
- Hashing Algorithms: Hash algorithms such as MD5, SHA1, and SHA256, used for password encryption.
- Libraries: `hashlib`, `bcrypt`, `scrypt`, `tkinter`, `concurrent.futures`.

### Project

#### Hash Cracker Full Preview

<img align="center" src="https://i.imgur.com/6qRwOtq.jpeg" alt="HashCracker_Full" />

#### HashCracker_Full Code with Comments (English)

```python
# HashCracker
# Import necessary libraries
import hashlib
import bcrypt
import scrypt
import tkinter as tk
from tkinter import filedialog, messagebox
from concurrent.futures import ThreadPoolExecutor

# Hash to crack as an example a SHA-256 "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
# The library is dictionary.txt, its location is in the project folder

# Function to open the file selection dialog
def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select dictionary file")
    return file_path

# Function to read the dictionary from the selected file
def read_dictionary(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file]

# Function to check if the password matches the hash using the specified algorithm
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

# Function to perform the decryption attack in parallel using a ThreadPoolExecutor
def crack_hash_parallel(hash_to_crack, dictionary, algorithm, result_text):
    with ThreadPoolExecutor() as executor:
        result = executor.map(lambda word: (word, check_hash(word, hash_to_crack, algorithm)), dictionary)

        for word, is_match in result:
            result_text.insert(tk.END, f"Trying: {word}\n")
            if is_match:
                messagebox.showinfo("Password Found", f"The original password is: {word}")
                return
    messagebox.showinfo("Result", "No matches found.")

# Function to start the attack
def start_attack():
    hash_to_crack = hash_entry.get()
    algorithm = algo_var.get()
    if not hash_to_crack or not dictionary:
        messagebox.showerror("Error", "Please enter a hash and select a dictionary.")
        return

    result_text.delete(1.0, tk.END)
    crack_hash_parallel(hash_to_crack, dictionary, algorithm, result_text)

# Function to select the dictionary to use
def select_dictionary():
    global dictionary
    file_path = open_file_dialog()
    if file_path:
        dictionary = read_dictionary(file_path)
        dic_label.config(text=f"Loaded dictionary: {file_path}")

# Initialize the graphical interface
dictionary = []
root = tk.Tk()
root.title("HashCracker")
root.geometry("500x400")

# Interface elements
tk.Label(root, text="Enter the hash to crack:").pack()
hash_entry = tk.Entry(root, width=50)
hash_entry.pack()

tk.Label(root, text="Select the hash algorithm:").pack()
algo_var = tk.StringVar(value="sha256")
algo_menu = tk.OptionMenu(root, algo_var, "sha256", "md5", "sha1", "bcrypt", "scrypt")
algo_menu.pack()

dic_label = tk.Label(root, text="No dictionary selected")
dic_label.pack()

tk.Button(root, text="Select Dictionary", command=select_dictionary).pack()
tk.Button(root, text="Start Attack", command=start_attack).pack()

result_text = tk.Text(root, height=10, width=50)
result_text.pack()

root.mainloop()
```

### Limitations

HashCracker_Full it's just for educational purpose under the MIT License.
HashCracker_Lite version´s code available on the repo too.

---

<h3 align="left">Connect with me</h3>

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
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Version-000000" alt="English Version" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Version-Green" alt="Spanish Version" /></a>
</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Credits-Gabriel%20Lugo-green" alt="Credits" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Profile%20views&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
