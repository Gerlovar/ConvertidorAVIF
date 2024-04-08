import customtkinter as CTK
import pillow_avif
import os
import threading
from tkinter import filedialog
from PIL import Image, ImageTk

def file_funct():
    file_names = filedialog.askopenfilenames(
        title='Seleccionar archivos', 
        filetypes=(('Multimedia', '*.png *.jpg'), )
    )
    if file_names:
        files = len(file_names)    
        aviso_text = "se convertira " + str(files) + " archivos"
        aviso.configure(text=aviso_text)
        button_iniciar.grid(row=2, column=1, padx=20)
        button_iniciar.configure(command=lambda: iniciar(file_names))

def direct_funct():
    archivos = []
    directorio = filedialog.askdirectory(title="Seleccionar carpeta")
    if directorio:
        for ruta, _, archivos_ruta in os.walk(directorio):
            for archivo in archivos_ruta:
                if archivo.endswith(('.jpg', '.png')):
                    archivos.append(os.path.join(ruta, archivo))

        aviso_text = "se convertira " + str(len(archivos)) + " archivos de la carpeta"
        aviso.configure(text=aviso_text)
        button_iniciar.grid(row=2, column=1, padx=20)
        button_iniciar.configure(command=lambda: iniciar(archivos))     

def iniciar(file_names):
    Guardar_en = filedialog.askdirectory(title="Guardar en:")
    print(Guardar_en)
    proceso_thread = threading.Thread(target=convert, args=(file_names, Guardar_en))
    proceso_thread.start()

def convert(file_names, Guardar_en):
    pct = 100/len(file_names)
    jsjs = 0
    the_label.configure(text=("Proceso: " + str(jsjs) + "%"))
    for img in file_names:
            try:
                img_name = os.path.basename(img)#*Obtiene el nombre de archivo sin la ruta (img es una ruta)
                Image.open(img).save(Guardar_en + "/" + img_name[:-4] + ".avif")
                jsjs += pct
            except:
                print("Something went wrong")
            the_label.configure(text=("Proceso: " + str(f"{jsjs:.2f}") + "%"))
    the_text = 'Conversion exitosa, se convirtieron ' + str(len(file_names)) + ' archivos'
    the_label.configure(text=the_text)

app = CTK.CTk(fg_color='#222e35')
app.title("Converter")
app.geometry("450x450+200+5")
app.iconbitmap(default="E:\\PROGRAMACION\\pythonxD\\ConvertidorAVIF\\AvifConverterIcon.ico")

app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=1)
app.rowconfigure(2, weight=1)
app.rowconfigure(3, weight=1)
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

welcome = CTK.CTkLabel(app, text="Bienvenido", text_color='white', font=('', 18))
welcome.grid(row=0, columnspan=2, padx=20)

button_file = CTK.CTkButton(app, text="Seleccionar archivos", command=file_funct)
button_file.grid(row=1, column=0, padx=20)
button_file = CTK.CTkButton(app, text="Seleccionar carpeta", command=direct_funct)
button_file.grid(row=1, column=1, padx=20)

aviso = CTK.CTkLabel(app, text="", text_color='white', font=('', 18), wraplength=200)
aviso.grid(row=2, column=0, padx=20)
button_iniciar = CTK.CTkButton(app, text="Iniciar", width=100)

the_label = CTK.CTkLabel(app, text="", text_color='white', font=('', 18))
the_label.grid(row=3, columnspan=2, padx=20)

app.mainloop()