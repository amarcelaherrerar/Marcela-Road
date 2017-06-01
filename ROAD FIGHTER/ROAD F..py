import tkinter
import time

ventana = tkinter.Tk()
ventana.geometry("5000x700")
ventana.title("ROAD FIGHTER")
nivel1=tkinter.Toplevel()

#LO DEL MENÚ.

fondo=tkinter.PhotoImage(file="el_fondo.png")
lblFondo=tkinter.Label(ventana,image=fondo).place(x=0,y=0)

lblNombreJ=tkinter.Label(text="NOMBRE DE LOS JUGADORES:").place(x=100,y=205)
entradaN=tkinter.StringVar()
lblNombre=tkinter.Label(text="Jugador1:").place(x=40,y=230)
lblNombre=tkinter.Label(text="Jugador2:").place(x=40,y=260)

entradaN=tkinter.StringVar()
txtNombre1=tkinter.Entry(ventana,textvariable=entradaN).place(x=100,y=230)

entradaN=tkinter.StringVar()
txtNombre2=tkinter.Entry(ventana,textvariable=entradaN).place(x=100,y=260)

lblNombreN=tkinter.Label(text="Nivel:").place(x=100,y=300)
selec=tkinter.IntVar()


boton=tkinter.Button(ventana,text="1", command=main).place(x=140,y=300)

boton=tkinter.Button(ventana,text="2", command=main).place(x=180,y=300)

boton=tkinter.Button(ventana,text="3", command=main).place(x=220,y=300)

boton=tkinter.Button(ventana,text="4", command=main).place(x=260,y=300)

boton=tkinter.Button(ventana,text="5", command=main).place(x=300,y=300)


boton1= tkinter.Button(ventana,text="JUGAR PARTIDA").place(x=100,y=350)
boton2 = tkinter.Button(ventana,text="GUARDAR PARTIDA").place(x=100,y=450)
boton3 = tkinter.Button(ventana,text="SALIR").place(x=100,y=500)


