import tkinter as tk
def jhordy():
    nnombre = tk.Label(vacilao,text=cnombre.get())
    nnombre.pack()
    aapellido= tk.Label(vacilao, text=capellido.get())
    aapellido.pack()
    tpsexo = tk.Label(vacilao, text=opcion.get())
    tpsexo.pack()
    seleccionados = ccuidad.curselection()
    for index in seleccionados:
        item = ccuidad.get(index)
        cui = tk.Label(vacilao, text=item)
        cui.pack()
   
    
    
    
ventana = tk.Tk()
ventana.title("mi primera ventana")
ventana.geometry("1024x960")

# nombre
lnombre =tk.Label(ventana, text="Nombre:")
lnombre.grid(row=0, column=0)
# cuadro de texto
cnombre = tk.Entry(ventana)
cnombre.grid(row=0, column= 1) 


# apellido
lapellido =tk.Label(ventana, text="Apellido:")
lapellido.grid(row=1, column=0)
#cuadro de texto
capellido = tk.Entry(ventana)
capellido.grid(row=1, column=1)


# sexo 
opcion = tk.StringVar()
lsexo =tk.Label(ventana, text="Sexo:")
lsexo.grid(row=2, column=0)
csexo1 = tk.Radiobutton(ventana, text="m", state="normal", variable=opcion, value="masculino")
csexo1.grid(row=3, column=1)
csexo2 = tk.Radiobutton(ventana, text="f", state="normal", variable=opcion, value="femenino")
csexo2.grid(row=3, column=2)


# cuidad
lcuidad =tk.Label(ventana, text="Cuidad:")
lcuidad.grid(row=4, column=0)
ccuidad = tk.Listbox(ventana, width=20, height=5)
ccuidad.grid(row=4, column=1)
ciudades = ["Cartagena", "Barranquilla", "Medellín", "Bogotá", "Cali"]
for ciudad in ciudades:
    ccuidad.insert(tk.END, ciudad)
    
# registro 
cregistro = tk.Button(ventana,text="registra", command=jhordy)
cregistro.grid(row=5, column=1)

#frame
vacilao = tk.Frame(ventana, width=200, height=100, bd=2, relief="solid")
vacilao.grid(row=6, column=1)






ventana.mainloop()