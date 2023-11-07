from tkinter import Tk, Button, Entry, END


# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x250")

# Configuración pantalla de salida 

pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=100, padx=1, pady=1)

def A1(evento):
    final = pantalla.get()+"1"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
def A2(evento):
    final = pantalla.get()+"2"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
def A3(evento):
    final = pantalla.get()+"3"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
def A4(evento):
    final = pantalla.get()+"4"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
def A5(evento):
    final = pantalla.get()+"5"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
def A6(evento):
    final = pantalla.get()+"6"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
def A7(evento):
    final = pantalla.get()+"7"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
def A8(evento):
    final = pantalla.get()+"8"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
def A9(evento):
    final = pantalla.get()+"9"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
def AS(evento):
    final = pantalla.get()+"+"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
def AR(evento):
    final = pantalla.get()+"-"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
def AM(evento):
    final = pantalla.get()+"*"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
def AD(evento):
    final = pantalla.get()+"/"
    pantalla.delete(0,END)
    pantalla.insert(0,final)
    
def Calcular(evento):
    try:
        numeros  = []
        if "+" in pantalla.get():
            numeros = pantalla.get().split("+")
            pantalla.delete(0,END)
            pantalla.insert(0,float(numeros[0])+float(numeros[1]))
        elif "-" in pantalla.get():
            numeros = pantalla.get().split("-")
            pantalla.delete(0,END)
            pantalla.insert(0,float(numeros[0])-float(numeros[1]))
        elif "*" in pantalla.get():
            numeros = pantalla.get().split("*")
            pantalla.delete(0,END)
            pantalla.insert(0,float(numeros[0])*float(numeros[1]))
        elif "/" in pantalla.get():
            pantalla.delete(0,END)
            pantalla.insert(0,float(numeros[0])/float(numeros[1]))
            numeros = pantalla.get().split("/")
    except:
        pantalla.delete(0,END)
        pantalla.insert(0,"Operacion  Invalida")
        
        #pantalla.delete(0,END)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_1.bind("<Button-1>",A1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_2.bind("<Button-1>",A2)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_3.bind("<Button-1>",A3)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_4.bind("<Button-1>",A4)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_5.bind("<Button-1>",A5)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_6.bind("<Button-1>",A6)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_7.bind("<Button-1>",A7)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_8.bind("<Button-1>",A8)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_9.bind("<Button-1>",A9)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_igual.bind("<Button-1>",Calcular)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_mas.bind("<Button-1>",AS)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_menos.bind("<Button-1>",AR)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_multiplicacion.bind("<Button-1>",AM)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)
boton_division.bind("<Button-1>",AD)



    

root.mainloop()