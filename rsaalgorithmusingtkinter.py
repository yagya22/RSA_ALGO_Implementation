import tkinter as tk
from tkinter import messagebox
import math

def prime(pr):
    j = int(math.sqrt(pr))
    for i in range(2, j + 1):
        if pr % i == 0:
            return False
    return True

def ce(p, q, t):
    e_values = []
    for i in range(2, t):
        if t % i != 0 and prime(i) and i != p and i != q:
            e_values.append(i)
    return e_values

def cd(x, t):
    k = 1
    while True:
        k += t
        if k % x == 0:
            return k // x

def encrypt_decrypt(e, d, n, message):
    encrypted = [(ord(char) ** e) % n for char in message]
    decrypted = [chr((char ** d) % n) for char in encrypted]
    return ''.join(chr(char) for char in encrypted), ''.join(decrypted)

def calculate():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        message = entry_message.get()

        if not prime(p) or not prime(q) or p == q:
            messagebox.showerror("Error", "Please enter valid prime numbers.")
            return

        n = p * q
        t = (p - 1) * (q - 1)
        e_values = ce(p, q, t)
        d_values = [cd(e, t) for e in e_values]

        e, d = e_values[0], d_values[0]
        encrypted, decrypted = encrypt_decrypt(e, d, n, message)

        label_e.config(text=f"Possible values of e: {', '.join(map(str, e_values))}")
        label_d.config(text=f"Possible values of d: {', '.join(map(str, d_values))}")
        label_encrypted.config(text=f"Encrypted Message: {encrypted}")
        label_decrypted.config(text=f"Decrypted Message: {decrypted}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for p and q.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("RSA Encryption and Decryption")
root.geometry("600x500")

frame = tk.Frame(root)
frame.pack(pady=20)

label_p = tk.Label(frame, text="Enter First Prime Number:", font=("Arial", 12))
label_p.grid(row=0, column=0, padx=10, pady=5)
entry_p = tk.Entry(frame, font=("Arial", 12))
entry_p.grid(row=0, column=1, padx=10, pady=5)

label_q = tk.Label(frame, text="Enter Second Prime Number:", font=("Arial", 12))
label_q.grid(row=1, column=0, padx=10, pady=5)
entry_q = tk.Entry(frame, font=("Arial", 12))
entry_q.grid(row=1, column=1, padx=10, pady=5)

label_message = tk.Label(frame, text="Enter Message:", font=("Arial", 12))
label_message.grid(row=2, column=0, padx=10, pady=5)
entry_message = tk.Entry(frame, font=("Arial", 12))
entry_message.grid(row=2, column=1, padx=10, pady=5)

button_calculate = tk.Button(frame, text="Click To Calculate ", command=calculate, font=("Arial", 12))
button_calculate.grid(row=3, columnspan=2, pady=10)

label_e = tk.Label(frame, text="Possible values of e:", font=("Arial", 12), wraplength=500, justify=tk.LEFT)
label_e.grid(row=4, columnspan=2, padx=10, pady=5, sticky=tk.W)

label_d = tk.Label(frame, text="Possible values of d:", font=("Arial", 12), wraplength=500, justify=tk.LEFT)
label_d.grid(row=5, columnspan=2, padx=10, pady=5, sticky=tk.W)

label_encrypted = tk.Label(frame, text="Encrypted Message:", font=("Arial", 12), wraplength=500, justify=tk.LEFT)
label_encrypted.grid(row=6, columnspan=2, padx=10, pady=5, sticky=tk.W)

label_decrypted = tk.Label(frame, text="Decrypted Message:", font=("Arial", 12), wraplength=500, justify=tk.LEFT)
label_decrypted.grid(row=7, columnspan=2, padx=10, pady=5, sticky=tk.W)

root.mainloop()
