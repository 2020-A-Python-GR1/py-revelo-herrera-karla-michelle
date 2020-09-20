#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 21:56:20 2020

@author: dev-16
"""

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import sys
from tkinter import filedialog as fd
from PIL import Image, ImageChops, ImageEnhance, ImageOps, ImageColor, ImageDraw

class Aplicacion():
    def __init__(self):
        self.inicio = tk.Tk()
        self.inicio.geometry('400x510') # anchura x altura
        self.inicio.title('')

        image2 = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/fondo.png")        
        image2 = image2.resize((420, 420), Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image2)                
        background_label = Label(self.inicio, image=image1)
        background_label.image=image1
        background_label.place(x=0, y=0, height=420, width=420)        

        fontStyle = tkFont.Font(family="Arial", size=12)

        self.botonCargar = tk.Button(self.inicio, text='CARGAR IMAGEN', font=fontStyle, bg = '#22201C', fg = 'white',
                 height = 5, width=60, command = abrir_imagen).pack(side=BOTTOM)

        self.inicio.mainloop()
def main():
    mi_app = Aplicacion()
    return 0

def abrir_imagen():
        #nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("png files","*.png"),("todos los archivos","*.*")))    
        #if nombrearch!='':      
        global pantallaPrincipal
        pantallaPrincipal = tk.Toplevel()
        pantallaPrincipal.geometry('400x510') 
        pantallaPrincipal.title('')
        pantallaPrincipal.configure(bg = 'white') 
        image2 = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")                
        image2 = image2.resize((400, 410), Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image2)
        background_label = Label(pantallaPrincipal, image=image1)
        background_label.image=image1
        background_label.place(x=0, y=60, height=385, width=400)                
        fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')
        botonInicio = tk.Button(pantallaPrincipal, text='INICIO', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=10, command = pantallaPrincipal.destroy).place(x=0, y=0)       
        #botonInicio.pack()
        botonGuardar = tk.Button(pantallaPrincipal, text='GUARDAR', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=10).place(x=310, y=0)    
        botonDimensiones = tk.Button(pantallaPrincipal, text='DIMENSIONES', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=12, command = dimensiones).place(x=0, y=460)       
        botonTexto = tk.Button(pantallaPrincipal, text='TEXTO', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=8).place(x=110, y=460)
        botonEfectos = tk.Button(pantallaPrincipal, text='EFECTOS', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=10, command = efectos).place(x=187, y=460)      
        botonSuperpo = tk.Button(pantallaPrincipal, text='SUPERPOSICION', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=14, command = superposicion).place(x=280, y=460)
    
def dimensiones():        
        pantallaDimensiones = tk.Toplevel()
        pantallaDimensiones.geometry('400x510') 
        pantallaDimensiones.title('')
        pantallaDimensiones.configure(bg = 'white')
        image2 = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")                
        image2 = image2.resize((400, 410), Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image2)
        background_label = Label(pantallaDimensiones, image=image1)
        background_label.image=image1
        background_label.place(x=0, y=60, height=385, width=400)                
        fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')
        botonAtras = tk.Button(pantallaDimensiones, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=10, command= pantallaDimensiones.destroy).place(x=0, y=0)    
        botonCortar = tk.Button(pantallaDimensiones, text='CORTAR', font=fontStyle, bg = 'white', fg = 'black',
             height = 2, width=25, command = cortar).place(x=0, y=460)
        botonRotar = tk.Button(pantallaDimensiones, text='ROTAR', font=fontStyle, bg = 'white', fg = 'black',
             height = 2, width=25, command = rotar).place(x=200, y=460)    
        pantallaDimensiones.mainloop()
        
def callback(event):
    global evento
    global corte
    global imgCorte
    evento = event.widget 
    evento_string = str(evento)
    print(evento_string)
    if(evento_string == ".!toplevel3.!button3"):
        print("corte_cuadrado")
        corte = "corte_cuadrado()"
        imgCorte = corte_cuadrado()
        print(corte)
    elif(evento_string == ".!toplevel3.!button4"):
        print("corte1") 
        corte = "corte1()"
        imgCorte = corte1()
        print(corte)
    elif(evento_string == ".!toplevel3.!button5"):
        print("corte2")
        corte = "corte2()"
        imgCorte = corte2()
        print(corte)
    elif(evento_string == ".!toplevel3.!button6"):
        print("corte3")
        corte = "corte3()"
        imgCorte = corte3()
        print(corte)
    #print(type(evento_string))
    #comparaciones(evento_string)    
def callback2(event):
    print("entro al 2")
    print(corte)
    if(corte == "corte_cuadrado()"):
        guardar_imagen(imgCorte)
    elif(corte == "corte1()"):
        guardar_imagen(imgCorte)
    if(corte == "corte2()"):
        guardar_imagen(imgCorte)
    if(corte == "corte3()"):
        guardar_imagen(imgCorte)
            
def cortar():
    #nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("png files","*.png"),("todos los archivos","*.*")))    
    #if nombrearch!='':      
    global pantallaCorte 
    global corte
    global box
    pantallaCorte = tk.Toplevel()
    pantallaCorte.geometry('400x510') 
    pantallaCorte.title('')
    pantallaCorte.configure(bg = 'white')
    image2 = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")                
    image2 = image2.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image2)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')         
    botonAtras = tk.Button(pantallaCorte, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = pantallaCorte.destroy).place(x=0, y=0)
    botonAceptar = tk.Button(pantallaCorte, text='ACEPTAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=310, y=0)        
    corteCuadrado = tk.Button(pantallaCorte, text='CUADRADO', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = corte_cuadrado).place(x=0, y=460)    
    corte_1 = tk.Button(pantallaCorte, text='4:3', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = corte1).place(x=100, y=460)
    corte_2 = tk.Button(pantallaCorte, text='3:2', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = corte2).place(x=200, y=460)
    corte_3 = tk.Button(pantallaCorte, text='16:9', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11, command = corte3).place(x=300, y=460)            
    pantallaCorte.bind("<Button-1>", callback)
    #print(corte_selec)
    pantallaCorte.bind("<Button-3>", callback2)    
    
def corte_cuadrado():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    global area_recortada 
    global box
    box = (100, 100, 400, 400)       
    area_recortada = imagen.crop(box)    
    #area_recortada.show()    
    image1 = ImageTk.PhotoImage(area_recortada)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)
    return image1                    

def corte1():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    box = (50, 50, 400, 400)    
    area_recortada = imagen.crop(box)
    #img = ImageTk.PhotoImage(area_recortada)
    image1 = ImageTk.PhotoImage(area_recortada)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)       
    return image1                 
    
def corte2():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    box = (200, 200, 400, 400)
    area_recortada = imagen.crop(box)
    #img = ImageTk.PhotoImage(area_recortada)
    image1 = ImageTk.PhotoImage(area_recortada)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return image1                  

def corte3():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    box = (160, 160, 500, 500)
    area_recortada = imagen.crop(box)
    #img = ImageTk.PhotoImage(area_recortada)
    image1 = ImageTk.PhotoImage(area_recortada)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    return image1
    
def callback3(event):
    global evento
    global rotacion
    global imgCorte    
    evento = event.widget 
    evento_string = str(evento)
    print(evento_string)
    if(evento_string == ".!toplevel3.!button3"):
        print("izquierda")
        rotacion = "izquierda()"
        imgCorte = izquierda()
        print(corte)
    elif(evento_string == ".!toplevel3.!button4"):
        print("derecha") 
        rotacion = "derecha()"
        imgCorte = derecha()
        print(corte)
    elif(evento_string == ".!toplevel3.!button5"):
        print("horizontal")
        rotacion = "horizontal()"
        imgCorte = horizontal()
        print(corte)
    elif(evento_string == ".!toplevel3.!button6"):
        print("vertical")
        rotacion = "vertical()"
        imgCorte = vertical()
        print(corte)
    

def callback4(event):
    print("entro al 4")
    print(rotacion)
    if(rotacion == "izquierda()"):
        guardar_imagen(imgCorte)
    elif(rotacion == "derecha()"):
        guardar_imagen(imgCorte)
    if(rotacion == "horizontal()"):
        guardar_imagen(imgCorte)
    if(rotacion == "vertical()"):
        guardar_imagen(imgCorte)
        
def rotar():
    #nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("png files","*.png"),("todos los archivos","*.*")))    
    #if nombrearch!='':  
    global pantallaRotar    
    pantallaRotar = tk.Toplevel()
    pantallaRotar.geometry('400x510') 
    pantallaRotar.title('')
    pantallaRotar.configure(bg = 'white')
    image2 = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")                
    image2 = image2.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image2)
    background_label = Label(pantallaRotar, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')             
    botonAtras = tk.Button(pantallaRotar, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = pantallaRotar.destroy).place(x=0, y=0)
    botonAceptar = tk.Button(pantallaRotar, text='ACEPTAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=310, y=0)
    rIzquierda = tk.Button(pantallaRotar, text='IZQUIERDA', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = izquierda).place(x=0, y=460)
    rDerecha = tk.Button(pantallaRotar, text='DERECHA', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = derecha).place(x=100, y=460)
    rHorizontal = tk.Button(pantallaRotar, text='HORIZONTAL', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = horizontal).place(x=200, y=460)
    rVertical = tk.Button(pantallaRotar, text='VERTICAL', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11, command = vertical).place(x=300, y=460)
    pantallaRotar.bind("<Button-1>", callback3)
    #print(corte_selec)
    pantallaRotar.bind("<Button-3>", callback4)    

def izquierda():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")        
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    img_rotada = imagen.transpose(Image.ROTATE_90)
    image1 = ImageTk.PhotoImage(img_rotada)
    background_label = Label(pantallaRotar, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return image1                      

def derecha():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    img_rotada = imagen.transpose(Image.ROTATE_270)
    image1 = ImageTk.PhotoImage(img_rotada)
    background_label = Label(pantallaRotar, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return image1  
    
def horizontal():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    img_rotada = imagen
    image1 = ImageTk.PhotoImage(img_rotada)
    background_label = Label(pantallaRotar, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return image1  
    
def vertical():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    img_rotada = imagen.transpose(Image.ROTATE_180)
    image1 = ImageTk.PhotoImage(img_rotada)
    background_label = Label(pantallaRotar, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return image1  

def callback5(event):
    global evento
    global efecto
    global imgCorte    
    evento = event.widget 
    evento_string = str(evento)
    print(evento_string)
    if(evento_string == ".!toplevel2.!frame.!canvas.!frame.!button"):
        print("luz")
        efecto = "luz()"
        imgCorte = luz()
        print(efecto)
    elif(evento_string == ".!toplevel2.!frame.!canvas.!frame.!button2"):
        print("contraste") 
        efecto = "contraste()"
        imgCorte = contraste()
        print(efecto)
    elif(evento_string == ".!toplevel2.!frame.!canvas.!frame.!button3"):
        print("saturacion")
        efecto = "saturacion()"
        imgCorte = saturacion()
        print(efecto)
    elif(evento_string == ".!toplevel2.!frame.!canvas.!frame.!button4"):
        print("temperatura")
        efecto = "temperatura()"
        imgCorte = temperatura()
        print(efecto)
    elif(evento_string == ".!toplevel2.!frame.!canvas.!frame.!button5"):
        print("ic")
        efecto = "ic()"
        imgCorte = ic()
        print(efecto)
    elif(evento_string == ".!toplevel2.!frame.!canvas.!frame.!button6"):
        print("bn")
        efecto = "bn()"
        imgCorte = bn()
        print(efecto)
    

def callback6(event):
    print("entro al 6")
    print(efecto)
    if(efecto == "luz()"):
        guardar_imagen(imgCorte)
    elif(efecto == "contraste()"):
        guardar_imagen(imgCorte)
    elif(efecto == "saturacion()"):
        guardar_imagen(imgCorte)
    elif(efecto == "temperatura()"):
        guardar_imagen(imgCorte)
    elif(efecto == "ic()"):
        guardar_imagen(imgCorte)
    elif(efecto == "bn()"):
        guardar_imagen(imgCorte)

def efectos():
    #nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("png files","*.png"),("todos los archivos","*.*")))    
    #if nombrearch!='':  
    global pantallaEfectos 
    global canvas1
    pantallaEfectos = tk.Toplevel()
    pantallaEfectos.geometry('400x510') 
    pantallaEfectos.title('')
    pantallaEfectos.configure(bg = 'white')
    image2 = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")                
    image2 = image2.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image2)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')                 
    botonAtras = tk.Button(pantallaEfectos, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = pantallaEfectos.destroy).place(x=0, y=0)
    botonAceptar = tk.Button(pantallaEfectos, text='ACEPTAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=310, y=0)
    frame1=tk.Frame(pantallaEfectos,bg='white')
    frame1.place(x=0,y=440)
    canvas1=tk.Canvas(frame1)
    frame2=tk.Frame(canvas1,bg='white',relief='groove',bd=1,width=1230,height=430)
    scrollbar1=tk.Scrollbar(frame1,orient="horizontal",command=canvas1.xview)
    canvas1.configure(xscrollcommand=scrollbar1.set)
    scrollbar1.pack(side=BOTTOM,fill=X)
    canvas1.pack(side=BOTTOM)
    canvas1.create_window((0,0),window=frame2,anchor='nw')
    frame2.bind("<Configure>",ScrollAll)
    
    bLuz = tk.Button(frame2, text='LUZ', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11, command = luz).place(x=0, y=10)        
    bContraste = tk.Button(frame2, text='CONTRASTE', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11, command = contraste).place(x=100, y=10)
    bSaturacion = tk.Button(frame2, text='SATURACION', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=14, command = saturacion).place(x=202, y=10)
    bTemperatura = tk.Button(frame2, text='TEMPERATURA', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=14, command = temperatura).place(x=325, y=10)
    bIC = tk.Button(frame2, text='I/C', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11, command = ic).place(x=445, y=10)    
    bBN = tk.Button(frame2, text='B/N', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11, command = bn).place(x=545, y=10)    
    pantallaEfectos.bind("<Button-1>", callback5)
    #print(corte_selec)
    pantallaEfectos.bind("<Button-3>", callback6)
    
def ScrollAll(event):
    canvas1.configure(scrollregion=(0,0,650,650),width=400,height=60,bg='white')

def luz():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")    
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    imagen_efecto = ImageEnhance.Brightness(imagen).enhance(2)
    image1 = ImageTk.PhotoImage(imagen_efecto)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)       
    return image1                 
    
def contraste():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    imagen_efecto = ImageEnhance.Contrast(imagen).enhance(4)
    image1 = ImageTk.PhotoImage(imagen_efecto)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return image1                  

def saturacion():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    imagen_efecto = ImageOps.equalize(imagen)
    image1 = ImageTk.PhotoImage(imagen_efecto)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    return image1

def temperatura():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")    
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    imagen_gris = ImageOps.grayscale(imagen)
    imagen_efecto = ImageOps.colorize(imagen_gris, "black", "yellow")
    image1 = ImageTk.PhotoImage(imagen_efecto)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    return image1

def ic():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    imagen_efecto = ImageChops.invert(imagen)
    image1 = ImageTk.PhotoImage(imagen_efecto)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    return image1

def bn():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    imagen = imagen.resize((400, 410), Image.ANTIALIAS)
    imagen_efecto = ImageOps.grayscale(imagen)
    image1 = ImageTk.PhotoImage(imagen_efecto)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    return image1

def callback7(event):
    global evento
    global superp
    global imgCorte    
    evento = event.widget 
    evento_string = str(evento)
    print(evento_string)
    if(evento_string == ".!toplevel2.!button3"):
        print("s_cuadrado")
        superp = "s_cuadrado()"
        imgCorte = s_cuadrado()
        print(superp)
    elif(evento_string == ".!toplevel2.!button4"):
        print("s_ovalo") 
        superp = "s_ovalo()"
        imgCorte = s_ovalo()
        print(superp)
    elif(evento_string == ".!toplevel2.!button5"):
        print("s_triangulo")
        superp = "s_triangulo()"
        imgCorte = s_triangulo()
        print(superp)
    elif(evento_string == ".!toplevel2.!button6"):
        print("s_trianguloIn")
        superp = "s_trianguloIn()"
        imgCorte = s_trianguloIn()
        print(superp)
    elif(evento_string == ".!toplevel2.!button7"):
        print("s_circulo")
        superp = "s_circulo()"
        imgCorte = s_circulo()
        print(superp)
    elif(evento_string == ".!toplevel2.!button8"):
        print("s_rectangulo")
        superp = "s_rectangulo()"
        imgCorte = s_rectangulo()
        print(superp)
    
def callback8(event):
    print("entro al 8")
    print(superp)
    if(superp == "s_cuadrado()"):
        guardar_imagen(imgCorte)
    elif(superp == "s_ovalo()"):
        guardar_imagen(imgCorte)
    elif(superp == "s_triangulo()"):
        guardar_imagen(imgCorte)
    elif(superp == "s_trianguloIn()"):
        guardar_imagen(imgCorte)
    elif(superp == "s_circulo()"):
        guardar_imagen(imgCorte)
    elif(superp == "s_rectangulo()"):
        guardar_imagen(imgCorte)
        
def superposicion():
    #nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("png files","*.png"),("todos los archivos","*.*")))    
    #if nombrearch!='':  
    global pantallaSuperpo    
    pantallaSuperpo = tk.Toplevel()
    pantallaSuperpo.geometry('400x520') 
    pantallaSuperpo.title('')
    pantallaSuperpo.configure(bg = 'white')
    image2 = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")                
    image2 = image2.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image2)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')             
    botonAtras = tk.Button(pantallaSuperpo, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = pantallaSuperpo.destroy).place(x=0, y=0)
    botonAceptar = tk.Button(pantallaSuperpo, text='ACEPTAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=310, y=0)
   
    img = Image.open('icono_cuadrado.png')    
    img = img.resize((56, 56), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    iconoCuadrado = ImageTk.PhotoImage(img)
    bCuadrado = Button(pantallaSuperpo, font=fontStyle, bg = 'white', fg = 'black',
              height = 50, width=60, image=iconoCuadrado, 
              compound="right", command = s_cuadrado)    
    bCuadrado.image = iconoCuadrado
    bCuadrado.place(x=0, y=460)
    
    img1 = Image.open('icono_ovalo.png')    
    img1 = img1.resize((30, 40), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    iconoOvalo = ImageTk.PhotoImage(img1)
    bOvalo = tk.Button(pantallaSuperpo, font=fontStyle, bg = 'white', fg = 'black',
              height = 50, width=60, image=iconoOvalo, 
              compound="right", command = s_ovalo)
    bOvalo.image = iconoOvalo
    bOvalo.place(x=68, y=460)
    
    img2 = Image.open('icono_triangulo.png')    
    img2 = img2.resize((40, 40), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    iconoTriangulo = ImageTk.PhotoImage(img2)
    bTriangulo = tk.Button(pantallaSuperpo, font=fontStyle, bg = 'white', fg = 'black',
              height = 50, width=60, image=iconoTriangulo,
              compound="right", command = s_triangulo)
    bTriangulo.image = iconoTriangulo
    bTriangulo.place(x=136, y=460)
    
    img3 = Image.open('icono_triangulo2.jpg')    
    img3 = img3.resize((40, 40), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    iconoTriangulo2 = ImageTk.PhotoImage(img3)
    btInvertido = tk.Button(pantallaSuperpo, font=fontStyle, bg = 'white', fg = 'black',
              height = 50, width=60,  image=iconoTriangulo2, 
              compound="right", command = s_trianguloIn)
    btInvertido.image = iconoTriangulo2
    btInvertido.place(x=204, y=460)
    
    img4 = Image.open('icono_circulo.png')    
    img4 = img4.resize((40, 40), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    iconoCirculo = ImageTk.PhotoImage(img4)
    bCirculo = tk.Button(pantallaSuperpo, font=fontStyle, bg = 'white', fg = 'black',
              height = 50, width=60, image=iconoCirculo, 
              compound="right", command = s_circulo)
    bCirculo.image = iconoCirculo
    bCirculo.place(x=270, y=460)    
    
    img5 = Image.open('icono_rectangulo.jpg')    
    img5 = img5.resize((40, 30), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    iconoRectangulo = ImageTk.PhotoImage(img5)
    bRectangulo = tk.Button(pantallaSuperpo, font=fontStyle, bg = 'white', fg = 'black',
              height = 50, width=60, image=iconoRectangulo, 
              compound="right", command = s_rectangulo)
    bRectangulo.image = iconoRectangulo
    bRectangulo.place(x=336, y=460)    
    
    pantallaSuperpo.bind("<Button-1>", callback7)    
    pantallaSuperpo.bind("<Button-3>", callback8)    

def s_cuadrado():
    img = Image.open("cuadrado.jpeg")            
    img = img.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(img)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)    
    return image1 

def s_ovalo():
    img = Image.open("ovalo.jpeg")            
    img = img.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(img)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)         
    return image1 

def s_triangulo():
    img = Image.open("triangulo.jpeg")            
    img = img.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(img)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)         
    return image1 

def s_trianguloIn():
    img = Image.open("trianguloInvertido.jpeg")            
    img = img.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(img)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)    
    return image1 

def s_circulo():
    img = Image.open("circulo.jpeg")            
    img = img.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(img)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)        
    return image1     

def s_rectangulo():
    img = Image.open("rectangulo.jpeg")            
    img = img.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(img)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)           
    return image1 

def guardar_imagen(image1):
    pantallaPrincipal = tk.Toplevel()
    pantallaPrincipal.geometry('400x510') 
    pantallaPrincipal.title('')
    pantallaPrincipal.configure(bg = 'white')         
    background_label = Label(pantallaPrincipal, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')
    botonInicio = tk.Button(pantallaPrincipal, text='INICIO', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = pantallaPrincipal.destroy).place(x=0, y=0)       
    #botonInicio.pack()
    botonGuardar = tk.Button(pantallaPrincipal, text='GUARDAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=310, y=0)    
    #botonGuardar.pack()
    botonDimensiones = tk.Button(pantallaPrincipal, text='DIMENSIONES', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=12, command = dimensiones).place(x=0, y=460)
      
    botonTexto = tk.Button(pantallaPrincipal, text='TEXTO', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=110, y=460)
    botonEfectos = tk.Button(pantallaPrincipal, text='EFECTOS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=197, y=460)      
    botonSuperpo = tk.Button(pantallaPrincipal, text='SUPERPOSICION', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=14).place(x=280, y=460)


if __name__ == '__main__':
    main()
    
    
