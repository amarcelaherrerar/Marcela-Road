import tkinter
import time
import random
from math import *

ventana = tkinter.Tk()
ventana.geometry("5000x700")
ventana.title("ROAD FIGHTER")
ventahija=tkinter.Toplevel()

lista=[ ]

#FONDO DE LA PANTALLA 1.


canvas = tkinter.Canvas(ventahija,width=3000,height=800, bg="white")


l=tkinter.PhotoImage(file="lado de la pantalla 1.png")
izquierdo=canvas.create_image(300,0,image=l)


d=tkinter.PhotoImage(file="lado de la pantalla 1.png")
derecho= canvas.create_image(1100,350,image=d)


  
# MINIVAN DE LA IZQUIERDA CORRIENDO.   
m=0    
def Van():
    global ventana, canvas, m, a
    canvas.move(a,0,5)
    if canvas.coords(a)[1]>=800:
        canvas.move(a,0,-canvas.coords(a)[1])


      
#PANTALLA DE LA IZQUIERDA CORRIENDO.
def pantallacorriendo_a():
    global ventana , canvas 
    canvas.move(izquierdo,0,5)
    if canvas.coords(izquierdo)[1]>=2400:
        canvas.move(izquierdo,0,-canvas.coords(izquierdo)[1])

#PANTALLA DE LA DERECHA CORRIENDO.
def pantallacorriendo_b():
    global ventana , canvas 
    canvas.move(derecho,0,5)
    if canvas.coords(derecho)[1]>=2400:
        canvas.move(derecho,0,-canvas.coords(derecho)[1])

#MINIVAN DE LA DERECHA CORRIENDO. 
def Van_b():
    global ventana, canvas, z
    canvas.move(z,0,5)
    if canvas.coords(z)[1]>=800:
        canvas.move(z,0,-canvas.coords(z)[1])


#RUNNER DE LA IZQUIERDA CORRIENDO.
direccion=1    
def Runner_a():
    global ventana, canvas, i, direccion
    
    canvas.move(i,-1,1)
    if canvas.coords(i)[0]<=200:
        direccion*=-1
        canvas.move(i,30,0)

    if (canvas.coords(i)[0]>=400):
         canvas.move(i,-30,1)
         direccion*=-1
    canvas.move(i,-5*direccion,1)
    
    if canvas.coords(i)[1]>=800:
        canvas.move(i,0,-canvas.coords(i)[1])    


#RUNNER DE LA DERECHA CORRIENDO.
direccion=1    
def Runner_b():
    global ventana, canvas, q, direccion
    
    canvas.move(q,-1,1)
    if canvas.coords(q)[0]<=1500:
        direccion*=-1
        canvas.move(q,30,0)

    if (canvas.coords(q)[0]>=500):
         canvas.move(q,-30,1)
         direccion*=-1
    canvas.move(q,-5*direccion,1)
    
    if canvas.coords(q)[1]>=800:
        canvas.move(q,0,-canvas.coords(q)[1])    

        
#COMBUSTIBLE DE LA IZQUIERDA CORRIENDO.
        
def Combustible_a():
    global ventana, canvas, z
    canvas.move(o,0,5)
    if canvas.coords(o)[1]>=800:
        canvas.move(o,0,-canvas.coords(o)[1])

     

#COMBUSTIBLE DE LA DERECHA CORRIENDO.
        
def Combustible_b():
    global ventana, canvas, z
    canvas.move(y,0,5)
    if canvas.coords(y)[1]>=800:
        canvas.move(y,0,-canvas.coords(y)[1])



#JUGADORES CORREN CON EL TECLADO.

def keyup(e):
  global x,lista

  if(e.keycode in lista):
    lista.pop(lista.index(e.keycode))
   

def keydown(e):
  global prime,segu,lista
  if not e.keycode in lista:
      
    lista.append(e.keycode)
  
 
J=tkinter.PhotoImage(file="Jugador 1.png")

prime=canvas.create_image(400,600,image=J)  

J2=tkinter.PhotoImage(file="Jugador 2.png")
segu=canvas.create_image(1250,600,image=J2)

def key():
  global lista, J, prime, J2, segu

  canvas.focus_set()

  if(65 in lista):  
    canvas.move(prime,-5,0)
    

        
       
  if(68 in lista):
    canvas.move(prime,5,0)

     
    
  if(74 in lista):
    canvas.move(segu,-5,0)
    
  if(76 in lista):
    canvas.move(segu,5,0)



#FIGHTER DE LA IZQUIERDA PERSIGUE AL JUGADOR DE LA IZQ

def Fighter_a():
   if(canvas.coords(fi)[1] < 700):
        if(canvas.coords(prime)[0]< canvas.coords(fi)[0]):
          canvas.move(fi,-2,5)
          
        elif(canvas.coords(prime)[0] > canvas.coords (fi)[0]):
           canvas.move(fi, 2,5)
        else:
           canvas.move(fi,2,5)
   else:
      canvas.move(fi,0,-700)
       


#FIGHTER DE LA DERECHA PERSIGUE AL JUGADOR DE LA DERCHA.

def Fighter_b():
   if(canvas.coords(fig)[1] < 700):
        if(canvas.coords(segu)[0]< canvas.coords(fig)[0]):
          canvas.move(fig,-2,5)
          
        elif(canvas.coords(segu)[0] > canvas.coords (fig)[0]):
           canvas.move(fig, 2,5)
        else:
           canvas.move(fig,2,5)
   else:
      canvas.move(fig,0,-700)

#CHOQUESS!

ex=tkinter.PhotoImage(file="explosion.png")
def Choques_a():
    global canvas

    canvas.focus_set()
    xp = canvas.coords(prime)[0]
    xa = canvas.coords (a) [0]
    xi = canvas.coords (i) [0]
    xf = canvas.coords (fi) [0]
    yp = canvas.coords(prime)[1]
    ya= canvas.coords (a) [1]
    yi = canvas.coords (i) [1]
    yf = canvas.coords (fi) [1]
    
    
    if (xp >= xa and xp <= xa+31 and yp >= ya and yp <= ya+64):
        explosion=canvas.create_image(xp,yp,image=ex)
        return True
    
    if (xp >= xi and xp <= xi+31 and yp >= ya and yp <= yi+64):
        explosion=canvas.create_image(xp,yp,image=ex)
        return True


    if (xp >= xf and xp <= xf+31 and yp >= yf and yp <= yf+64):
        explosion=canvas.create_image(xp,yp,image=ex)
        return True
    
def Choques_b():
    global canvas

    xp2 = canvas.coords(segu)[0]
    xa2 = canvas.coords (z) [0]
    xi2 = canvas.coords (q) [0]
    xf2 = canvas.coords (fig) [0]
    yp2 = canvas.coords (segu) [1]
    ya2 = canvas.coords (z) [1]
    yi2 = canvas.coords (q) [1]
    yf2 = canvas.coords (fig) [1] 

     
    if (xp2 >= xa2 and xp2 <= xa2+31 and yp2 >= ya2 and yp2 <= ya2+64):
        explosion=canvas.create_image(xp2,yp2,image=ex)
        return True
    
    if (xp2 >= xi2 and xp2 <= xi2+31 and yp2 >= ya2 and yp2 <= yi2+64):
        explosion=canvas.create_image(xp,yp,image=ex)
        return True


    if (xp2 >= xf2 and xp2 <= xf2+31 and yp2 >= yf2 and yp2 <= yf2+64):
        explosion=canvas.create_image(xp2,yp2,image=ex)
        return True
   

               

#canvas = tkinter.Canvas(ventahija,width=3000,height=800)
#canvas.pack()
v=tkinter.PhotoImage(file="MiniVan.png")
#a=canvas.create_Image(200,600, image=M)

ventahija.iconify()




     
def main():
    global ku, canvas, ventahija,mi

 
    Van()
    Van_b()
    Runner_a()
    Runner_b()
    Combustible_a()
    Combustible_b()
    Fighter_a()
    Fighter_b()
    if(Choques_a()):
        return 0
    
    if(Choques_b()):
        return 0
 
   

    pantallacorriendo_a()
    pantallacorriendo_b()
        
    ventahija.deiconify()
    key()
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
boton33 = tkinter.Button(ventana,text="SALIR", command=ventana.destroy).place(x=100,y=500)



#CARROS CARRETERA IZQUIERDA.

M=tkinter.PhotoImage(file="MiniVan.png")
a=canvas.create_image(250,40,image=M)

R=tkinter.PhotoImage(file="Runner.png")
i=canvas.create_image(200,40,image=R)

C=tkinter.PhotoImage(file="Combustible.png")
o=canvas.create_image(400,40,image=C)


F1=tkinter.PhotoImage(file="Figther.png")
fi=canvas.create_image(300,40,image=F1)


#CARROS CARRETERA DERECHA.

M2=tkinter.PhotoImage(file="MiniVan.png")
z=canvas.create_image(1000,40,image=M2)


R2=tkinter.PhotoImage(file="Runner.png")
q=canvas.create_image(1000,40,image=R2)


C2=tkinter.PhotoImage(file="Combustible.png")
y=canvas.create_image(1200,40,image=C2)


F2=tkinter.PhotoImage(file="Figther.png")
fig=canvas.create_image(1200,40,image=F2)



# Bindeamos
canvas.bind("<KeyPress>",keydown)
canvas.bind("<KeyRelease>",keyup)




canvas.pack()
ventana.mainloop()




























