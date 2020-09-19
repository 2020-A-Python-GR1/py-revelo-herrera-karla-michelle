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

class Aplicacion():
    def __init__(self):
        self.inicio = tk.Tk()
        self.inicio.geometry('350x500') # anchura x altura
        self.inicio.title('')

        image2 = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/fondo.png")        
        image1 = ImageTk.PhotoImage(image2)                
        background_label = Label(self.inicio, image=image1)
        background_label.image=image1
        background_label.place(x=0, y=0, height=500, width=500)        

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
        #botonGuardar.pack()
        botonDimensiones = tk.Button(pantallaPrincipal, text='DIMENSIONES', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=12, command = dimensiones).place(x=0, y=460)
       #botonDimensiones.pack()
        botonTexto = tk.Button(pantallaPrincipal, text='TEXTO', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=10).place(x=110, y=460)
        botonEfectos = tk.Button(pantallaPrincipal, text='EFECTOS', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=10).place(x=197, y=460)      
        botonSuperpo = tk.Button(pantallaPrincipal, text='SUPERPOSICION', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=14).place(x=280, y=460)
    
def dimensiones():        
        pantallaDimensiones = tk.Toplevel()
        pantallaDimensiones.geometry('400x510') 
        pantallaDimensiones.title('')
        pantallaDimensiones.configure(bg = 'white')
        image2 = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")                
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
    evento = event.widget
    eventostr = evento.getText()
    print (evento)
    comparaciones(evento)
    
def comparaciones(evento):    
    if(evento == "!toplevel3.!button3"):
        print("corte_cuadrado")
    elif(evento == "!toplevel3.!button4"):
        print("corte1")   
    elif(evento == "!toplevel3.!button5"):
        print("corte2")
    elif(evento == "!toplevel3.!button6"):
        print("corte3")
        
    
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
    image1 = ImageTk.PhotoImage(image2)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')         
    botonAtras = tk.Button(pantallaCorte, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = pantallaCorte.destroy).place(x=0, y=0)
    botonAceptar = tk.Button(pantallaCorte, text='ACEPTAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = guardar_imagen).place(x=280, y=0)        
    corteCuadrado = tk.Button(pantallaCorte, text='CUADRADO', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = corte_cuadrado).place(x=0, y=460)    
    corte_1 = tk.Button(pantallaCorte, text='4:3', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=8, command = corte1).place(x=120, y=460)
    corte_2 = tk.Button(pantallaCorte, text='3:2', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=8, command = corte2).place(x=210, y=460)
    corte_3 = tk.Button(pantallaCorte, text='16:9', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=8, command = corte3).place(x=305, y=460)            
    pantallaCorte.bind("<Button-1>", callback)
def corte_cuadrado():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    global area_recortada 
    global box
    box = (100, 100, 400, 400)       
    area_recortada = imagen.crop(box)    
    #area_recortada.show()    
    image1 = ImageTk.PhotoImage(area_recortada)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)
    return box                    

def corte1():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    box = (50, 50, 400, 400)    
    area_recortada = imagen.crop(box)
    #img = ImageTk.PhotoImage(area_recortada)
    image1 = ImageTk.PhotoImage(area_recortada)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)       
    return box                 
    
def corte2():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    box = (200, 200, 400, 400)
    area_recortada = imagen.crop(box)
    #img = ImageTk.PhotoImage(area_recortada)
    image1 = ImageTk.PhotoImage(area_recortada)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return box                  

def corte3():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    box = (160, 160, 500, 500)
    area_recortada = imagen.crop(box)
    #img = ImageTk.PhotoImage(area_recortada)
    image1 = ImageTk.PhotoImage(area_recortada)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    return box

def guardar_imagen():
    pantallaPrincipal = tk.Toplevel()
    pantallaPrincipal.geometry('400x510') 
    pantallaPrincipal.title('')
    pantallaPrincipal.configure(bg = 'white')   
    box = corte_cuadrado()
    box = corte1()
    box = corte2()
    box = corte3()
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    if(box[0] == 100):
        area_recortada = imagen.crop(box)
        image1 = ImageTk.PhotoImage(area_recortada)
    elif(box[0] == 50):
        area_recortada = imagen.crop(box)
        image1 = ImageTk.PhotoImage(area_recortada)
    elif(box[0] == 200):
        area_recortada = imagen.crop(box)
        image1 = ImageTk.PhotoImage(area_recortada)
    elif(box[0] == 160):
        area_recortada = imagen.crop(box)
        image1 = ImageTk.PhotoImage(area_recortada)
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
    
def rotar():
    #nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("png files","*.png"),("todos los archivos","*.*")))    
    #if nombrearch!='':      
    pantallaRotar = tk.Tk()
    pantallaRotar.geometry('400x500') 
    pantallaRotar.title('')
    pantallaRotar.configure(bg = 'white')
    #fondo=PhotoImage(file= "/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")        
    #fondo.configure(height = 400, width = 400)
    #lblFondo=Label(pantallaPrincipal,image=fondo).place(x=0,y=50) #fondo 
    fontStyle = tkFont.Font(family="Arial", size=2, weight = 'bold')
    botonAtras = tk.Button(pantallaRotar, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = pantallaRotar.destroy).place(x=0, y=0)
    botonAceptar = tk.Button(pantallaRotar, text='ACEPTAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=280, y=0)
    rIzquierda = tk.Button(pantallaRotar, text='IZQUIERDA', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=8, command = izquierda).place(x=0, y=460)
    rDerecha = tk.Button(pantallaRotar, text='DERECHA', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=7, command = derecha).place(x=100, y=460)
    rHorizontal = tk.Button(pantallaRotar, text='HORIZONTAL', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=9, command = horizontal).place(x=195, y=460)
    rVertical = tk.Button(pantallaRotar, text='VERTICAL', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=8, command = vertical).place(x=305, y=460)

def izquierda():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")    
    #img = ImageTk.PhotoImage(area_recortada)
    img_rotada = imagen.transpose(Image.ROTATE_90)
    img_rotada.show()
    #panel = tk.Label(pantallaCorte, image = img)
    #panel.pack(side = "bottom", fill = "both", expand = "yes")

def derecha():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    img_rotada = imagen.transpose(Image.ROTATE_270)
    img_rotada.show()
    
def horizontal():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    img_rotada = imagen
    img_rotada.show()
    
def vertical():
    imagen = Image.open("/home/dev-16/Documentos/Universidad/Python-Revelo-Karla/py-revelo-herrera-karla-michelle/perrito.png")
    img_rotada = imagen.transpose(Image.ROTATE_180)
    img_rotada.show()
if __name__ == '__main__':
    main()
    
    
