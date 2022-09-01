from tkinter import *
from tkinter import filedialog 
from tkinter import messagebox 
tipo = ""


def explorador(): 
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("CSV", "*.csv*"), ("all files", "*.*"))) 
    direccion.set(filename)                                                                      
def continuar():
	window.withdraw()
	win2 = Toplevel()
	win2.geometry("500x200")
	win2.config(background = "#d9ead3")
	framecabeza2 = Frame(win2)
	framecabeza2.grid(row=0, column=0)
	framecuerpo2 = Frame(win2)
	framecuerpo2.grid(row=1, column=0)
	framefinal2 = Frame(win2)
	framefinal2.grid(row=3, column=0,sticky=S)
	Label(framecabeza2, text="¿Cómo quieres procesar la base de datos?",background="#d9ead3",fg="black",font=("Arial ", 10)).grid(row=0,column=0,sticky="w")
	button_filtra = Button(framecuerpo2,text = "Palabras deseadas",command = nodeseadas) 
	button_filtra.grid(column = 0, row = 0)
	button_filtra2 = Button(framecuerpo2,text = "Palabras no deseadas",command = deseadas) 
	button_filtra2.grid(column = 1, row = 0)
	button_exit2 = Button(framefinal2,text = "Exit",command = exit)    
	button_exit2.grid(column = 0, row = 0)
def deseadas():
	tipo="deseadas"
	tercerpaso()

def nodeseadas():	
	tipo="nodeseadas"
	tercerpaso()

def tercerpaso():
	win3 = Toplevel()
	win3.geometry("500x200")
	win3.config(background = "#d9ead3")
	framecabeza3 = Frame(win3)
	framecabeza3.grid(row=0, column=0)
	framecuerpo3 = Frame(win3)
	framecuerpo3.grid(row=1, column=0)
	framefinal3 = Frame(win3)
	framefinal3.grid(row=3, column=0,sticky=S)
	Label(framecabeza3, text="¿Cómo quieres procesar la base de datos?",background="#d9ead3",fg="black",font=("Arial ", 10)).grid(row=0,column=0,sticky="w")
	button_filtra3 = Button(framecuerpo3,text = "Palabras deseadas",command = nodeseadas) 
	button_filtra3.grid(column = 0, row = 0)
	button_filtra12 = Button(framecuerpo3,text = "Palabras no deseadas",command = deseadas) 
	button_filtra12.grid(column = 1, row = 0)
	button_exit3 = Button(framefinal3,text = "Exit",command = exit)    
	button_exit3.grid(column = 0, row = 0)
	win2.destroy






	

	if not direccion:
		messagebox.showinfo("ATENCION", "Debe seleccionar un archivo para poder continuar")
		window.withdraw()
window = Tk()    
#elementos de la primer ventana 
window.title('Herramienta para purga base de datos')  
window.geometry("500x200")   
window.config(background = "#d9ead3")
framecabeza=Frame(window)
framecuerpo=Frame(window, width=500, height=300)
framefinal=Frame(window, width=500)
framecabeza.pack(anchor=W)
framecuerpo.pack(anchor=W)
framefinal.pack(anchor=SW)
framefinal.config(background = "#d9ead3")
framecabeza.config(background = "#d9ead3")
framecuerpo.config(background = "#d9ead3")
direccion=StringVar()
Label(framecabeza, text="¿Que base de datos desea procesar?",background="#d9ead3",fg="black",font=("Arial ", 10)).grid(row=0,column=0,sticky="w")
txtbusqueda=Entry(framecuerpo, textvariable=direccion, width=50,)
txtbusqueda.grid(row=0,column=0,pady=6,sticky="w")
button_explore = Button(framecuerpo,text = "Buscar archivo",command = explorador) 
button_explore.grid(column = 1, row = 0)
button_exit = Button(framefinal,text = "Exit",command = exit)    
button_exit.grid(column = 0, row = 0)
button_continuar = Button(framefinal,text = "Continuar",command = continuar)    
button_continuar.grid(column = 1, row = 0)
#elementos de la segunda ventana 



window.mainloop() 
