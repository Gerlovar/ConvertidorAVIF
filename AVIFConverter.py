import customtkinter as CTK
import pillow_avif
import os
import threading
from tkinter import filedialog
from PIL import Image


def button_callback():
    file_names = filedialog.askopenfilenames(
        title='Seleccionar archivos', 
        filetypes=(('Multimedia', '*.png *.jpg'), )
    )
    files = len(file_names)
    if file_names:
        the_label.configure(text="Convirtiendo...")
        proceso_thread = threading.Thread(target=convert, args=(file_names, files))
        proceso_thread.start()
    else:
        print("")

def convert(file_names, files):
    for img in file_names:
            try:
                img_name = os.path.basename(img)
                Image.open(img).save(".\ImagenesAVIF\\" + img_name[:-4] + ".avif")                
            except:
                files -= 1
    the_text = 'Conversion exitosa, se convirtieron ' + str(files) + ' archivos'
    the_label.configure(text=the_text)

app = CTK.CTk(fg_color='#222e35')
app.title("Converter")
app.geometry("450x200+200+5")

app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=1)
app.columnconfigure(0, weight=1)

button = CTK.CTkButton(app, text="Seleccionar archivos", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

the_label = CTK.CTkLabel(app, text="", text_color='white', font=('', 18))
the_label.grid(row=1, column=0, padx=20, pady=20)

app.mainloop()