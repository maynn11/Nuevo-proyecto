import sys
import tkinter as tk
from PIL import Image, ImageTk
import os

def mostrar_imagen_y_datos(factura_id, condiciones, cliente, fecha, monto, estado):
    ruta_imagen = os.path.join("imagenes", f"{factura_id}.jpg")
    if not os.path.exists(ruta_imagen):
        print(f"Imagen no encontrada: {ruta_imagen}")
        return

    root = tk.Tk()
    root.title(f"Factura {factura_id}")

    # Mostrar imagen
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((500, 300))
    imagen_tk = ImageTk.PhotoImage(imagen)
    label_img = tk.Label(root, image=imagen_tk)
    label_img.image = imagen_tk
    label_img.pack()

    # Mostrar texto con datos
    texto = (
        f"Condiciones: {condiciones}\n"
        f"Cliente: {cliente}\n"
        f"Fecha: {fecha}\n"
        f"Monto: {monto}\n"
        f"Estado: {estado}"
    )
    label_texto = tk.Label(root, text=texto, justify="left", font=("Arial", 12))
    label_texto.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Uso: python imagen_b.py <numero> <condiciones> <cliente> <fecha> <monto> <estado>")
    else:
        mostrar_imagen_y_datos(*sys.argv[1:])