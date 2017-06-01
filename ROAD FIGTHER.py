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
global canvas 
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
    canvas.move(izquierdo,0,10)
    if canvas.coords(izquierdo)[1]>=2400:
        canvas.move(izquierdo,0,-canvas.coords(izquierdo)[1])

#PANTALLA DE LA DERECHA CORRIENDO.
def pantallacorriendo_b():
    global ventana , canvas 
    canvas.move(derecho,0,10)
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
 
#COMBUSTIBLE DE LA DERECHA CORRIENDO
        
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

explo=tkinter.PhotoImage(file= "explosion.png")
def key():
  global lista, J, prime, J2, segu, explo
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

    
def mancha_a():
    global ventana, canvas, m, mancha
    canvas.move(mancha,0,5)
    if canvas.coords(mancha)[1]>= 1000:
        canvas.move(mancha,0,-canvas.coords(mancha)[1])

def mancha_b():
    global ventana, canvas, m, mancha
    canvas.move(mancha1,0,5)
    if canvas.coords(mancha1)[1]>= 1000:
        canvas.move(mancha1,0,-canvas.coords(mancha1)[1])



#CHOQUESS!
explosionpng=tkinter.PhotoImage(file="laexplosion.png")
def Choques_a():
    global canvas, explosionpng, cuentaGasolina1, explosionpng, cuentaVelocidad1

    canvas.focus_set()
    xp = canvas.coords(prime)[0]
    xa = canvas.coords (a) [0]
    xi = canvas.coords (i) [0]
    xf = canvas.coords (fi) [0]
    xc = canvas.coords (o) [0]
    yp = canvas.coords(prime)[1]
    ya= canvas.coords (a) [1]
    yi = canvas.coords (i) [1]
    yf = canvas.coords (fi) [1]
    xm = canvas.coords(mancha) [0]
    ym = canvas.coords(mancha1) [0]
    
    
    if (xp >= xa and xp <= xa+23 and yp >= ya and yp <= ya+46):
        canvas.move(prime,10,0)
        cuentaGasolina1=cuentaGasolina1-400
        cuentaVelocidad1=cuentaVelocidad1-20

        return True
        
    if (xp >= xm and xp <= xm+23 and yp >= ym and yp <= ym+46):
        canvas.move(prime,10,0)
        cuentaGasolina1=cuentaGasolina1-400
        cuentaVelocidad1=cuentaVelocidad1-20

        return True
    
    if (xp + 23 >= xa and xp <= xa + 23 and ya+23>= yp and ya <= yp + 46): 
        canvas.move(prime,-5,0)     

    
    
    if (xp >= xi and xp <= xi+23 and yp >= yi and yp <= yi+46):
        canvas.move(prime,5,0)
        return True
    if (xp + 23 >= xi and xp <= xi + 23 and yi+23>= yp and yi <= yp + 46): 
        canvas.move(prime,-5,0) 



    if (xp >= xf and xp <= xf+23 and yp >= yf and yp <= yf+46):
        canvas.move(prime,5,0) 
        return True
    if (xp + 23 >= xf and xp <= xf + 23 and yf+23>= yp and yf <= yp + 46): 
        canvas.move(prime,-5,0)


    if canvas.coords(prime)[0]>=455 :

      cuentaGasolina1=0
      canvas.move(fi,-5,0)
      explosion=canvas.create_image(canvas.coords(prime)[0],canvas.coords(prime)[1], image=explosionpng)
      canvas.move(prime, 0, -20000)
      
    elif  canvas.coords(prime)[0]<=180:

      cuentaGasolina1=0
      canvas.move(fi,5,0)
      explosion=canvas.create_image(canvas.coords(prime)[0],canvas.coords(prime)[1], image=explosionpng)
      canvas.move(prime, 0, -20000)

def Choques_b():
    global canvas, cuentaGasolina11,cuentaVelocidad11 
    xp2 = canvas.coords(segu)[0]
    xa2 = canvas.coords (z) [0]
    xi2 = canvas.coords (q) [0]
    xf2 = canvas.coords (fig) [0]
    yp2 = canvas.coords (segu) [1]
    ya2 = canvas.coords (z) [1]
    yi2 = canvas.coords (q) [1]
    yf2 = canvas.coords (fig) [1]
    xm = canvas.coords (mancha1) [1]
    ym = canvas.coords(mancha) [0]
    

     
    if (xp2 >= xa2 and xp2 <= xa2+23 and yp2 >= ya2 and yp2 <= ya2+46):
        canvas.move(segu,10,0)
        cuentaGasolina11=cuentaGasolina11-400
        cuentaVelocidad11=cuentaVelocidad11-20

        return True
    
    if (xp2 >= xm and xp2 <= xm+23 and yp2 >= ym and yp2 <= ym+46):
        canvas.move(segu,10,0)
        cuentaGasolina11=cuentaGasolina11-400
        cuentaVelocidad11=cuentaVelocidad11-20

        return True




    
    if (xp2 + 23 >= xa2 and xp2 <= xa2 + 23 and ya2+23>= yp2 and ya2 <= yp2 + 46): 
        canvas.move(segu,-5,0)     
   
    
    if (xp2 >= xi2 and xp2 <= xi2+23 and yp2 >= yi2 and yp2 <= yi2+46):
        canvas.move(segu,5,0)
        return True
    if (xp2 + 23 >= xi2 and xp2 <= xi2 + 23 and yi2+23>= yp2 and yi2 <= yp2 + 46): 
        canvas.move(segu,-5,0) 


    if (xp2 >= xf2 and xp2 <= xf2+23 and yp2 >= yf2 and yp2 <= yf2+46):
        canvas.move(segu,5,0) 
        return True
    if (xp2 + 23 >= xf2 and xp2 <= xf2 + 23 and yf2+23>= yp2 and yf2 <= yp2 + 46): 
        canvas.move(segu,-5,0)

    if canvas.coords(segu)[0]>=1280 :

      cuentaGasolina11=0
      canvas.move(fig,-5,0)
      explosion=canvas.create_image(canvas.coords(segu)[0],canvas.coords(segu)[1], image=explosionpng)
      canvas.move(segu, 0, -20000)

      
    elif  canvas.coords(segu)[0]<=1000:

      cuentaGasolina11=0
      canvas.move(fig,5,0)
      explosion=canvas.create_image(canvas.coords(segu)[0],canvas.coords(segu)[1], image=explosionpng)
      canvas.move(segu, 0, -20000)



#SEGUNDO NIVEL.
lista2=[ ]
#FONDO DE LA PANTALLA 2.
l2=tkinter.PhotoImage(file="lado de la pantalla 2.png")
izquierdo2=canvas.create_image(300,0,image=l2)

d2=tkinter.PhotoImage(file="lado de la pantalla 2.png")
derecho2= canvas.create_image(1100,350,image=d2)

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

# MINIVAN2 DE LA IZQUIERDA CORRIENDO.   
m2=0    
def Van2():
    global ventana, canvas, m2, a
    canvas.move(a,0,5)
    if canvas.coords(a)[1]>=800:
        canvas.move(a,0,-canvas.coords(a)[1])
        
#PANTALLA DE LA IZQUIERDA CORRIENDO.
def pantallacorriendo_a2():
    global ventana , canvas 
    canvas.move(izquierdo2,0,16)
    if canvas.coords(izquierdo2)[1]>=2400:
        canvas.move(izquierdo2,0,-canvas.coords(izquierdo2)[1])

#PANTALLA DE LA DERECHA CORRIENDO.
def pantallacorriendo_b2():
    global ventana , canvas 
    canvas.move(derecho2,0,16)
    if canvas.coords(derecho2)[1]>=2400:
        canvas.move(derecho2,0,-canvas.coords(derecho2)[1])

#MINIVAN DE LA DERECHA CORRIENDO. 
def Van_b2():
    global ventana, canvas, z
    canvas.move(z,0,5)
    if canvas.coords(z)[1]>=800:
        canvas.move(z,0,-canvas.coords(z)[1])

#RUNNER DE LA IZQUIERDA CORRIENDO.
direccion2=1    
def Runner_a2():
    global ventana, canvas, i, direccion2    
    canvas.move(i,-1,1)
    if canvas.coords(i)[0]<=200:
        direccion2*=-1
        canvas.move(i,30,0)
    if (canvas.coords(i)[0]>=400):
         canvas.move(i,-30,1)
         direccion2*=-1
    canvas.move(i,-5*direccion2,1)    
    if canvas.coords(i)[1]>=800:
        canvas.move(i,0,-canvas.coords(i)[1])    

#RUNNER DE LA DERECHA CORRIENDO.
direccion2=1    
def Runner_b2():
    global ventana, canvas, q, direccion2    
    canvas.move(q,-1,1)
    if canvas.coords(q)[0]<=1500:
        direccion2*=-1
        canvas.move(q,30,0)

    if (canvas.coords(q)[0]>=500):
         canvas.move(q,-30,1)
         direccion2*=-1
    canvas.move(q,-5*direccion2,1)
    
    if canvas.coords(q)[1]>=800:
        canvas.move(q,0,-canvas.coords(q)[1])    
        
#COMBUSTIBLE DE LA IZQUIERDA CORRIENDO.        
def Combustible_a2():
    global ventana, canvas, z
    canvas.move(o,0,5)
    if canvas.coords(o)[1]>=800:
        canvas.move(o,0,-canvas.coords(o)[1])
 
#COMBUSTIBLE DE LA DERECHA CORRIENDO.        
def Combustible_b2():
    global ventana, canvas, z
    canvas.move(y,0,5)
    if canvas.coords(y)[1]>=800:
        canvas.move(y,0,-canvas.coords(y)[1])

#JUGADORES CORREN CON EL TECLADO.
def keyup2(e2):
  global x,lista2
  if(e.keycode in lista2):
    lista2.pop(lista2.index(e2.keycode))

def keydown2(e2):
  global prime,segu,lista
  if not e2.keycode in lista2:
     lista2.append(e2.keycode)
   
J=tkinter.PhotoImage(file="Jugador 1.png")
prime=canvas.create_image(400,600,image=J)  

J2=tkinter.PhotoImage(file="Jugador 2.png")
segu=canvas.create_image(1250,600,image=J2)

def key2():
  global lista2, J, prime, J2, segu
  canvas.focus_set()
  if(65 in lista2):  
    canvas.move(prime,-5,0)   
  if(68 in lista2):
    canvas.move(prime,5,0)     
  if(74 in lista2):
    canvas.move(segu,-5,0)    
  if(76 in lista2):
    canvas.move(segu,5,0)
    
#FIGHTER DE LA IZQUIERDA PERSIGUE AL JUGADOR DE LA IZQ
def Fighter_a2():
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
def Fighter_b2():
   if(canvas.coords(fig)[1] < 700):
        if(canvas.coords(segu)[0]< canvas.coords(fig)[0]):
          canvas.move(fig,-2,5)
          
        elif(canvas.coords(segu)[0] > canvas.coords (fig)[0]):
           canvas.move(fig, 2,5)
        else:
           canvas.move(fig,2,5)
   else: 
      canvas.move(fig,0,-700)
      
#manchas.
def mancha_a2():
    global ventana, canvas, m, mancha
    canvas.move(mancha,0,5)
    if canvas.coords(mancha)[1]>= 1000:
        canvas.move(mancha,0,-canvas.coords(mancha)[1])

def mancha_b2():
    global ventana, canvas, m, mancha
    canvas.move(mancha1,0,5)
    if canvas.coords(mancha1)[1]>= 1000:
        canvas.move(mancha1,0,-canvas.coords(mancha1)[1])

#CHOQUE DE LA CARRETERA DERECHA.
def Choques_a2():
    global canvas, explosionpng, cuentaGasolina2, explosionpng, cuentaVelocidad2

    canvas.focus_set()
    xp2 = canvas.coords(prime)[0]
    xa2 = canvas.coords (a) [0]
    xi2 = canvas.coords (i) [0]
    xf2 = canvas.coords (fi) [0]
    yp2 = canvas.coords(prime)[1]
    ya2= canvas.coords (a) [1]
    yi2 = canvas.coords (i) [1]
    yf2 = canvas.coords (fi) [1]
    
    if (xp2 >= xa2 and xp2 <= xa2+23 and yp2 >= ya2 and yp2 <= ya2+46):
        canvas.move(prime,10,0)
        cuentaGasolina2=cuentaGasolina2-400
        cuentaVelocidad2=cuentaVelocidad2-20

        return True  
    if (xp2 + 23 >= xa2 and xp2 <= xa2 + 23 and ya2+23>= yp2 and ya2 <= yp2 + 46): 
        canvas.move(prime,-5,0)     

    
    
    if (xp2 >= xi2 and xp2 <= xi2+23 and yp2 >= yi2 and yp2 <= yi2+46):
        canvas.move(prime,5,0)
        return True
    if (xp2 + 23 >= xi2 and xp2 <= xi2 + 23 and yi2+23>= yp2 and yi2 <= yp2 + 46): 
        canvas.move(prime,-5,0) 



    if (xp2 >= xf2 and xp2 <= xf2+23 and yp2 >= yf2 and yp2 <= yf2+46):
        canvas.move(prime,5,0) 
        return True
    if (xp2 + 23 >= xf2 and xp2 <= xf2 + 23 and yf2+23>= yp2 and yf2 <= yp2 + 46): 
        canvas.move(prime,-5,0)


    if canvas.coords(prime)[0]>=455 :

      cuentaGasolina2=0
      canvas.move(fi,-5,0)
      explosion=canvas.create_image(canvas.coords(prime)[0],canvas.coords(prime)[1], image=explosionpng)
      canvas.move(prime, 0, -20000)

      
    elif  canvas.coords(prime)[0]<=180:

      cuentaGasolina2=0
      canvas.move(fi,5,0)
      explosion=canvas.create_image(canvas.coords(prime)[0],canvas.coords(prime)[1], image=explosionpng)
      canvas.move(prime, 0, -20000)
   
#CHOQUES DE LA CARRETERA IZQUIERDA.        
def Choques_b2():
    global canvas, cuentaGasolina22,cuentaVelocidad22 
    xp2 = canvas.coords(segu)[0]
    xa2 = canvas.coords (z) [0]
    xi2 = canvas.coords (q) [0]
    xf2 = canvas.coords (fig) [0]
    yp2 = canvas.coords (segu) [1]
    ya2 = canvas.coords (z) [1]
    yi2 = canvas.coords (q) [1]
    yf2 = canvas.coords (fig) [1] 
     
    if (xp2 >= xa2 and xp2 <= xa2+23 and yp2 >= ya2 and yp2 <= ya2+46):
        canvas.move(segu,10,0)
        cuentaGasolina22=cuentaGasolina22-400
        cuentaVelocidad22=cuentaVelocidad22-20

        return True  
    if (xp2 + 23 >= xa2 and xp2 <= xa2 + 23 and ya2+23>= yp2 and ya2 <= yp2 + 46): 
        canvas.move(segu,-5,0)        
    
    if (xp2 >= xi2 and xp2 <= xi2+23 and yp2 >= yi2 and yp2 <= yi2+46):
        canvas.move(segu,5,0)
        return True
    if (xp2 + 23 >= xi2 and xp2 <= xi2 + 23 and yi2+23>= yp2 and yi2 <= yp2 + 46): 
        canvas.move(segu,-5,0) 

    if (xp2 >= xf2 and xp2 <= xf2+23 and yp2 >= yf2 and yp2 <= yf2+46):
        canvas.move(segu,5,0) 
        return True
    if (xp2 + 23 >= xf2 and xp2 <= xf2 + 23 and yf2+23>= yp2 and yf2 <= yp2 + 46): 
        canvas.move(segu,-5,0)


    if canvas.coords(segu)[0]>=1280 :
      cuentaGasolina22=0
      canvas.move(fig,-5,0)
      explosion=canvas.create_image(canvas.coords(segu)[0],canvas.coords(segu)[1], image=explosionpng)
      canvas.move(segu, 0, -20000)

      
    elif  canvas.coords(segu)[0]<=1000:
      cuentaGasolina22=0
      canvas.move(fig,5,0)
      explosion=canvas.create_image(canvas.coords(segu)[0],canvas.coords(segu)[1], image=explosionpng)
      canvas.move(segu, 0, -20000)
     
ventahija.iconify()
##TERCER NIVEL.
lista3=[ ]
#FONDO DE LA PANTALLA 3.
l3=tkinter.PhotoImage(file="lado de la pantalla 3.png")
izquierdo3=canvas.create_image(300,0,image=l3)
d3=tkinter.PhotoImage(file="lado de la pantalla 3.png")
derecho3= canvas.create_image(1100,350,image=d3)

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

# MINIVAN2 DE LA IZQUIERDA CORRIENDO.   
m3=0    
def Van3():
    global ventana, canvas, m3, a
    canvas.move(a,0,5)
    if canvas.coords(a)[1]>=800:
        canvas.move(a,0,-canvas.coords(a)[1])
    
#PANTALLA DE LA IZQUIERDA CORRIENDO.
def pantallacorriendo_a3():
    global ventana , canvas 
    canvas.move(izquierdo3,0,17)
    if canvas.coords(izquierdo3)[1]>=2400:
        canvas.move(izquierdo3,0,-canvas.coords(izquierdo3)[1])

#PANTALLA DE LA DERECHA CORRIENDO.
def pantallacorriendo_b3():
    global ventana , canvas 
    canvas.move(derecho3,0,17)
    if canvas.coords(derecho3)[1]>=2400:
        canvas.move(derecho3,0,-canvas.coords(derecho3)[1])

#MINIVAN DE LA DERECHA CORRIENDO. 
def Van_b3():
    global ventana, canvas, z
    canvas.move(z,0,5)
    if canvas.coords(z)[1]>=800:
        canvas.move(z,0,-canvas.coords(z)[1])

#RUNNER DE LA IZQUIERDA CORRIENDO.
direccion3=1    
def Runner_a3():
    global ventana, canvas, i, direccion3    
    canvas.move(i,-1,1)
    if canvas.coords(i)[0]<=200:
        direccion3*=-1
        canvas.move(i,30,0)
    if (canvas.coords(i)[0]>=400):
         canvas.move(i,-30,1)
         direccion3*=-1
    canvas.move(i,-5*direccion3,1)    
    if canvas.coords(i)[1]>=800:
        canvas.move(i,0,-canvas.coords(i)[1])    

#RUNNER DE LA DERECHA CORRIENDO.
direccion3=1    
def Runner_b3():
    global ventana, canvas, q, direccion3
    canvas.move(q,-1,1)
    if canvas.coords(q)[0]<=1500:
        direccion3*=-1
        canvas.move(q,30,0)
    if (canvas.coords(q)[0]>=500):
         canvas.move(q,-30,1)
         direccion3*=-1
    canvas.move(q,-5*direccion3,1)    
    if canvas.coords(q)[1]>=800:
        canvas.move(q,0,-canvas.coords(q)[1])    
        
#COMBUSTIBLE DE LA IZQUIERDA CORRIENDO.
        
def Combustible_a3():
    global ventana, canvas, z
    canvas.move(o,0,5)
    if canvas.coords(o)[1]>=800:
        canvas.move(o,0,-canvas.coords(o)[1])
 
#COMBUSTIBLE DE LA DERECHA CORRIENDO.
        
def Combustible_b3():
    global ventana, canvas, z
    canvas.move(y,0,5)
    if canvas.coords(y)[1]>=800:
        canvas.move(y,0,-canvas.coords(y)[1])

#JUGADORES CORREN CON EL TECLADO.

def keyup3(e3):
  global x,lista3
  if(e.keycode in lista3):
    lista3.pop(lista3.index(e3.keycode))

def keydown3(e3):
  global prime,segu,lista
  if not e3.keycode in lista3:
     lista3.append(e3.keycode)
   
J=tkinter.PhotoImage(file="Jugador 1.png")
prime=canvas.create_image(400,600,image=J)  

J2=tkinter.PhotoImage(file="Jugador 2.png")
segu=canvas.create_image(1250,600,image=J2)

def key3():
  global lista3, J, prime, J2, segu
  canvas.focus_set()
  if(65 in lista3):  
    canvas.move(prime,-5,0)   
  if(68 in lista3):
    canvas.move(prime,5,0)     
  if(74 in lista3):
    canvas.move(segu,-5,0)    
  if(76 in lista3):
    canvas.move(segu,5,0)
    
#FIGHTER DE LA IZQUIERDA PERSIGUE AL JUGADOR DE LA IZQ

def Fighter_a3():
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
def Fighter_b3():
   if(canvas.coords(fig)[1] < 700):
        if(canvas.coords(segu)[0]< canvas.coords(fig)[0]):
          canvas.move(fig,-2,5)          
        elif(canvas.coords(segu)[0] > canvas.coords (fig)[0]):
           canvas.move(fig, 2,5)
        else:
           canvas.move(fig,2,5)
   else:
      canvas.move(fig,0,-700)


#manchas.
def mancha_a3():
    global ventana, canvas, m, mancha
    canvas.move(mancha,0,5)
    if canvas.coords(mancha)[1]>= 1000:
        canvas.move(mancha,0,-canvas.coords(mancha)[1])

def mancha_b3():
    global ventana, canvas, m, mancha
    canvas.move(mancha1,0,5)
    if canvas.coords(mancha1)[1]>= 1000:
        canvas.move(mancha1,0,-canvas.coords(mancha1)[1])

#CHOQUES
def Choques_a3():
    global canvas, explosionpng, cuentaGasolina3, explosionpng, cuentaVelocidad3

    canvas.focus_set()
    xp2 = canvas.coords(prime)[0]
    xa2 = canvas.coords (a) [0]
    xi2 = canvas.coords (i) [0]
    xf2 = canvas.coords (fi) [0]
    yp2 = canvas.coords(prime)[1]
    ya2= canvas.coords (a) [1]
    yi2 = canvas.coords (i) [1]
    yf2 = canvas.coords (fi) [1]
    
    if (xp2 >= xa2 and xp2 <= xa2+23 and yp2 >= ya2 and yp2 <= ya2+46):
        canvas.move(prime,10,0)
        cuentaGasolina3=cuentaGasolina3-400
        cuentaVelocidad3=cuentaVelocidad3-20
        return True  
    if (xp2 + 23 >= xa2 and xp2 <= xa2 + 23 and ya2+23>= yp2 and ya2 <= yp2 + 46): 
        canvas.move(prime,-5,0)      
    
    if (xp2 >= xi2 and xp2 <= xi2+23 and yp2 >= yi2 and yp2 <= yi2+46):
        canvas.move(prime,5,0)
        return True
    if (xp2 + 23 >= xi2 and xp2 <= xi2 + 23 and yi2+23>= yp2 and yi2 <= yp2 + 46): 
        canvas.move(prime,-5,0) 

    if (xp2 >= xf2 and xp2 <= xf2+23 and yp2 >= yf2 and yp2 <= yf2+46):
        canvas.move(prime,5,0) 
        return True
    if (xp2 + 23 >= xf2 and xp2 <= xf2 + 23 and yf2+23>= yp2 and yf2 <= yp2 + 46): 
        canvas.move(prime,-5,0)
    if canvas.coords(prime)[0]>=455 :

      cuentaGasolina3=0
      canvas.move(fi,-5,0)
      explosion=canvas.create_image(canvas.coords(prime)[0],canvas.coords(prime)[1], image=explosionpng)
      canvas.move(prime, 0, -20000)
      
    elif  canvas.coords(prime)[0]<=180:

      cuentaGasolina3=0
      canvas.move(fi,5,0)
      explosion=canvas.create_image(canvas.coords(prime)[0],canvas.coords(prime)[1], image=explosionpng)
      canvas.move(prime, 0, -20000)
       
def Choques_b3():
    global canvas, cuentaGasolina33,cuentaVelocidad33 
    xp2 = canvas.coords(segu)[0]
    xa2 = canvas.coords (z) [0]
    xi2 = canvas.coords (q) [0]
    xf2 = canvas.coords (fig) [0]
    yp2 = canvas.coords (segu) [1]
    ya2 = canvas.coords (z) [1]
    yi2 = canvas.coords (q) [1]
    yf2 = canvas.coords (fig) [1] 
     
    if (xp2 >= xa2 and xp2 <= xa2+23 and yp2 >= ya2 and yp2 <= ya2+46):
        canvas.move(segu,10,0)
        cuentaGasolina33=cuentaGasolina33-400
        cuentaVelocidad33=cuentaVelocidad33-20

        return True  
    if (xp2 + 23 >= xa2 and xp2 <= xa2 + 23 and ya2+23>= yp2 and ya2 <= yp2 + 46): 
        canvas.move(segu,-5,0)
    
    if (xp2 >= xi2 and xp2 <= xi2+23 and yp2 >= yi2 and yp2 <= yi2+46):
        canvas.move(segu,5,0)
        return True
    if (xp2 + 23 >= xi2 and xp2 <= xi2 + 23 and yi2+23>= yp2 and yi2 <= yp2 + 46): 
        canvas.move(segu,-5,0)
    if (xp2 >= xf2 and xp2 <= xf2+23 and yp2 >= yf2 and yp2 <= yf2+46):
        canvas.move(segu,5,0)
        return True
    if (xp2 + 23 >= xf2 and xp2 <= xf2 + 23 and yf2+23>= yp2 and yf2 <= yp2 + 46): 
        canvas.move(segu,-5,0)

    if canvas.coords(segu)[0]>=1280 :

      cuentaGasolina33=0
      canvas.move(fig,-5,0)
      explosion=canvas.create_image(canvas.coords(segu)[0],canvas.coords(segu)[1], image=explosionpng)
      canvas.move(segu, 0, -20000)
      
    elif  canvas.coords(segu)[0]<=1000:

      cuentaGasolina33=0
      canvas.move(fig,5,0)
      explosion=canvas.create_image(canvas.coords(segu)[0],canvas.coords(segu)[1], image=explosionpng)
      canvas.move(segu, 0, -20000)
   
ventahija.iconify()


#CUARTO NIVEL.
lista4=[ ]
#FONDO DE LA PANTALLA 4.
l4=tkinter.PhotoImage(file="lado de la pantalla 4.png")
izquierdo4=canvas.create_image(300,0,image=l4)
d4=tkinter.PhotoImage(file="lado de la pantalla 4.png")
derecho4= canvas.create_image(1100,350,image=d4)

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

# MINIVAN2 DE LA IZQUIERDA CORRIENDO.   
m4=0    
def Van4():
    global ventana, canvas, m4, a
    canvas.move(a,0,5)
    if canvas.coords(a)[1]>=800:
        canvas.move(a,0,-canvas.coords(a)[1])
    
#PANTALLA DE LA IZQUIERDA CORRIENDO.
def pantallacorriendo_a4():
    global ventana , canvas 
    canvas.move(izquierdo4,0,18)
    if canvas.coords(izquierdo4)[1]>=2400:
        canvas.move(izquierdo4,0,-canvas.coords(izquierdo4)[1])

#PANTALLA DE LA DERECHA CORRIENDO.
def pantallacorriendo_b4():
    global ventana , canvas 
    canvas.move(derecho4,0,18)
    if canvas.coords(derecho4)[1]>=2400:
        canvas.move(derecho4,0,-canvas.coords(derecho4)[1])

#MINIVAN DE LA DERECHA CORRIENDO. 
def Van_b4():
    global ventana, canvas, z
    canvas.move(z,0,5)
    if canvas.coords(z)[1]>=800:
        canvas.move(z,0,-canvas.coords(z)[1])
        
#RUNNER DE LA IZQUIERDA CORRIENDO.
direccion4=1    
def Runner_a4():
    global ventana, canvas, i, direccion4
    
    canvas.move(i,-1,1)
    if canvas.coords(i)[0]<=200:
        direccion4*=-1
        canvas.move(i,30,0)
    if (canvas.coords(i)[0]>=400):
         canvas.move(i,-30,1)
         direccion4*=-1
    canvas.move(i,-5*direccion4,1)
    
    if canvas.coords(i)[1]>=800:
        canvas.move(i,0,-canvas.coords(i)[1])    

#RUNNER DE LA DERECHA CORRIENDO.
direccion4=1    
def Runner_b4():
    global ventana, canvas, q, direccion4
    
    canvas.move(q,-1,1)
    if canvas.coords(q)[0]<=1500:
        direccion4*=-1
        canvas.move(q,30,0)
    if (canvas.coords(q)[0]>=500):
         canvas.move(q,-30,1)
         direccion4*=-1
    canvas.move(q,-5*direccion4,1)
    
    if canvas.coords(q)[1]>=800:
        canvas.move(q,0,-canvas.coords(q)[1])    
        
#COMBUSTIBLE DE LA IZQUIERDA CORRIENDO.
        
def Combustible_a4():
    global ventana, canvas, z
    canvas.move(o,0,5)
    if canvas.coords(o)[1]>=800:
        canvas.move(o,0,-canvas.coords(o)[1])
 
#COMBUSTIBLE DE LA DERECHA CORRIENDO.
        
def Combustible_b4():
    global ventana, canvas, z
    canvas.move(y,0,5)
    if canvas.coords(y)[1]>=800:
        canvas.move(y,0,-canvas.coords(y)[1])

#JUGADORES CORREN CON EL TECLADO.

def keyup4(e4):
  global x,lista4
  if(e.keycode in lista4):
    lista4.pop(lista4.index(e4.keycode))

def keydown4(e4):
  global prime,segu,lista
  if not e4.keycode in lista4:
     lista4.append(e4.keycode)
   
J=tkinter.PhotoImage(file="Jugador 1.png")
prime=canvas.create_image(400,600,image=J)  

J2=tkinter.PhotoImage(file="Jugador 2.png")
segu=canvas.create_image(1250,600,image=J2)

def key4():
  global lista4, J, prime, J2, segu
  canvas.focus_set()
  if(65 in lista4):  
    canvas.move(prime,-5,0)   
  if(68 in lista4):
    canvas.move(prime,5,0)     
  if(74 in lista4):
    canvas.move(segu,-5,0)    
  if(76 in lista4):
    canvas.move(segu,5,0)
    
#FIGHTER DE LA IZQUIERDA PERSIGUE AL JUGADOR DE LA IZQ

def Fighter_a4():
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
def Fighter_b4():
   if(canvas.coords(fig)[1] < 700):
        if(canvas.coords(segu)[0]< canvas.coords(fig)[0]):
          canvas.move(fig,-2,5)
          
        elif(canvas.coords(segu)[0] > canvas.coords (fig)[0]):
           canvas.move(fig, 2,5)
        else:
           canvas.move(fig,2,5)
   else:
      canvas.move(fig,0,-700)

#manchas.
def mancha_a4():
    global ventana, canvas, m, mancha
    canvas.move(mancha,0,5)
    if canvas.coords(mancha)[1]>= 1000:
        canvas.move(mancha,0,-canvas.coords(mancha)[1])

def mancha_b4():
    global ventana, canvas, m, mancha
    canvas.move(mancha1,0,5)
    if canvas.coords(mancha1)[1]>= 1000:
        canvas.move(mancha1,0,-canvas.coords(mancha1)[1])

#CHOQUESS!

def Choques_a4():
    global canvas, explosionpng, cuentaGasolina4, explosionpng, cuentaVelocidad4

    canvas.focus_set()
    xp = canvas.coords(prime)[0]
    xa = canvas.coords (a) [0]
    xi = canvas.coords (i) [0]
    xf = canvas.coords (fi) [0]
    yp = canvas.coords(prime)[1]
    ya= canvas.coords (a) [1]
    yi = canvas.coords (i) [1]
    yf = canvas.coords (fi) [1]
    
    if (xp >= xa and xp <= xa+23 and yp >= ya and yp <= ya+46):
        canvas.move(prime,10,0)
        cuentaGasolina4=cuentaGasolina4-400
        cuentaVelocidad4=cuentaVelocidad4-20
        return True  
    if (xp + 23 >= xa and xp <= xa + 23 and ya+23>= yp and ya <= yp + 46): 
        canvas.move(prime,-5,0)      
    
    if (xp >= xi and xp <= xi+23 and yp >= yi and yp <= yi+46):
        canvas.move(prime,5,0)
        return True
    if (xp + 23 >= xi and xp <= xi + 23 and yi+23>= yp and yi <= yp + 46): 
        canvas.move(prime,-5,0) 

    if (xp >= xf and xp <= xf+23 and yp >= yf and yp <= yf+46):
        canvas.move(prime,5,0) 
        return True
    if (xp + 23 >= xf and xp <= xf + 23 and yf+23>= yp and yf <= yp + 46): 
        canvas.move(prime,-5,0)

    if canvas.coords(prime)[0]>=455 :

      cuentaGasolina4=0
      canvas.move(fi,-5,0)
      explosion=canvas.create_image(canvas.coords(prime)[0],canvas.coords(prime)[1], image=explosionpng)
      canvas.move(prime, 0, -20000)
      
    elif  canvas.coords(prime)[0]<=180:

      cuentaGasolina4=0
      canvas.move(fi,5,0)
      explosion=canvas.create_image(canvas.coords(prime)[0],canvas.coords(prime)[1], image=explosionpng)
      canvas.move(prime, 0, -20000) 


       
def Choques_b4():
    global canvas, cuentaGasolina44,cuentaVelocidad44 
    xp2 = canvas.coords(segu)[0]
    xa2 = canvas.coords (z) [0]
    xi2 = canvas.coords (q) [0]
    xf2 = canvas.coords (fig) [0]
    yp2 = canvas.coords (segu) [1]
    ya2 = canvas.coords (z) [1]
    yi2 = canvas.coords (q) [1]
    yf2 = canvas.coords (fig) [1] 
     
    if (xp2 >= xa2 and xp2 <= xa2+23 and yp2 >= ya2 and yp2 <= ya2+46):
        canvas.move(segu,10,0)
        cuentaGasolina44=cuentaGasolina44-400
        cuentaVelocidad44=cuentaVelocidad44-20

        return True  
    if (xp2 + 23 >= xa2 and xp2 <= xa2 + 23 and ya2+23>= yp2 and ya2 <= yp2 + 46): 
        canvas.move(segu,-5,0)    
    
    if (xp2 >= xi2 and xp2 <= xi2+23 and yp2 >= yi2 and yp2 <= yi2+46):
        canvas.move(segu,5,0)
        return True
    if (xp2 + 23 >= xi2 and xp2 <= xi2 + 23 and yi2+23>= yp2 and yi2 <= yp2 + 46): 
        canvas.move(segu,-5,0) 



    if (xp2 >= xf2 and xp2 <= xf2+23 and yp2 >= yf2 and yp2 <= yf2+46):
        canvas.move(segu,5,0) 
        return True
    if (xp2 + 23 >= xf2 and xp2 <= xf2 + 23 and yf2+23>= yp2 and yf2 <= yp2 + 46): 
        canvas.move(segu,-5,0)

    if canvas.coords(segu)[0]>=1280 :

      cuentaGasolina44=0
      canvas.move(fig,-5,0)
      explosion=canvas.create_image(canvas.coords(segu)[0],canvas.coords(segu)[1], image=explosionpng)
      canvas.move(segu, 0, -20000)

      
    elif  canvas.coords(segu)[0]<=1000:

      cuentaGasolina44=0
      canvas.move(fig,5,0)
      explosion=canvas.create_image(canvas.coords(segu)[0],canvas.coords(segu)[1], image=explosionpng)
      canvas.move(segu, 0, -20000)
   

ventahija.iconify()

#NIVEL 5.
lista5=[ ]
#FONDO DE LA PANTALLA 5
l5=tkinter.PhotoImage(file="lado de la pantalla 5.png")
izquierdo5=canvas.create_image(300,0,image=l5)
d5=tkinter.PhotoImage(file="lado de la pantalla 5.png")
derecho5= canvas.create_image(1100,350,image=d5) 

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

# MINIVAN2 DE LA IZQUIERDA CORRIENDO.   
m5=0    
def Van5():
    global ventana, canvas, m5, a
    canvas.move(a,0,5)
    if canvas.coords(a)[1]>=800:
        canvas.move(a,0,-canvas.coords(a)[1])
    
#PANTALLA DE LA IZQUIERDA CORRIENDO.
def pantallacorriendo_a5():
    global ventana , canvas 
    canvas.move(izquierdo5,0,19)
    if canvas.coords(izquierdo5)[1]>=2500:
        canvas.move(izquierdo5,0,-canvas.coords(izquierdo5)[1])

#PANTALLA DE LA DERECHA CORRIENDO.
def pantallacorriendo_b5():
    global ventana , canvas 
    canvas.move(derecho5,0,19)
    if canvas.coords(derecho5)[1]>=2500:
        canvas.move(derecho5,0,-canvas.coords(derecho5)[1])

#MINIVAN DE LA DERECHA CORRIENDO. 
def Van_b5():
    global ventana, canvas, z
    canvas.move(z,0,5)
    if canvas.coords(z)[1]>=800:
        canvas.move(z,0,-canvas.coords(z)[1])

#RUNNER DE LA IZQUIERDA CORRIENDO.
direccion5=1    
def Runner_a5():
    global ventana, canvas, i, direccion5
    
    canvas.move(i,-1,1)
    if canvas.coords(i)[0]<=200:
        direccion5*=-1
        canvas.move(i,30,0)

    if (canvas.coords(i)[0]>=400):
         canvas.move(i,-30,1)
         direccion5*=-1
    canvas.move(i,-5*direccion5,1)
    
    if canvas.coords(i)[1]>=800:
        canvas.move(i,0,-canvas.coords(i)[1])    

#RUNNER DE LA DERECHA CORRIENDO.
direccion5=1    
def Runner_b5():
    global ventana, canvas, q, direccion5
    
    canvas.move(q,-1,1)
    if canvas.coords(q)[0]<=1500:
        direccion5*=-1
        canvas.move(q,30,0)

    if (canvas.coords(q)[0]>=500):
         canvas.move(q,-30,1)
         direccion5*=-1
    canvas.move(q,-5*direccion5,1)
    
    if canvas.coords(q)[1]>=800:
        canvas.move(q,0,-canvas.coords(q)[1])    
        
#COMBUSTIBLE DE LA IZQUIERDA CORRIENDO.
        
def Combustible_a5():
    global ventana, canvas, z
    canvas.move(o,0,5)
    if canvas.coords(o)[1]>=800:
        canvas.move(o,0,-canvas.coords(o)[1])
 
#COMBUSTIBLE DE LA DERECHA CORRIENDO.
        
def Combustible_b5():
    global ventana, canvas, z
    canvas.move(y,0,5)
    if canvas.coords(y)[1]>=800:
        canvas.move(y,0,-canvas.coords(y)[1])

#JUGADORES CORREN CON EL TECLADO.

def keyup5(e5):
  global x,lista5
  if(e.keycode in lista5):
    lista5.pop(lista5.index(e5.keycode))

def keydown5(e5):
  global prime,segu,lista
  if not e5.keycode in lista5:
     lista5.append(e5.keycode)
   
J=tkinter.PhotoImage(file="Jugador 1.png")
prime=canvas.create_image(400,600,image=J)  

J2=tkinter.PhotoImage(file="Jugador 2.png")
segu=canvas.create_image(1250,600,image=J2)

def key5():
  global lista4, J, prime, J2, segu
  canvas.focus_set()
  if(65 in lista5):  
    canvas.move(prime,-5,0)   
  if(68 in lista5):
    canvas.move(prime,5,0)     
  if(74 in lista5):
    canvas.move(segu,-5,0)    
  if(76 in lista5):
    canvas.move(segu,5,0)
    
#FIGHTER DE LA IZQUIERDA PERSIGUE AL JUGADOR DE LA IZQ

def Fighter_a5():
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
def Fighter_b5():
   if(canvas.coords(fig)[1] < 700):
        if(canvas.coords(segu)[0]< canvas.coords(fig)[0]):
          canvas.move(fig,-2,5)
          
        elif(canvas.coords(segu)[0] > canvas.coords (fig)[0]):
           canvas.move(fig, 2,5)
        else:
           canvas.move(fig,2,5)
   else:
      canvas.move(fig,0,-700)
      
#manchas.
def mancha_a5():
    global ventana, canvas, m, mancha
    canvas.move(mancha,0,5)
    if canvas.coords(mancha)[1]>= 1000:
        canvas.move(mancha,0,-canvas.coords(mancha)[1])

def mancha_b5():
    global ventana, canvas, m, mancha
    canvas.move(mancha1,0,5)
    if canvas.coords(mancha1)[1]>= 1000:
        canvas.move(mancha1,0,-canvas.coords(mancha1)[1])
        

#CHOQUESS!

def Choques_a5():
    global canvas, explosionpng, cuentaGasolina5, explosionpng, cuentaVelocidad5

    canvas.focus_set()
    xp = canvas.coords(prime)[0]
    xa = canvas.coords (a) [0]
    xi = canvas.coords (i) [0]
    xf = canvas.coords (fi) [0]
    yp = canvas.coords(prime)[1]
    ya= canvas.coords (a) [1]
    yi = canvas.coords (i) [1]
    yf = canvas.coords (fi) [1]
    
    if (xp >= xa and xp <= xa+23 and yp >= ya and yp <= ya+46):
        canvas.move(prime,10,0)
        cuentaGasolina5=cuentaGasolina5-400
        cuentaVelocidad5=cuentaVelocidad5-20

        return True  
    if (xp + 23 >= xa and xp <= xa + 23 and ya+23>= yp and ya <= yp + 46): 
        canvas.move(prime,-5,0)     

    
    
    if (xp >= xi and xp <= xi+23 and yp >= yi and yp <= yi+46):
        canvas.move(prime,5,0)
        return True
    if (xp + 23 >= xi and xp <= xi + 23 and yi+23>= yp and yi <= yp + 46): 
        canvas.move(prime,-5,0) 



    if (xp >= xf and xp <= xf+23 and yp >= yf and yp <= yf+46):
        canvas.move(prime,5,0) 
        return True
    if (xp + 23 >= xf and xp <= xf + 23 and yf+23>= yp and yf <= yp + 46): 
        canvas.move(prime,-5,0)


    if canvas.coords(prime)[0]>=455 :

      cuentaGasolina5=0
      canvas.move(fi,-5,0)
      explosion=canvas.create_image(canvas.coords(prime)[0],canvas.coords(prime)[1], image=explosionpng)
      canvas.move(prime, 0, -20000)

      
    elif  canvas.coords(prime)[0]<=180:

      cuentaGasolina5=0
      canvas.move(fi,5,0)
      explosion=canvas.create_image(canvas.coords(prime)[0],canvas.coords(prime)[1], image=explosionpng)
      canvas.move(prime, 0, -20000)
   


       
def Choques_b5():
    global canvas, cuentaGasolina55,cuentaVelocidad55 
    xp2 = canvas.coords(segu)[0]
    xa2 = canvas.coords (z) [0]
    xi2 = canvas.coords (q) [0]
    xf2 = canvas.coords (fig) [0]
    yp2 = canvas.coords (segu) [1]
    ya2 = canvas.coords (z) [1]
    yi2 = canvas.coords (q) [1]
    yf2 = canvas.coords (fig) [1] 
     
    if (xp2 >= xa2 and xp2 <= xa2+23 and yp2 >= ya2 and yp2 <= ya2+46):
        canvas.move(segu,10,0)
        cuentaGasolina55=cuentaGasolina55-400
        cuentaVelocidad55=cuentaVelocidad55-20

        return True  
    if (xp2 + 23 >= xa2 and xp2 <= xa2 + 23 and ya2+23>= yp2 and ya2 <= yp2 + 46): 
        canvas.move(segu,-5,0)     

    
    
    if (xp2 >= xi2 and xp2 <= xi2+23 and yp2 >= yi2 and yp2 <= yi2+46):
        canvas.move(segu,5,0)
        return True
    if (xp2 + 23 >= xi2 and xp2 <= xi2 + 23 and yi2+23>= yp2 and yi2 <= yp2 + 46): 
        canvas.move(segu,-5,0) 



    if (xp2 >= xf2 and xp2 <= xf2+23 and yp2 >= yf2 and yp2 <= yf2+46):
        canvas.move(segu,5,0) 
        return True
    if (xp2 + 23 >= xf2 and xp2 <= xf2 + 23 and yf2+23>= yp2 and yf2 <= yp2 + 46): 
        canvas.move(segu,-5,0)


    if canvas.coords(segu)[0]>=1280 :

      cuentaGasolina55=0
      canvas.move(fig,-5,0)
      explosion=canvas.create_image(canvas.coords(segu)[0],canvas.coords(segu)[1], image=explosionpng)
      canvas.move(segu, 0, -20000)

      
    elif  canvas.coords(segu)[0]<=1000:

      cuentaGasolina55=0
      canvas.move(fig,5,0)
      explosion=canvas.create_image(canvas.coords(segu)[0],canvas.coords(segu)[1], image=explosionpng)
      canvas.move(segu, 0, -20000)
   

ventahija.iconify()   


#llamas de las funciones. 

cuentaGasolina1 = 2000
Gasolina1 = tkinter.StringVar()  

cuentaVelocidad1 = 0
Velocidad1 = tkinter.StringVar() 

cuentaTiempo1 = 0
Tiempo1 = tkinter.StringVar() 

cuentaDistancia1 = 0
Distancia1 = tkinter.StringVar() 

def main():
    global ku, canvas, ventahija,mi, cuentaGasolina1, Gasolina1, cuentaVelocidad1, Velocidad1, cuentaTiempo1, Tiempo1, cuentaDistancia1, Distancia1
    Van()
    Runner_a()
    Combustible_a()
    Fighter_a()
    Fighter_b()
    Choques_a()
    mancha_a()
    pantallacorriendo_a()  
    ventahija.deiconify()
    
    key()
    

    if cuentaGasolina1 > 0: 
       cuentaGasolina1 += -0.1 
       Gasolina1.set (round(cuentaGasolina1))
    else:
      return 0


    if cuentaVelocidad1 <300:
       cuentaVelocidad1 += 1
       Velocidad1.set (cuentaVelocidad1)
    else:
      cuentaVelocidad1 += 1

    if cuentaTiempo1 <= 61:
       cuentaTiempo1 += (0.01)
       Tiempo1.set (round (cuentaTiempo1))
    else:
      return 0

 
    cuentaDistancia1 += 1
    Distancia1.set (cuentaDistancia1)

    ventana.iconify() 
    ventahija.after(15,main)


cuentaGasolina11 = 2000
Gasolina11 = tkinter.StringVar() 

cuentaVelocidad11 = 0
Velocidad11 = tkinter.StringVar()  

cuentaTiempo11 = 0
Tiempo11 = tkinter.StringVar()

cuentaDistancia11 = 0
Distancia11 = tkinter.StringVar() 


def mainDere(): 
    global ku, canvas, ventahija,mi, cuentaGasolina11, Gasolina11, cuentaVelocidad11, Velocidad11, cuentaTiempo11, Tiempo11, cuentaDistancia11, Distancia11
    Van_b()
    Runner_b()
    Combustible_b()
    Fighter_b()
    Choques_b()
    mancha_b()
    pantallacorriendo_b()
    ventahija.deiconify()
    key()

    if cuentaGasolina11 > 0: 
       cuentaGasolina11 += -0.1 
       Gasolina11.set (round(cuentaGasolina11))
    else:
      return 0


    if cuentaVelocidad11 <300:
       cuentaVelocidad11 += 1
       Velocidad11.set (cuentaVelocidad11)
    else:
      cuentaVelocidad11 += 1

    if cuentaTiempo11 <= 60:
       cuentaTiempo11 += (0.01)
       Tiempo11.set (round (cuentaTiempo11))
    else:
      return 0

 
    cuentaDistancia11 += 1
    Distancia11.set (cuentaDistancia11)

    ventana.iconify() 
    ventahija.after(15,mainDere)

def primernivel():
        
    txtNombre1=tkinter.Label(ventahija,text=entradaN.get()).place(x=670,y=100)
    txtNombre2=tkinter.Label(ventahija,text=entradaN1.get()).place(x=670,y=430)

    lblGasolina1=tkinter.Label(ventahija,textvariable=Gasolina1).place(x=690, y=130)
    lblGasolina11=tkinter.Label(ventahija,textvariable=Gasolina11).place(x=690, y=460)

    lblVelocidad1=tkinter.Label(ventahija,textvariable=Velocidad1).place(x=690, y=160)
    lblVelocidad11=tkinter.Label(ventahija,textvariable=Velocidad11).place(x=690, y=488)

    lblTiempo1=tkinter.Label(ventahija,textvariable=Tiempo1).place(x=690, y=190)
    lblTiempo11=tkinter.Label(ventahija,textvariable=Tiempo11).place(x=690, y=520)

    lblDistancia1=tkinter.Label(ventahija,textvariable=Distancia1).place(x=690, y=220)
    lblDistancia11=tkinter.Label(ventahija,textvariable=Distancia11).place(x=690, y=550)

      
    canvas.delete(derecho2)
    canvas.delete(izquierdo2)
    canvas.delete(derecho3)
    canvas.delete(izquierdo3)
    canvas.delete(izquierdo4)
    canvas.delete(derecho4)
    canvas.delete(derecho5)
    canvas.delete(izquierdo5)
    mainDere()
                      
    main()
    
    


cuentaGasolina2 = 2000
Gasolina2 = tkinter.StringVar()  

cuentaVelocidad2 = 0
Velocidad2 = tkinter.StringVar() 

cuentaTiempo2 = 0
Tiempo2 = tkinter.StringVar() 

cuentaDistancia2 = 0
Distancia2 = tkinter.StringVar()


def main2():
    global ku, canvas, ventahija,mi, cuentaGasolina2, Gasolina2, cuentaVelocidad2, Velocidad2, cuentaTiempo2, Tiempo2, cuentaDistancia2, Distancia2
 
    Van2()   
    Runner_a2()    
    Combustible_a2()    
    Fighter_a2() 
    Choques_a2()
    mancha_a2()
       
    pantallacorriendo_a2()   
        
    ventahija.deiconify()
    key()

    if cuentaGasolina2 > 0: 
       cuentaGasolina2 += -0.1 
       Gasolina2.set (round(cuentaGasolina2))
    else:
      return 0


    if cuentaVelocidad2 <300:
       cuentaVelocidad2 += 1
       Velocidad2.set (cuentaVelocidad2)
    else:
      cuentaVelocidad2 += 1

    if cuentaTiempo2 <= 61:
       cuentaTiempo2 += (0.01)
       Tiempo2.set (round (cuentaTiempo2))
    else:
      return 0
 
    cuentaDistancia2 += 1
    Distancia2.set (cuentaDistancia2)

    
    ventana.iconify()
 
    ventahija.after(15,main2)



cuentaGasolina22 = 2000
Gasolina22 = tkinter.StringVar() 

cuentaVelocidad22 = 0
Velocidad22 = tkinter.StringVar()  

cuentaTiempo22 = 0
Tiempo22 = tkinter.StringVar()

cuentaDistancia22 = 0
Distancia22 = tkinter.StringVar()
def main2Dere():
    global ku, canvas, ventahija,mi, cuentaGasolina22, Gasolina22, cuentaVelocidad22, Velocidad22, cuentaTiempo22, Tiempo22, cuentaDistancia22, Distancia22
    Van_b2()
    Runner_b2()
    Combustible_b2()
    Fighter_b2()
    Choques_b2()
    mancha_b2()
    pantallacorriendo_b2()

    ventahija.deiconify()
    key()

    if cuentaGasolina22 > 0: 
       cuentaGasolina22 += -0.1 
       Gasolina22.set (round(cuentaGasolina22))
    else:
      return 0


    if cuentaVelocidad22 <300:
       cuentaVelocidad22 += 1
       Velocidad22.set (cuentaVelocidad22)
    else:
      cuentaVelocidad22 += 1

    if cuentaTiempo22 <= 60:
       cuentaTiempo22 += (0.01)
       Tiempo22.set (round (cuentaTiempo22))
    else:
      return 0

 
    cuentaDistancia22 += 1
    Distancia22.set (cuentaDistancia22)
    ventana.iconify()
 
    ventahija.after(15,main2Dere)




def segundonivel():
    
    txtNombre1=tkinter.Label(ventahija,text=entradaN.get()).place(x=670,y=100)
    txtNombre2=tkinter.Label(ventahija,text=entradaN1.get()).place(x=670,y=430)

    lblGasolina2=tkinter.Label(ventahija,textvariable=Gasolina2).place(x=690, y=130)
    lblGasolina22=tkinter.Label(ventahija,textvariable=Gasolina22).place(x=690, y=460)

    lblVelocidad2=tkinter.Label(ventahija,textvariable=Velocidad2).place(x=690, y=160)
    lblVelocidad22=tkinter.Label(ventahija,textvariable=Velocidad22).place(x=690, y=488)

    lblTiempo2=tkinter.Label(ventahija,textvariable=Tiempo2).place(x=690, y=190)
    lblTiempo22=tkinter.Label(ventahija,textvariable=Tiempo22).place(x=690, y=520)

    lblDistancia2=tkinter.Label(ventahija,textvariable=Distancia2).place(x=690, y=220)
    lblDistancia22=tkinter.Label(ventahija,textvariable=Distancia22).place(x=690, y=550)

    
    canvas.delete(derecho3)
    canvas.delete(izquierdo3)
    canvas.delete(izquierdo4)
    canvas.delete(derecho4)
    canvas.delete(izquierdo5)
    canvas.delete(derecho5)
    canvas.delete(izquierdo)
    canvas.delete(derecho)
    main2()
    main2Dere() 
    
cuentaGasolina3 = 2000
Gasolina3 = tkinter.StringVar()  

cuentaVelocidad3 = 0
Velocidad3 = tkinter.StringVar() 

cuentaTiempo3 = 0
Tiempo3 = tkinter.StringVar() 

cuentaDistancia3 = 0
Distancia3 = tkinter.StringVar() 
######################################
def main3():
    global ku, canvas, ventahija,mi, cuentaGasolina3, Gasolina3, cuentaVelocidad3, Velocidad3, cuentaTiempo3, Tiempo3, cuentaDistancia3, Distancia3
 
    Van3()
    Runner_a3()
    Combustible_a3()
    Fighter_a3()
    Choques_a3()
    mancha_a3()
    pantallacorriendo_a3()   
        
    ventahija.deiconify()
    key()

    if cuentaGasolina3 > 0: 
       cuentaGasolina3 += -0.1 
       Gasolina3.set (round(cuentaGasolina3))
    else:
      return 0

    if cuentaVelocidad3 <300:
       cuentaVelocidad3 += 1
       Velocidad3.set (cuentaVelocidad3)
    else:
      cuentaVelocidad3 += 1

    if cuentaTiempo3 <= 61:
       cuentaTiempo3 += (0.01)
       Tiempo3.set (round (cuentaTiempo3))
    else:
      return 0
 
    cuentaDistancia3 += 1
    Distancia3.set (cuentaDistancia3)
    ventana.iconify()
 
    ventahija.after(15,main3)


cuentaGasolina33 = 2000
Gasolina33 = tkinter.StringVar() 

cuentaVelocidad33 = 0
Velocidad33 = tkinter.StringVar()  

cuentaTiempo33 = 0
Tiempo33 = tkinter.StringVar()

cuentaDistancia33 = 0
Distancia33 = tkinter.StringVar() 

def main3Dere():
    global ku, canvas, ventahija,mi, cuentaGasolina33, Gasolina33, cuentaVelocidad33, Velocidad33, cuentaTiempo33, Tiempo33, cuentaDistancia33, Distancia33

    Van_b3()
    Runner_b3()
    Combustible_b3()
    Fighter_b3()
    Choques_b3()
    mancha_b3()
    pantallacorriendo_b3()

    ventahija.deiconify()
    key()

    if cuentaGasolina33 > 0: 
       cuentaGasolina33 += -0.1 
       Gasolina33.set (round(cuentaGasolina33))
    else:
      return 0
    if cuentaVelocidad33 <300:
       cuentaVelocidad33 += 1
       Velocidad33.set (cuentaVelocidad33)
    else:
      cuentaVelocidad33 += 1

    if cuentaTiempo33 <= 60:
       cuentaTiempo33 += (0.01)
       Tiempo33.set (round (cuentaTiempo33))
    else:
      return 0 
    cuentaDistancia33 += 1
    Distancia33.set (cuentaDistancia33)
    ventana.iconify()
 
    ventahija.after(15,main3Dere)

def tercernivel():
    txtNombre1=tkinter.Label(ventahija,text=entradaN.get()).place(x=670,y=100)
    txtNombre2=tkinter.Label(ventahija,text=entradaN1.get()).place(x=670,y=430)

    lblGasolina3=tkinter.Label(ventahija,textvariable=Gasolina3).place(x=690, y=130)
    lblGasolina33=tkinter.Label(ventahija,textvariable=Gasolina33).place(x=690, y=460)

    lblVelocidad3=tkinter.Label(ventahija,textvariable=Velocidad3).place(x=690, y=160)
    lblVelocidad33=tkinter.Label(ventahija,textvariable=Velocidad33).place(x=690, y=488)

    lblTiempo3=tkinter.Label(ventahija,textvariable=Tiempo3).place(x=690, y=190)
    lblTiempo33=tkinter.Label(ventahija,textvariable=Tiempo33).place(x=690, y=520)

    lblDistancia3=tkinter.Label(ventahija,textvariable=Distancia3).place(x=690, y=220)
    lblDistancia33=tkinter.Label(ventahija,textvariable=Distancia33).place(x=690, y=550)
    
    canvas.delete(izquierdo)
    canvas.delete(derecho)
    canvas.delete(izquierdo2)
    canvas.delete(derecho2) 
    canvas.delete(izquierdo4)
    canvas.delete(derecho4)
    canvas.delete(izquierdo5)
    canvas.delete(derecho5) 
       
    main3()
    main3Dere() 


cuentaGasolina4 = 2000
Gasolina4 = tkinter.StringVar()  

cuentaVelocidad4 = 0
Velocidad4 = tkinter.StringVar() 

cuentaTiempo4 = 0
Tiempo4 = tkinter.StringVar() 

cuentaDistancia4 = 0
Distancia4 = tkinter.StringVar() 

def main4():
    global ku, canvas, ventahija,mi, cuentaGasolina4, Gasolina4, cuentaVelocidad4, Velocidad4, cuentaTiempo4, Tiempo4, cuentaDistancia4, Distancia4
 
    Van4()    
    Runner_a4()    
    Combustible_a4()    
    Fighter_a4()  
    Choques_a4()
    mancha_a4()
    pantallacorriendo_a4()         
    ventahija.deiconify()
    key()

    if cuentaGasolina4 > 0: 
       cuentaGasolina4 += -0.1 
       Gasolina4.set (round(cuentaGasolina4))
    else:
      return 0


    if cuentaVelocidad4 <300:
       cuentaVelocidad4 += 1
       Velocidad4.set (cuentaVelocidad4)
    else:
      cuentaVelocidad4 += 1

    if cuentaTiempo4 <= 61:
       cuentaTiempo4 += (0.01)
       Tiempo4.set (round (cuentaTiempo4))
    else:
      return 0

    cuentaDistancia4 += 1
    Distancia4.set (cuentaDistancia4)
    
    ventana.iconify()
 
    ventahija.after(15,main4)



cuentaGasolina44 = 2000
Gasolina44 = tkinter.StringVar() 

cuentaVelocidad44 = 0
Velocidad44 = tkinter.StringVar()  

cuentaTiempo44 = 0
Tiempo44 = tkinter.StringVar()

cuentaDistancia44 = 0
Distancia44 = tkinter.StringVar() 
    

def main4Dere():
    global ku, canvas, ventahija,mi, cuentaGasolina44, Gasolina44, cuentaVelocidad44, Velocidad44, cuentaTiempo44, Tiempo44, cuentaDistancia44, Distancia44
    Van_b4()
    Runner_b4()
    Combustible_b4()
    Fighter_b4()
    Choques_b4()
    mancha_b4()
    pantallacorriendo_b4()

    ventahija.deiconify()
    key()

    if cuentaGasolina44 > 0: 
       cuentaGasolina44 += -0.1 
       Gasolina44.set (round(cuentaGasolina44))
    else:
      return 0


    if cuentaVelocidad44 <300:
       cuentaVelocidad44 += 1
       Velocidad44.set (cuentaVelocidad44)
    else:
      cuentaVelocidad44 += 1

    if cuentaTiempo44 <= 60:
       cuentaTiempo44 += (0.01)
       Tiempo44.set (round (cuentaTiempo44))
    else:
      return 0 
    cuentaDistancia44 += 1
    Distancia44.set (cuentaDistancia44)

 
    ventana.iconify()
    ventahija.after(15,main4Dere)

#################################################
def cuartonivel():
    txtNombre1=tkinter.Label(ventahija,text=entradaN.get()).place(x=670,y=100)
    txtNombre2=tkinter.Label(ventahija,text=entradaN1.get()).place(x=670,y=430)

    lblGasolina4=tkinter.Label(ventahija,textvariable=Gasolina4).place(x=690, y=130)
    lblGasolina44=tkinter.Label(ventahija,textvariable=Gasolina44).place(x=690, y=460)

    lblVelocidad4=tkinter.Label(ventahija,textvariable=Velocidad4).place(x=690, y=160)
    lblVelocidad44=tkinter.Label(ventahija,textvariable=Velocidad44).place(x=690, y=488)

    lblTiempo4=tkinter.Label(ventahija,textvariable=Tiempo4).place(x=690, y=190)
    lblTiempo44=tkinter.Label(ventahija,textvariable=Tiempo44).place(x=690, y=520)

    lblDistancia4=tkinter.Label(ventahija,textvariable=Distancia4).place(x=690, y=220)
    lblDistancia44=tkinter.Label(ventahija,textvariable=Distancia44).place(x=690, y=550)
    
    canvas.delete(derecho3)
    canvas.delete(izquierdo3)
    canvas.delete(derecho5)
    canvas.delete(izquierdo5)
    canvas.delete(izquierdo)
    canvas.delete(derecho)
    canvas.delete(izquierdo2)
    canvas.delete(derecho2)
   
    main4()
    main4Dere() 

cuentaGasolina5 = 2000
Gasolina5 = tkinter.StringVar()  

cuentaVelocidad5 = 0
Velocidad5 = tkinter.StringVar() 

cuentaTiempo5 = 0
Tiempo5 = tkinter.StringVar() 

cuentaDistancia5 = 0
Distancia5 = tkinter.StringVar() 


def main5():
    global ku, canvas, ventahija,mi, cuentaGasolina5, Gasolina5, cuentaVelocidad5, Velocidad5, cuentaTiempo5, Tiempo5, cuentaDistancia5, Distancia5
    Van5()    
    Runner_a5()    
    Combustible_a5()
    Fighter_a5()
    Choques_a5()
    mancha_a5()
      
    pantallacorriendo_a5()
    ventahija.deiconify()
    key()

    if cuentaGasolina5 > 0: 
       cuentaGasolina5 += -0.1 
       Gasolina5.set (round(cuentaGasolina5))
    else:
      return 0

    if cuentaVelocidad5 <300:
       cuentaVelocidad5 += 1
       Velocidad5.set (cuentaVelocidad5)
    else:
      cuentaVelocidad5 += 1

    if cuentaTiempo5 <= 61:
       cuentaTiempo5 += (0.01)
       Tiempo5.set (round (cuentaTiempo5))
    else:
      return 0
 
    cuentaDistancia5 += 1
    Distancia5.set (cuentaDistancia5)
    ventana.iconify()
 
    ventahija.after(15,main5)


cuentaGasolina55 = 2000
Gasolina55 = tkinter.StringVar() 

cuentaVelocidad55 = 0
Velocidad55 = tkinter.StringVar()  

cuentaTiempo55 = 0
Tiempo55 = tkinter.StringVar()

cuentaDistancia55 = 0
Distancia55 = tkinter.StringVar() 


def main5Dere():
    global ku, canvas, ventahija,mi, cuentaGasolina55, Gasolina55, cuentaVelocidad55, Velocidad55, cuentaTiempo55, Tiempo55, cuentaDistancia55,Distancia55
    Van_b5()
    Runner_b5()
    Combustible_b5()
    Fighter_b5()
    Choques_b5()
    mancha_b5()
    pantallacorriendo_b5()
    ventahija.deiconify()
    key()

    if cuentaGasolina55 > 0: 
       cuentaGasolina55 += -0.1 
       Gasolina55.set (round(cuentaGasolina55))
    else:
      return 0


    if cuentaVelocidad55 <300:
       cuentaVelocidad55 += 1
       Velocidad55.set (cuentaVelocidad55)
    else:
      cuentaVelocidad55 += 1

    if cuentaTiempo55 <= 60:
       cuentaTiempo55 += (0.01)
       Tiempo55.set (round (cuentaTiempo55))
    else:
      return 0 
    cuentaDistancia55 += 1
    Distancia55.set (cuentaDistancia55)

    ventana.iconify() 
    ventahija.after(15,main5Dere)

def quintonivel():
    txtNombre1=tkinter.Label(ventahija,text=entradaN.get()).place(x=670,y=100)
    txtNombre2=tkinter.Label(ventahija,text=entradaN1.get()).place(x=670,y=430)

    lblGasolina5=tkinter.Label(ventahija,textvariable=Gasolina5).place(x=690, y=130)
    lblGasolina55=tkinter.Label(ventahija,textvariable=Gasolina55).place(x=690, y=460)

    lblVelocidad5=tkinter.Label(ventahija,textvariable=Velocidad5).place(x=690, y=160)
    lblVelocidad55=tkinter.Label(ventahija,textvariable=Velocidad55).place(x=690, y=488)

    lblTiempo5=tkinter.Label(ventahija,textvariable=Tiempo5).place(x=690, y=190)
    lblTiempo55=tkinter.Label(ventahija,textvariable=Tiempo55).place(x=690, y=520)

    lblDistancia5=tkinter.Label(ventahija,textvariable=Distancia5).place(x=690, y=220)
    lblDistancia55=tkinter.Label(ventahija,textvariable=Distancia55).place(x=690, y=550)
    
   
    canvas.delete(derecho4)
    canvas.delete(izquierdo4)
    canvas.delete(derecho3)
    canvas.delete(izquierdo3)
    canvas.delete(derecho2)
    canvas.delete(izquierdo2)
    canvas.delete(derecho)
    canvas.delete(izquierdo)
 
      
    main5()
    main5Dere() 

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

boton2=tkinter.Button(ventana,text="2", command=segundonivel).place(x=180,y=300)
boton3=tkinter.Button(ventana,text="3", command = tercernivel).place(x=220,y=300)
boton4=tkinter.Button(ventana,text="4", command= cuartonivel).place(x=260,y=300)
boton5=tkinter.Button(ventana,text="5", command = quintonivel).place(x=300,y=300)
boton22 = tkinter.Button(ventana,text="GUARDAR PARTIDA").place(x=100,y=450)
boton33 = tkinter.Button(ventana,text="SALIR", command=ventana.destroy).place(x=100,y=500)


#TITULOS. 
Jugador1=tkinter.PhotoImage(file="JUGADOR1.png")
juga1=canvas.create_image(695,70,image=Jugador1)
Jugador2=tkinter.PhotoImage(file="JUGADOR2.png")
juga2=canvas.create_image(695,400,image=Jugador2)
gasolinapng=tkinter.PhotoImage(file="gasolina.png")
gasolin=canvas.create_image(650,140,image=gasolinapng)
gasolinapng2=tkinter.PhotoImage(file="gasolina.png")
gasolin2=canvas.create_image(650,470,image=gasolinapng2)
velocidadpng=tkinter.PhotoImage(file="velocidad.png")
veloci=canvas.create_image(650,170,image=velocidadpng)
velocidadpng2=tkinter.PhotoImage(file="velocidad.png")
veloci2=canvas.create_image(650,500,image=velocidadpng2)
tiempopng=tkinter.PhotoImage(file="tiempo.png")
tiem=canvas.create_image(650,200,image=tiempopng)
tiempopng2=tkinter.PhotoImage(file="tiempo.png")
tiem2=canvas.create_image(650,530,image=tiempopng2)
distanciapng=tkinter.PhotoImage(file="distancia.png")
dista=canvas.create_image(650,230,image=distanciapng)
distanciapng2=tkinter.PhotoImage(file="distancia.png")
dista2=canvas.create_image(650,560,image=distanciapng2)

#CARROS CARRETERA IZQUIERDA.
M=tkinter.PhotoImage(file="MiniVan.png")
a=canvas.create_image(250,40,image=M)

R=tkinter.PhotoImage(file="Runner.png")
i=canvas.create_image(200,40,image=R)

C=tkinter.PhotoImage(file="Combustible.png")
o=canvas.create_image(400,40,image=C)


F1=tkinter.PhotoImage(file="Figther.png")
fi=canvas.create_image(300,40,image=F1)
Mancha=tkinter.PhotoImage(file="mancha.png")
mancha=canvas.create_image(200,40,image=Mancha)


#CARROS CARRETERA DERECHA.
M2=tkinter.PhotoImage(file="MiniVan.png")
z=canvas.create_image(1000,40,image=M2)


R2=tkinter.PhotoImage(file="Runner.png")
q=canvas.create_image(1000,40,image=R2)


C2=tkinter.PhotoImage(file="Combustible.png")
y=canvas.create_image(1200,40,image=C2)


F2=tkinter.PhotoImage(file="Figther.png")
fig=canvas.create_image(1200,40,image=F2)

Mancha1=tkinter.PhotoImage(file="mancha.png")
mancha1=canvas.create_image(1100,40,image=Mancha1)


# Bindeamos
canvas.bind("<KeyPress>",keydown)
canvas.bind("<KeyRelease>",keyup)



canvas.pack()
ventana.mainloop()





















