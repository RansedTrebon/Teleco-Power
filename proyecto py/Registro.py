import tkinter as tk
from tkinter import *
from tkinter import ttk
from cProfile import label
from distutils.command.config import config
# import imp
from tkinter import *
from email.mime import image #
from tkinter.font import BOLD
from turtle import heading
#import paglogin

w = 1320
h = 680

class paginaregistro1():
    def __init__(controller):

        #Raiz
        ventana=Tk()
        ventana.title("Registro")
        ventana.resizable(False, False)
        ventana.geometry("1320x680")
        



        #Bordes verdes
        recverde2=Frame()
        recverde2.pack(side="right", anchor="n")
        recverde2.config(bg="#039900", width=1320, height=80)

        recverde3=Frame()
        recverde3.place(x=200, y=100)
        recverde3.config(bg="#039900", width=1000, height=400)

        



        #Datos usuario
        textoregistro=Label(ventana, text = "REGISTRATE", font = ("Zilla Slab", 20)).place(x = 000, y = 50)

        correotexto=Label(ventana, text = "Nombre: ", font = ("Zilla Slab", 13)).place(x = 270, y = 145)
        correocuadro=Entry(ventana, font = ("Zilla Slab", 10), width = 40, bd = 0, bg="white").place(x = 370, y = 150)

        direcciontexto=Label(ventana, text = "Correo: ", font = ("Zilla Slab", 13)).place(x = 750, y = 145)
        direccioncuadro=Entry(ventana, font = ("Zilla Slab", 10), width = 40, bd = 0, bg="white").place(x = 850, y = 150)

        contraseñatexto=Label(ventana, text = "Codigo: ", font = ("Zilla Slab", 13)).place(x = 270, y = 230)
        contraseñacuadro=Entry(ventana, font = ("Zilla Slab", 10), width = 40, bd = 0, bg="white", show = "*").place(x = 370, y = 235)

        confirmarcontratexto=Label(ventana, text = "Confirmar\ncodigo: ", font = ("Zilla Slab", 13)).place(x = 750, y = 220)
        confirmarcontracuadro=Entry(ventana, font = ("Zilla Slab", 10), width = 40, bd = 0, bg="white", show = "*").place(x = 850, y = 235)


        #Botones
        registrarboton=Button(ventana, text = "REGISTRAR", font = ("Zilla Slab", 13), bg = "white", bd = 0, width = 15).place(x = 600, y = 335)

        iniciar=Button(ventana, text="Iniciar Sesión", font = ("Zilla Slab", 13, BOLD), bg = "white", bd = 0, width = 10,height= 1, fg = "#039900").place(x = 720, y = 430)
        iniciartexto=Label(ventana, text = "Si ya tienes cuenta ---> ", font = ("Zilla Slab", 13)).place(x = 500, y = 430)

        texto=Label(ventana, text = "Si eres un usuario no registrado digita tu correo y codigo, el administrador o la empresa te registrara dentro de poco.", font = ("Zilla Slab", 13)).place(x = 250, y = 600)
       # ventana.mainloop()

        def destroy_3():
            ventana.destroy()

        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(ventana, image=img_boton , command= destroy_3)
        boton.place(y=34, relx=0.95, anchor=CENTER)
        boton.image = img_boton



















class ScrumBoard():
    def __init__(controller):

        #Raiz
        ventana2=Tk()
        ventana2.title("Proyecto 1")
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

        # ----------------- CAJA LATERAL ---------------- #


        cajalateral = tk.Frame(ventana2, highlightbackgroun='white', highlightcolor='white', highlightthickness=2, bg='#039900', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Scrum Board', padx=15, pady=5, bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1) #command = mainform1)

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1)

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5, bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1)
        
        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5, bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1)



        cajalateral.pack(side = LEFT)
        cajalateral.config(cursor='gobbler')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, relx=0.2)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, x=65)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=92)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        

        ventana2.config(menu=menubar, bg="#000000")

        label1 = tk.Label(ventana2, text="To Do", bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1)
        label1.place(y=100, x=440, anchor=CENTER)
        label11 = tk.Label(ventana2,  font=('Zilla Slab',24), bg = "red", height= 14, width=10)
        label11.place(y=400, x=440, anchor=CENTER)

        label2 = tk.Label(ventana2, text="In Progress", bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1)
        label2.place(y=100, x=800, anchor=CENTER)
        label21 = tk.Label(ventana2,  font=('Zilla Slab',24), bg = "red", height= 14, width=10)
        label21.place(y=400, x=800, anchor=CENTER)

        label3 = tk.Label(ventana2, text="Done", bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1)
        label3.place(y=100, x=1170, anchor=CENTER)
        label31 = tk.Label(ventana2,  font=('Zilla Slab',24), bg = "red", height= 14, width=10)
        label31.place(y=400, x=1170, anchor=CENTER)

        def destroy_3():
            ventana2.destroy()

        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(ventana2, image=img_boton , command= destroy_3)
        boton.place(y=34, relx=0.95, anchor=CENTER)
        boton.image = img_boton

        ventana2.mainloop()

class ScrumBoard2():
    def __init__(controller):

        #Raiz
        ventana2=Tk()
        ventana2.title("Proyecto 2")
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

        # ----------------- CAJA LATERAL ---------------- #


        cajalateral = tk.Frame(ventana2, highlightbackgroun='white', highlightcolor='white', highlightthickness=2, bg='#039900', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Scrum Board', padx=15, pady=5, bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1) #command = mainform1)

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1)

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5, bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1)
        
        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5, bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1)



        cajalateral.pack(side = LEFT)
        cajalateral.config(cursor='gobbler')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, relx=0.2)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, x=65)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=92)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        

        ventana2.config(menu=menubar, bg="#000000")

        label1 = tk.Label(ventana2, text="To Do", bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1)
        label1.place(y=100, x=440, anchor=CENTER)
        label11 = tk.Label(ventana2,  font=('Zilla Slab',24), bg = "red", height= 14, width=10)
        label11.place(y=400, x=440, anchor=CENTER)

        label2 = tk.Label(ventana2, text="In Progress", bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1)
        label2.place(y=100, x=800, anchor=CENTER)
        label21 = tk.Label(ventana2,  font=('Zilla Slab',24), bg = "red", height= 14, width=10)
        label21.place(y=400, x=800, anchor=CENTER)

        label3 = tk.Label(ventana2, text="Done", bg='#ffffff', fg='#039900', font=('Zilla Slab',18, 'bold italic'), height= 1)
        label3.place(y=100, x=1170, anchor=CENTER)
        label31 = tk.Label(ventana2,  font=('Zilla Slab',24), bg = "red", height= 14, width=10)
        label31.place(y=400, x=1170, anchor=CENTER)

        def destroy_3():
            ventana2.destroy()

        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(ventana2, image=img_boton , command= destroy_3)
        boton.place(y=34, relx=0.95, anchor=CENTER)
        boton.image = img_boton

        ventana2.mainloop()