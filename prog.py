import PIL
from PIL import Image
from tkinter.filedialog import * 
import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.withdraw()

# Auswahl eines zu komprimierenden Bildes mit Pfad in eine Variable
file_path=askopenfilename()

# Öffnen des Bildes in der image Variablen
try:
    image=PIL.Image.open(file_path)
except PIL.UnidentifiedImageError:
    messagebox.showerror("Fehler", "Wähle eine korrekte Bild Datei aus! (.jpg/.png/.webp)")

# Pfad in Extension und Datei-Pfad Variable trennen
file_path, file_extension = os.path.splitext(file_path)

# Bildgröße Höhe und Breite extrahieren in Variablen
myHeight,myWidth=image.size

# # Bildqualität durch Interpolation reduzieren aber Maße beibehalten
image=image.resize((myHeight,myWidth),PIL.Image.NEAREST)

# Neuen Speicherort wählen
# save_path=asksaveasfilename()

# Bild komprimieren
image.convert("RGB").save(file_path + " compressed.jpeg", "JPEG", quality=50)

messagebox.showinfo("Fertig", "Dein Bild wurde erfolgreich komprimiert")
    
