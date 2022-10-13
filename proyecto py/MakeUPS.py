# MakeUPS

import tkinter as tk
from tkinter import *
from tkinter import ttk
from cProfile import label
from distutils.command.config import config
from email.mime import image
# import imp
from tkinter import*
from tkinter.font import BOLD
from turtle import heading
from Registro import*
#import pagregister


w = 1320
h = 680


class Inicio():
    def __init__(controller):

        #Raiz
        ventana2=Tk()
        ventana2.title("Desarrollador de software Scrum")
        ventana2.resizable(True, True)
        #ventana2.geometry("900x500")
        #ventana.iconbitmap("Scrum.ico")


        # ----------- CENTER FORM ------------- #
        ws = ventana2.winfo_screenwidth()
        hs = ventana2.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        ventana2.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #
        
        headerframe = tk.Frame(ventana2, highlightbackgroun='white', highlightcolor='#039900', highlightthickness=2, bg='#039900', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#039900', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='Scrum', padx=15, pady=5, bg='#ffffff', fg='#039900', font=('Zilla Slab',30, 'bold italic'), width=8)
        

        headerframe.pack()
        titleframe.pack()
        title_label.pack()
        
        titleframe.place(y=32, relx=0.5, anchor=CENTER)

         # ----------- END HEADER ------------- #

         # ----------- MENU ------------- #

        freim = tk.Frame(ventana2)
        menubar = Menu(freim)
        products = Menu(menubar)
        products.add_command(label="Inicio")
        products.add_command(label="Avances")
        products.add_command(label="Tareas")

        menubar.add_cascade(menu=products, label="Paginas")

        categories = Menu(menubar)
        categories.add_command(label="Añadir")
        categories.add_command(label="Editar")
        categories.add_command(label="Remover")

        menubar.add_cascade(menu=categories, label="Category")

        freim.pack()

        # ----------------- CAJA LATERAL ---------------- #

        def destroy_1():
            ventana2.destroy()
            paginaregistro1 () 
        
        def destroy_2():
            ventana2.destroy()
            paginaregistro1 () 

        cajalateral = tk.Frame(ventana2, highlightbackgroun='white', highlightcolor='white', highlightthickness=2, bg='#039900', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='¡Registrate Aqui!', padx=15, pady=5, bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1, command= destroy_1) #command = mainform1)

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='Inicia sesion', padx=15, pady=5, bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1, command= destroy_2)


        cajalateral.pack(side = LEFT)
        cajalateral.config(cursor='gobbler')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, relx=0.2)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, x=65)

        

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        

        ventana2.config(menu=menubar, bg="#ffffff")
        
        img_scrum = tk.PhotoImage(file="SCRUM.png")
        lbl = ttk.Label(ventana2, image=img_scrum)
        lbl.place(y=210, x=385)
        lbl.image = img_scrum
        
        def destroy_3():
            ventana2.destroy()

        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(ventana2, image=img_boton , command= destroy_3)
        boton.place(y=34, relx=0.95, anchor=CENTER)
        boton.image = img_boton

        ventana2.mainloop()

Inicio()


class Inicio2():
    def __init__(controller):

        #Raiz
        ventana2=Tk()
        ventana2.title("Desarrollador de software Scrum")
        ventana2.resizable(False, False)
        #ventana2.geometry("900x500")
        #ventana.iconbitmap("Scrum.ico")


        # ----------- CENTER FORM ------------- #
        ws = ventana2.winfo_screenwidth()
        hs = ventana2.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        ventana2.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #
        
        headerframe = tk.Frame(ventana2, highlightbackgroun='white', highlightcolor='#039900', highlightthickness=2, bg='#039900', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#039900', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='Scrum', padx=15, pady=5, bg='#ffffff', fg='#039900', font=('Zilla Slab',30, 'bold italic'), width=8)
        

        headerframe.pack()
        titleframe.pack()
        title_label.pack()
        
        titleframe.place(y=32, relx=0.5, anchor=CENTER)

         # ----------- END HEADER ------------- #

         # ----------- MENU ------------- #

        freim = tk.Frame(ventana2)
        menubar = Menu(freim)
        products = Menu(menubar)
        products.add_command(label="Inicio")
        products.add_command(label="Avances")
        products.add_command(label="Tareas")

        menubar.add_cascade(menu=products, label="Paginas")

        categories = Menu(menubar)
        categories.add_command(label="Añadir")
        categories.add_command(label="Editar")
        categories.add_command(label="Remover")

        menubar.add_cascade(menu=categories, label="Category")

        freim.pack()

        #
        

        ventana2.config(menu=menubar, bg="#ffffff")

        lbl = tk.Label(ventana2, text='Bienvenido selecciona el proyecto en el que trabajaras hoy', font=('Zilla Slab',15, 'bold italic'), fg='#039900',bg="#ffffff")
        lbl.place(y=200, x=650, anchor=CENTER)


        def destroy_1():
            ventana2.destroy()
            ScrumBoard()  

        def destroy_2():
            ventana2.destroy()
            ScrumBoard2()   

        img_Proye1 = tk.PhotoImage(file="Proyecto1.png")
        boton = ttk.Button(ventana2, image=img_Proye1, command= destroy_1)
        boton.place(x=275, y=240)
        boton.image = img_Proye1
        lbl_Proy1 = tk.Label(ventana2, text = "Proyecto 1", font = ("Times New Roman", 13), bg = "#D9D9D9").place(x = 390, y = 455)

        img_Proye2 = tk.PhotoImage(file="Proyecto2.png")
        boton2 = ttk.Button(ventana2, image=img_Proye2, command= destroy_2  )
        boton2.place(x=740, y=240)
        boton2.image = img_Proye2
        lbl_Proy2 = tk.Label(ventana2, text = "Proyecto 2", font = ("Times New Roman", 13), bg = "#D9D9D9").place(x = 835, y = 455)

        
        def destroy_3():
            ventana2.destroy()

        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(ventana2, image=img_boton , command= destroy_3)
        boton.place(y=34, relx=0.95, anchor=CENTER)
        boton.image = img_boton

        ventana2.mainloop()

Inicio2()