#Interfaz gráfica
from tkinter import *
#Conexión con el Serial
import serial

#Configuración Serial del arduino
port = 'COM7'
arduino=serial.Serial(port,9600,timeout=2)

#Estados
prim=False
seg=False
ter=False
cuar=False
org=False
dest=False
taken=False
magnet=False

def TodasFalsas():
    global prim,seg,ter,cuar
    prim=False
    seg=False
    ter=False
    cuar=False

def takefrom(x): #Formulario 1(coger desde)
    global prim
    prim=True

def takefromto(x): #Formulario 2 (llevar hasta)
    global seg
    seg=True

def taketo(x): #Formulario 3 (Transportar desde )
    global ter
    ter=True

def too(x): #Formulario 4 (hasta)
    global cuar
    cuar=True
    
def validateB1(): #Boton GO función que se llama al presionar el botón GOB1
    global prim,taken,arduino
    #Si ya hay algo cogido, no hacer nada, si no, coger la ficha de esa posición  con la instrucción (ficha*100)+15
    if prim and not taken:
        e=o1.get()
        instr= AfterInstr(e)*100
        instr=instr+15
        mensaje=str(instr)
        arduino.write(mensaje.encode())
        taken=True

def validateB2(): #Boton GO, función que se llama al presionar el botón GOB2
    #Verificar que la ficha esté cogida y el destino esté seleccionado
    global prim, seg,taken,arduino
    if prim and seg:
        f=o2.get()
        instr2= AfterInstr(f)*100
        instr2=instr2+5
        mensaje=str(instr2)
        arduino.write(mensaje.encode())
        taken=False
        TodasFalsas()

def validate2(): #Boton GO, función que se llama al presionar el botón GO3
    #Verificar que el tercero y cuarto estén seleccionados, llevar desde el origen hasta el objetivo
    global ter,cuar, arduino
    if ter and cuar:
        orig=o3.get() #Llamar a obtener y luego a llevar, obtener lo de los formularios 3 y 4 para ello
        instr=AfterInstr(orig)*100
        dest=o4.get()
        instr=instr+AfterInstr(dest)*10
        instr=instr+6
        mensaje=str(instr)
        arduino.write(mensaje.encode())
        ter=False
        cuar=False

def up(): #Flecha subir
    arduino.write("11".encode())

def down(): #Flecha bajar
    arduino.write("21".encode())

def left(): #Flecha izquierda
    arduino.write("31".encode())

def right(): #Flecha derecha
    arduino.write("41".encode())

def Magnet(): #Imán. Baja y coge la ficha de la posición donde se encuentre, si no, la baja y la suelta.
    global magnet
    if magnet:
        arduino.write("03".encode())
    else:
        arduino.write("13".encode())
    magnet= not magnet

def first(): #Ir a P1
    arduino.write(bytes(b'14'))

def second(): #Ir a P2
    arduino.write(bytes(b'24'))
    
def third(): #Ir a P3
    arduino.write("34".encode())

def hanoi(): #Es el botón que valida que exista origen y destino
    #Las fichas deben estar organizadas de mayor a menor una encima de otra, luego, se toma esa posición inicial y se hace un hanoi en el destino
    global org,dest, arduino
    if org and dest:
        orig=o5.get()
        instr=AfterInstr(orig)*100 
        desti=o6.get()
        instr= instr+AfterInstr(desti)*10
        instr= instr+7
        mensaje=str(instr)
        arduino.write(mensaje.encode())
        org=False
        dest=False
        #jugar hanoi

def origin(x):
    global org
    org=True

def destiny(x):
    global dest
    dest=True

def AfterInstr(x):
    #Método para obtener la instrucción (lo que pasaremos por serial)
    if x=="P1":
        return int(1) 
    elif x=="P2":
        return int(2)
    elif x=="P3":
        return int(3)
    else:
        return int(0)

#Crear la interfaz gráfica

Ventana=Tk()
Ventana.geometry("800x600+0+0")
Ventana.title("Grúa")

#Formularios
o1=StringVar(Ventana)
o1.set("Selecciona")
o = OptionMenu(Ventana,o1,"P1","P2","P3",command=takefrom)
o.place(x=30,y=420)

o2=StringVar(Ventana)
o2.set("Selecciona")
tph=OptionMenu(Ventana,o2,"P1","P2","P3",command=takefromto)
tph.place(x=250,y=420)

o3=StringVar(Ventana)
o3.set("Selecciona")
to= OptionMenu(Ventana,o3,"P1","P2","P3",command=taketo)
to.place(x=30,y=520)

o4=StringVar(Ventana)
o4.set("Selecciona")
h=OptionMenu(Ventana,o4,"P1","P2","P3",command=too)
h.place(x=150,y=520)

#Label Coger de:
e1=Label(Ventana,text="Coger de:",fg='black',bg='ivory1').place(x=30,y=400)
Ventana.config(bg="ivory1")

#Creando un frame naranja
miframe=Frame()
miframe.pack()
miframe.config(bg="dark orange")
miframe.config(width="800",height="400")

#Formulario del hanoi
o5=StringVar(Ventana)
o5.set("Origen")
og=OptionMenu(Ventana,o5,"P1","P2","P3",command=origin)
og.place(x=380,y= 220)

o6=StringVar(Ventana)
o6.set("Destino")
dt=OptionMenu(Ventana,o6,"P1","P2","P3",command=destiny)
dt.place(x=460,y= 220)

#Labels
e2=Label(Ventana,text="Llevar hasta",fg='black',bg='ivory1').place(x=250,y=400)

e3=Label(Ventana,text="Transportar desde,         hasta",fg='black',bg='ivory1').place(x=30,y=500)

e4=Label(Ventana,text="Ir hasta",fg="black",bg='dark orange').place(x=550,y=100)

#Creación de los botones con sus imágenes: flechas

flecharriba=PhotoImage(file="resources/flechaarriba.PNG")
ButtArr=Button(Ventana,image=flecharriba,height=110,width=110,command=up).place(x=120,y=0)

flechabajo=PhotoImage(file="resources/flechabajo.PNG")
ButtAba=Button(Ventana,image=flechabajo,height=110,width=110,command=down).place(x=120,y=230)

flechaizq=PhotoImage(file="resources/flechaizq.PNG")
ButtArr=Button(Ventana,image=flechaizq,height=110,width=110,command=left).place(x=0,y=115)

flechader=PhotoImage(file="resources/flechader.PNG")
ButtArr=Button(Ventana,image=flechader,height=110,width=110,command=right).place(x=240,y=115)

#Botón imán
ImgMagnet=PhotoImage(file="resources/rayo.PNG")
BtMagnet=Button(Ventana,image=ImgMagnet,height=110,width=110,command=Magnet).place(x=120,y=115)

#Botón Jugar Hanoi
ButtonHanoi=Button(Ventana,text="Jugar Hanoi", height=6,width=15,command=hanoi).place(x=400,y=120)

#Botones GO
ButtonGoB1=Button(Ventana,text="GO",height=1,width=2,command=validateB1).place(x=145,y=420)
ButtonGoB2=Button(Ventana,text="GO",height=1,width=2,command=validateB2).place(x=360,y=420)
ButtonGo3=Button(Ventana,text= "GO",height=1,width=2,command=validate2).place(x=260,y=520) 

#Botones para ir a la posición

ButtonP1=Button(Ventana,text= "P1",height=3,width=10,command=first).place(x=550,y=120)
ButtonP2=Button(Ventana,text= "P2",height=3,width=10,command=second).place(x=550,y=220)
ButtonP3=Button(Ventana,text= "P3",height=3,width=10,command=third).place(x=550,y=320)

#mainloop de la interfaz
Ventana.mainloop()

#Desconectar la conexión con arduino al cerrar interfaz.

arduino.close()