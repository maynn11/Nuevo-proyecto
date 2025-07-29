import tkinter as tk
from tkinter import messagebox
import csv
import os
import subprocess
from PIL import Image, ImageDraw

# Función para guardar los datos de la factura
def guardar_factura():
    numero = entry_numero.get().strip()
    condiciones = entry_condiciones.get().strip()
    cliente = entry_cliente.get().strip()
    fecha = entry_fecha.get().strip()
    monto = entry_monto.get().strip()
    estado = entry_estado.get().strip()

    if not (numero and condiciones and cliente and fecha and monto and estado):
        messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
        return

    # Guardar en CSV
    with open("facturas.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([numero, condiciones, cliente, fecha, monto, estado])

    # Crear imagen 
    crear_imagen_factura(numero, condiciones, cliente, fecha, monto, estado)

    # Esperar un poco o hasta que la imagen exista para evitar mensaje falso
    import time
    ruta_imagen = os.path.join("imagenes", f"{numero}.jpg")
    for _ in range(10):  # hasta 10 intentos con 0.1 seg de espera cada uno
        if os.path.exists(ruta_imagen):
            break
        time.sleep(0.1)
    else:
        print("⚠️ La imagen no se encontró tras esperar")

    # visulizar imagen desde aplicacion b 
    subprocess.Popen(['python', 'imagen_b.py', numero, condiciones, cliente, fecha, monto, estado])

    # campos
    entry_numero.delete(0, tk.END)
    entry_condiciones.delete(0, tk.END)
    entry_cliente.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)
    entry_monto.delete(0, tk.END)
    entry_estado.delete(0, tk.END)

    messagebox.showinfo("Éxito", "Factura registrada y enviada a visualización.")

# funcion de la imagen 
def crear_imagen_factura(numero, condiciones, cliente, fecha, monto, estado):
    if not os.path.exists("imagenes"):
        os.makedirs("imagenes")

    ruta = os.path.join("imagenes", f"{numero}.jpg")

    # Crear imagen blanca
    img = Image.new('RGB', (600, 400), color='white')
    draw = ImageDraw.Draw(img)

    # Dibujar los datos en la imagen
    texto = [
        f"Factura No.: {numero}",
        f"Condiciones: {condiciones}",
        f"Cliente ID: {cliente}",
        f"Fecha: {fecha}",
        f"Monto: {monto}",
        f"Estado: {estado}"
    ]

    y = 50
    for linea in texto:
        draw.text((50, y), linea, fill=(0, 0, 0))
        y += 40  # espacio entre líneas

    img.save(ruta)
    print(f"Imagen guardada en: {ruta}")

# Crear la interfaz
root = tk.Tk()
root.title("Registro de Facturas")

tk.Label(root, text="Número de Factura").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Condiciones").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="ID del Cliente").grid(row=2, column=0, padx=5, pady=5)
tk.Label(root, text="Fecha de Factura").grid(row=3, column=0, padx=5, pady=5)
tk.Label(root, text="Monto").grid(row=4, column=0, padx=5, pady=5)
tk.Label(root, text="Estado").grid(row=5, column=0, padx=5, pady=5)

entry_numero = tk.Entry(root)
entry_condiciones = tk.Entry(root)
entry_cliente = tk.Entry(root)
entry_fecha = tk.Entry(root)
entry_monto = tk.Entry(root)
entry_estado = tk.Entry(root)

entry_numero.grid(row=0, column=1, padx=5, pady=5)
entry_condiciones.grid(row=1, column=1, padx=5, pady=5)
entry_cliente.grid(row=2, column=1, padx=5, pady=5)
entry_fecha.grid(row=3, column=1, padx=5, pady=5)
entry_monto.grid(row=4, column=1, padx=5, pady=5)
entry_estado.grid(row=5, column=1, padx=5, pady=5)

tk.Button(root, text="Guardar Factura", command=guardar_factura).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()