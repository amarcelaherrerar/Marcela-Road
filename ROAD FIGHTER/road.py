import tkinter
import time

ventana = tkinter.Tk()
ventana.geometry("5000x700")
ventana.title("ROAD FIGHTER")

ventahija=tkinter.Toplevel()



#FONDO DE LA PANTALLA 1.
canvas = tkinter.Canvas(ventahija,width=3000,height=800, bg="white")


l=tkinter.PhotoImage(file="lado de la pantalla 1.png")
izquierdo=canvas.create_image(300,0,image=l)


d=tkinter.PhotoImage(file="lado de la pantalla 1.png")
derecho= canvas.create_image(1100,350,image=d)

##############################################
c=tkinter.PhotoImage(file="Combustible.png")
r=tkinter.PhotoImage(file="Runner.png")
f=tkinter.PhotoImage(file="Figther.png")
v=tkinter.PhotoImage(file="Minivan.png")
##############################################
"""

"""





m=0

def Van():
    global ventana, canvas, m, a
    

    canvas.move(a,0,5)

    if canvas.coords(a)[1]>=800:
        canvas.move(a,0,-canvas.coords(a)[1])


      

def pantallacorriendo_a():

    global ventana , canvas 

  

    canvas.move(izquierdo,0,10)
    

    if canvas.coords(izquierdo)[1]>=2400:
        canvas.move(izquierdo,0,-canvas.coords(izquierdo)[1])

def pantallacorriendo_b():

    global ventana , canvas 

  

    canvas.move(derecho,0,10)
    

    if canvas.coords(derecho)[1]>=2400:
        canvas.move(derecho,0,-canvas.coords(derecho)[1])

def Van_b():
    global ventana, canvas, z
    

    canvas.move(z,0,5)

    if canvas.coords(z)[1]>=800:
        canvas.move(z,0,-canvas.coords(z)[1])

      
    

    
     


 
        

#canvas = tkinter.Canvas(ventahija,width=3000,height=800)
#canvas.pack()
v=tkinter.PhotoImage(file="MiniVan.png")
#a=canvas.create_Image(200,600, image=M)

        
def main():
    global ku, canvas, ventahija

    Van()
    Van_b()

    ventana.after(20,pantallacorriendo_a)
    ventana.after(20,pantallacorriendo_b)
        
    ventahija.deiconify()
    ventana.iconify()

    ventahija.after(15,main)

def primernivel():

    main()
    











#LO DEL MENÚ.

fondo=tkinter.PhotoImage(file="el_fondo.png")
lblFondo=tkinter.Label(ventana,image=fondo).place(x=0,y=0)

lblNombreJ=tkinter.Label(text="NOMBRE DE LOS JUGADORES:").place(x=100,y=205)
entradaN2=tkinter.StringVar()
lblNombre1=tkinter.Label(text="Jugador1:").place(x=40,y=230)
lblNombre2=tkinter.Label(text="Jugador2:").place(x=40,y=260)

entradaN=tkinter.StringVar()
txtNombre1=tkinter.Entry(ventana,textvariable=entradaN).place(x=100,y=230)

entradaN1=tkinter.StringVar()
txtNombre2=tkinter.Entry(ventana,textvariable=entradaN1).place(x=100,y=260)



lblNombreN=tkinter.Label(text="Nivel:").place(x=100,y=300)
selec=tkinter.IntVar()


boton1=tkinter.Button(ventana,text="1",command=primernivel).place(x=140,y=300)

boton2=tkinter.Button(ventana,text="2").place(x=180,y=300)

boton3=tkinter.Button(ventana,text="3").place(x=220,y=300)

boton4=tkinter.Button(ventana,text="4").place(x=260,y=300)

boton5=tkinter.Button(ventana,text="5").place(x=300,y=300)


boton11= tkinter.Button(ventana,text="JUGAR PARTIDA").place(x=100,y=350)
boton22 = tkinter.Button(ventana,text="GUARDAR PARTIDA").place(x=100,y=450)
boton33 = tkinter.Button(ventana,text="SALIR").place(x=100,y=500)



#CARROS CARRETERA IZQUIERDA.

M=tkinter.PhotoImage(file="MiniVan.png")
a=canvas.create_image(200,40,image=M)

#############################SE VA MOVIENDO LA MINIVAN.


 
#######


F=tkinter.PhotoImage(file="Figther.png")
e=canvas.create_image(250,600,image=F)

R=tkinter.PhotoImage(file="Runner.png")
i=canvas.create_image(350,600,image=R)

C=tkinter.PhotoImage(file="Combustible.png")
o=canvas.create_image(400,600,image=C)

J=tkinter.PhotoImage(file="Jugador 1.png")
u=canvas.create_image(400,500,image=J)


#####################################################################



#CARROS CARRETERA DERECHA.

M2=tkinter.PhotoImage(file="MiniVan.png")
z=canvas.create_image(1000,40,image=M2)

w=F2=tkinter.PhotoImage(file="Figther.png")
canvas.create_image(1070,500,image=F2)

t=R2=tkinter.PhotoImage(file="Runner.png")
q=canvas.create_image(1150,500,image=R2)

C2=tkinter.PhotoImage(file="Combustible.png")
y=canvas.create_image(1200,500,image=C2)

J2=tkinter.PhotoImage(file="Jugador 2.png")
s=canvas.create_image(1250,500,image=J2)






canvas.pack()
ventana.mainloop()




























