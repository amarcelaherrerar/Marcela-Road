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
        canvas.move(prime,1,1)               
        return True  
    
    
    if (xp >= xi and xp <= xi+31 and yp >= ya and yp <= yi+64):
        canvas.move(prime,1,1) 
        return True

    if (xp >= xf and xp <= xf+31 and yp >= yf and yp <= yf+64):
        canvas.move(prime,1,1) 
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
        return True
    
    if (xp2 >= xi2 and xp2 <= xi2+31 and yp2 >= ya2 and yp2 <= yi2+64):
        return True

    if (xp2 >= xf2 and xp2 <= xf2+31 and yp2 >= yf2 and yp2 <= yf2+64):
        return True


#RELOJ

"""
#tiempo= StringVar()
#Label = Label(primernivel,textvariable=tiempo).place(x=38,y=120)
#labeltiem = Label(primernivel,text=":").place(x=0,y=170)
    
def Tiempo():
    global TiempoReloj
    Tiempo.set(str(TiempoReloj//60)+":"+str(TiempoReloj%60))
    TiempoReloj-=1
    primernivel.after(1000,Tiempo)
                   
    Tiempo()
-----------------------------------------------------------


entradaN11=tkinter.StringVar()

Tiempo=tkinter.Label(ventahija,textvariable=entradaN11).place(x=100,y=260)
timeclock = None 

def Tiempo():

    global timeclock
    entradaN11.set(str(timeclock//60)+":"+str(timeclock%60))
    timeclock-=1
    ventahija.after(1000,Tiempo)
                   
    Tiempo()

-----------------------------------

rel = StringVar()
                label = Label(ventananivel1,textvariable=rel,font=("ubuntu","24"),fg="white",bg="black").place(x=38,y=120)
                llabel = Label(ventananivel1,text="Para ganar",font=("ubuntu","22"),fg="white",bg="black").place(x=0,y=170)

                def timer():
                    global timeclock
                    rel.set(str(timeclock//60)+":"+str(timeclock%60))
                    timeclock-=1
                    ventananivel1.after(1000,timer)
                    
                timer()


---------------------------------


rel = tkinter.Label()
rel['text'] ='60'
rel.pack()

from time import strtime

strtime('%S')

def tic():
    rel['text'] = strftime('%S')
tic()
tic()
      def tac():
                           
          tic()
           rel.after(1000, tac)
tac() 
 -------------------------------------------       
"""        
def reloj(a,b,c):
       a=a*60
       b=b*60
       c=c
       resta=a-b-c
       return resta
 
def reloj():
       resta=0
       while (resta<=100):
           print (resta)
       resta=resta-1
       time.sleep()














### SEGUNDO NIVEL ##########################################################################################################################


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
    canvas.move(izquierdo2,0,5)
    if canvas.coords(izquierdo2)[1]>=2400:
        canvas.move(izquierdo2,0,-canvas.coords(izquierdo2)[1])

#PANTALLA DE LA DERECHA CORRIENDO.
def pantallacorriendo_b2():
    global ventana , canvas 
    canvas.move(derecho2,0,5)
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

#CHOQUESS!

def Choques_a2():
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
        canvas.move(prime,1,1)               
        return True  
    
    
    if (xp >= xi and xp <= xi+31 and yp >= ya and yp <= yi+64):
        canvas.move(prime,1,1) 
        return True

    if (xp >= xf and xp <= xf+31 and yp >= yf and yp <= yf+64):
        canvas.move(prime,1,1) 
        return True

       
def Choques_b2():
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
        return True
    
    if (xp2 >= xi2 and xp2 <= xi2+31 and yp2 >= ya2 and yp2 <= yi2+64):
        return True

    if (xp2 >= xf2 and xp2 <= xf2+31 and yp2 >= yf2 and yp2 <= yf2+64):
        return True
   
#RELOOJ
    










ventahija.iconify()
##TERCER NIVEL ############################################################################################


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
    canvas.move(izquierdo3,0,5)
    if canvas.coords(izquierdo3)[1]>=2400:
        canvas.move(izquierdo3,0,-canvas.coords(izquierdo3)[1])

#PANTALLA DE LA DERECHA CORRIENDO.
def pantallacorriendo_b3():
    global ventana , canvas 
    canvas.move(derecho3,0,5)
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

#CHOQUESS!

def Choques_a3():
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
        canvas.move(prime,1,1)               
        return True  
    
    
    if (xp >= xi and xp <= xi+31 and yp >= ya and yp <= yi+64):
        canvas.move(prime,1,1) 
        return True

    if (xp >= xf and xp <= xf+31 and yp >= yf and yp <= yf+64):
        canvas.move(prime,1,1) 
        return True

       
def Choques_b3():
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
        return True
    
    if (xp2 >= xi2 and xp2 <= xi2+31 and yp2 >= ya2 and yp2 <= yi2+64):
        return True

    if (xp2 >= xf2 and xp2 <= xf2+31 and yp2 >= yf2 and yp2 <= yf2+64):
        return True
   



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
    canvas.move(izquierdo4,0,5)
    if canvas.coords(izquierdo4)[1]>=2400:
        canvas.move(izquierdo4,0,-canvas.coords(izquierdo4)[1])

#PANTALLA DE LA DERECHA CORRIENDO.
def pantallacorriendo_b4():
    global ventana , canvas 
    canvas.move(derecho4,0,5)
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

#CHOQUESS!

def Choques_a4():
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
        canvas.move(prime,1,1)               
        return True  
    
    
    if (xp >= xi and xp <= xi+31 and yp >= ya and yp <= yi+64):
        canvas.move(prime,1,1) 
        return True

    if (xp >= xf and xp <= xf+31 and yp >= yf and yp <= yf+64):
        canvas.move(prime,1,1) 
        return True

       
def Choques_b4():
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
        return True
    
    if (xp2 >= xi2 and xp2 <= xi2+31 and yp2 >= ya2 and yp2 <= yi2+64):
        return True

    if (xp2 >= xf2 and xp2 <= xf2+31 and yp2 >= yf2 and yp2 <= yf2+64):
        return True
   

ventahija.iconify()





###################### NIVEL 5 #########################################################


lista5=[ ]


#FONDO DE LA PANTALLA 54.



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
    canvas.move(izquierdo5,0,5)
    if canvas.coords(izquierdo5)[1]>=2400:
        canvas.move(izquierdo5,0,-canvas.coords(izquierdo5)[1])

#PANTALLA DE LA DERECHA CORRIENDO.
def pantallacorriendo_b5():
    global ventana , canvas 
    canvas.move(derecho5,0,5)
    if canvas.coords(derecho5)[1]>=2400:
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

#CHOQUESS!

def Choques_a5():
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
        canvas.move(prime,1,1)               
        return True  
    
    
    if (xp >= xi and xp <= xi+31 and yp >= ya and yp <= yi+64):
        canvas.move(prime,1,1) 
        return True

    if (xp >= xf and xp <= xf+31 and yp >= yf and yp <= yf+64):
        canvas.move(prime,1,1) 
        return True

       
def Choques_b5():
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
        return True
    
    if (xp2 >= xi2 and xp2 <= xi2+31 and yp2 >= ya2 and yp2 <= yi2+64):
        return True

    if (xp2 >= xf2 and xp2 <= xf2+31 and yp2 >= yf2 and yp2 <= yf2+64):
        return True


ventahija.iconify()   


############################################################################################################################     
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
    Choques_a()
    Choques_b()
    reloj ()
                     
                           

    pantallacorriendo_a()
    pantallacorriendo_b()
        
    ventahija.deiconify()
    key()
    ventana.iconify()
 
    ventahija.after(15,main)


def primernivel():
        
    txtNombre1=tkinter.Label(ventahija,text=entradaN.get()).place(x=670,y=100)
    txtNombre2=tkinter.Label(ventahija,text=entradaN1.get()).place(x=670,y=430)


    
    



    
   
       
    canvas.delete(derecho2)
    canvas.delete(izquierdo2)
    canvas.delete(derecho3)
    canvas.delete(izquierdo3)
    canvas.delete(izquierdo4)
    canvas.delete(derecho4)
    canvas.delete(derecho5)
    canvas.delete(izquierdo5)


       
                     
    main()
    
    
def main2():
    global ku, canvas, ventahija,mi
 
    Van2()
    Van_b2()
    Runner_a2()
    Runner_b2()
    Combustible_a2()
    Combustible_b2()
    Fighter_a2()
    Fighter_b2()
    Choques_a2()
            
     
    
    Choques_b2()
  

     
    pantallacorriendo_a2()
    pantallacorriendo_b2()
        
    ventahija.deiconify()
    key()
    ventana.iconify()
 
    ventahija.after(15,main2)


def segundonivel():
    txtNombre1=tkinter.Label(ventahija,text=entradaN.get()).place(x=670,y=100)
    txtNombre2=tkinter.Label(ventahija,text=entradaN1.get()).place(x=670,y=430)
    canvas.delete(derecho3)
    canvas.delete(izquierdo3)
    canvas.delete(izquierdo4)
    canvas.delete(derecho4)
    canvas.delete(izquierdo5)
    canvas.delete(derecho5)
    canvas.delete(izquierdo)
    canvas.delete(derecho)
    main2()
    
######################################
def main3():
    global ku, canvas, ventahija,mi
 
    Van3()
    Van_b3()
    Runner_a3()
    Runner_b3()
    Combustible_a3()
    Combustible_b3()
    Fighter_a3()
    Fighter_b3()
    Choques_a3()
     
    
    Choques_b3()
  

     
    pantallacorriendo_a3()
    pantallacorriendo_b3()
        
    ventahija.deiconify()
    key()
    ventana.iconify()
 
    ventahija.after(15,main3)


def tercernivel():
    txtNombre1=tkinter.Label(ventahija,text=entradaN.get()).place(x=670,y=100)
    txtNombre2=tkinter.Label(ventahija,text=entradaN1.get()).place(x=670,y=430)
    canvas.delete(izquierdo)
    canvas.delete(derecho)
    canvas.delete(izquierdo2)
    canvas.delete(derecho2) 
    canvas.delete(izquierdo4)
    canvas.delete(derecho4)
    canvas.delete(izquierdo5)
    canvas.delete(derecho5) 
       
    main3()

###########################################

def main4():
    global ku, canvas, ventahija,mi
 
    Van4()
    Van_b4()
    Runner_a4()
    Runner_b4()
    Combustible_a4()
    Combustible_b4()
    Fighter_a4()
    Fighter_b4()
    Choques_a4()
     
    
    Choques_b4()
  

     
    pantallacorriendo_a4()
    pantallacorriendo_b4()
        
    ventahija.deiconify()
    key()
    ventana.iconify()
 
    ventahija.after(15,main4)


def cuartonivel():
    txtNombre1=tkinter.Label(ventahija,text=entradaN.get()).place(x=670,y=100)
    txtNombre2=tkinter.Label(ventahija,text=entradaN1.get()).place(x=670,y=430)
    
    canvas.delete(derecho3)
    canvas.delete(izquierdo3)
    canvas.delete(derecho5)
    canvas.delete(izquierdo5)
    canvas.delete(izquierdo)
    canvas.delete(derecho)
    canvas.delete(izquierdo2)
    canvas.delete(derecho2)
   
    main4()
##############################################

def main5():
    global ku, canvas, ventahija,mi
 
    Van5()
    Van_b5()
    Runner_a5()
    Runner_b5()
    Combustible_a5()
    Combustible_b5()
    Fighter_a5()
    Fighter_b5()
    Choques_a5()
     
    
    Choques_b5()
  

     
    pantallacorriendo_a5()
    pantallacorriendo_b5()
        
    ventahija.deiconify()
    key()
    ventana.iconify()
 
    ventahija.after(15,main5)


def quintonivel():
    txtNombre1=tkinter.Label(ventahija,text=entradaN.get()).place(x=670,y=100)
    txtNombre2=tkinter.Label(ventahija,text=entradaN1.get()).place(x=670,y=430)
    canvas.delete(derecho4)
    canvas.delete(izquierdo4)
    canvas.delete(derecho3)
    canvas.delete(izquierdo3)
    canvas.delete(derecho2)
    canvas.delete(izquierdo2)
    canvas.delete(derecho)
    canvas.delete(izquierdo)
 
    
   
    main5()

###########################################


    


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



#CARROS CARRETERA IZQUIERDA.

Jugador1=tkinter.PhotoImage(file="JUGADOR1.png")
juga1=canvas.create_image(695,70,image=Jugador1)


Jugador2=tkinter.PhotoImage(file="JUGADOR2.png")
juga2=canvas.create_image(695,400,image=Jugador2)



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





















