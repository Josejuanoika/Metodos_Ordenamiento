from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import time
import random

main = Tk()
main.title("Prueba Graficos")
main.minsize(width=1100, height=600)
main.state('zoomed')


def m():
    list = []
    listx = []
    casillero = []
    ca1 = []
    ca2 = []
    ca3 = []
    ca4 = []
    ca5 = []
    capi = []

    def oscuro():
        frame.configure(bg="#424242", bd=0, relief=FLAT)
        w1.configure(bg="#424242", fg="white", highlightthickness=0)

    def claro():
        frame.configure(bg="SystemButtonFace")

    def resize(event):
        new_width = event.width
        new_height = event.height
        # print(new_width,new_height)
        w1.place(x=20, y=(new_height - 100), width=(new_width - 40), height=60)
        generar.place(x=20, y=(new_height - 35), width=80, height=25)
        reset.place(x=110, y=(new_height - 35), width=80, height=25)
        metodo.place(x=200, y=(new_height - 35), width=200, height=25)
        iniciar.place(x=410, y=(new_height - 35), width=80, height=25)
        vel.place(x=530, y=(new_height - 35), width=80, height=25)
        velmin.place(x=605, y=(new_height - 35), width=25, height=25)
        velo.place(x=630, y=(new_height - 25), width=100, height=10)
        progressbar.place(x=630, y=(new_height - 35), width=100, height=10)
        velmax.place(x=735, y=(new_height - 35), width=25, height=25)

        ex = (main.winfo_width() - (w1.get() * 10)) / 2
        for x in range(len(list)):
            listx[x] = ex
            list[x].place(x=ex, y=10)
            ex += 10

    def burbuja():
        for x in range(w1.get() - 1):
            list[x].configure(bg="blue")
            main.update()
            for y in range(x + 1, w1.get()):
                list[y].configure(bg="yellow")
                velocidad = velo.get() / 100
                time.sleep(velocidad)
                main.update()
                if int(list[x]['height']) > int(list[y]['height']):
                    list[x].configure(bg="red")
                    list[y].configure(bg="red")
                    time.sleep(velocidad)
                    main.update()
                    list[y].place(x=listx[x], y=10, width=8, height=list[y]['height'])
                    list[y].configure(bg="blue")
                    list[x].place(x=listx[y], y=10, width=8, height=list[x]['height'])
                    list[x].configure(bg="black")
                    # main.update()
                    aux = list[x]
                    list[x] = list[y]
                    list[y] = aux
                else:
                    list[y].configure(bg="black")
            list[x].configure(bg="green")
            main.update()
        list[w1.get() - 1].configure(bg="green")
        main.update()

    def bidi():
        izq = 0
        der = w1.get()
        while izq <= der:
            for x in range(izq, der - 1):
                list[x].configure(bg="blue")
                main.update()
                if int(list[x]['height']) > int(list[x + 1]['height']):
                    list[x + 1].place(x=listx[x], y=10, width=8, height=list[x + 1]['height'])
                    list[x].place(x=listx[x + 1], y=10, width=8, height=list[x]['height'])
                    aux = list[x]
                    list[x] = list[x + 1]
                    list[x + 1] = aux
                list[x].configure(bg="black")
                main.update()
            list[der - 1].configure(bg="green")
            main.update()
            der -= 1
            for x in range(der - 1, izq, -1):
                list[x].configure(bg="blue")
                main.update()
                if int(list[x]['height']) < int(list[x - 1]['height']):
                    list[x - 1].place(x=listx[x], y=10, width=8, height=list[x - 1]['height'])
                    list[x].place(x=listx[x - 1], y=10, width=8, height=list[x]['height'])
                    aux = list[x]
                    list[x] = list[x - 1]
                    list[x - 1] = aux
                list[x].configure(bg="black")
                main.update()
            list[izq].configure(bg="green")
            main.update()
            izq += 1

    def inse():
        for x in range(w1.get() - 1):
            list[x].configure(bg="blue")
            main.update()
            if int(list[x]['height']) > int(list[x + 1]['height']):
                for y in range(x + 1, 0, -1):
                    if int(list[y]['height']) < int(list[y - 1]['height']):
                        list[y - 1].place(x=listx[y], y=10, width=8, height=list[y - 1]['height'])
                        list[y].place(x=listx[y - 1], y=10, width=8, height=list[y]['height'])
                        list[y - 1].configure(bg="black")
                        list[y].configure(bg="blue")
                        main.update()
                        aux = list[y]
                        list[y] = list[y - 1]
                        list[y - 1] = aux
                    list[y].configure(bg="black")
                    list[0].configure(bg="black")
            else:
                list[x].configure(bg="black")
                main.update()
                list[x + 1].configure(bg="blue")
                main.update()
            list[x].configure(bg="black")
            main.update()
        list[w1.get() - 1].configure(bg="black")
        main.update()
        for x in range(w1.get()):
            list[x].configure(bg="green")
            main.update()

    def casi():

        def bi():
            posx = 0
            acu = 0
            for z in capi:
                izq = 0
                der = len(z)
                while izq <= der:
                    for x in range(izq, der - 1):
                        z[x].configure(bg="blue")
                        main.update()
                        if int(z[x]['height']) > int(z[x + 1]['height']):
                            z[x + 1].place(x=listx[posx], y=10, width=8, height=z[x + 1]['height'])
                            z[x].place(x=listx[posx + 1], y=10, width=8, height=z[x]['height'])
                            aux = z[x]
                            z[x] = z[x + 1]
                            z[x + 1] = aux
                        z[x].configure(bg="black")
                        main.update()
                        posx += 1
                    z[der - 1].configure(bg="green")
                    main.update()
                    der -= 1
                    for x in range(der - 1, izq, -1):
                        posx -= 1
                        z[x].configure(bg="blue")
                        main.update()
                        if int(z[x]['height']) < int(z[x - 1]['height']):
                            z[x - 1].place(x=listx[posx], y=10, width=8, height=z[x - 1]['height'])
                            z[x].place(x=listx[posx - 1], y=10, width=8, height=z[x]['height'])
                            aux = z[x]
                            z[x] = z[x - 1]
                            z[x - 1] = aux
                        z[x].configure(bg="black")
                        main.update()
                    z[izq].configure(bg="green")
                    main.update()
                    izq += 1
                acu += len(z)
                posx = acu
                print(acu)

        for x in range(w1.get()):
            list[x].place(x=-10, y=-1)
        main.update()
        for x in list:
            if int(x['height']) <= 100:
                ca1.append(x)
        capi.append(ca1)
        for x in list:
            if int(x['height']) > 100 and int(x['height']) <= 200:
                ca2.append(x)
        capi.append(ca2)
        for x in list:
            if int(x['height']) > 200 and int(x['height']) <= 300:
                ca3.append(x)
        capi.append(ca3)
        for x in list:
            if int(x['height']) > 300 and int(x['height']) <= 400:
                ca4.append(x)
        capi.append(ca4)
        for x in list:
            if int(x['height']) > 400 and int(x['height']) <= 500:
                ca5.append(x)
        capi.append(ca5)
        ex = (main.winfo_width() - (w1.get() * 10)) / 2
        anch = 0
        for x in range(len(casillero)):
            anch = (len(capi[x]) * 10)
            casillero[x].place(x=ex, y=10, width=anch, height=500)
            ex += anch
        ex = (main.winfo_width() - (w1.get() * 10)) / 2
        for y in capi:
            for x in y:
                x.place(x=ex, y=10, width=8, height=x['height'])
                ex += 10
            main.update()
        bi()

    def ini():
        iniciar.config(state=DISABLED)
        if metodo.get() == "Ordenamiento de burbuja":
            burbuja()
        elif metodo.get() == "Ordenamiento de burbuja bidirecional":
            bidi()
        elif metodo.get() == 'Ordenamiento por inserción':
            inse()
        elif metodo.get() == 'Ordenamiento por casilleros':
            casi()
        w1.config(state=NORMAL)
        generar.config(state=NORMAL)

    def generar():
        while len(list) > 0:
            list[len(list) - 1].place(x=-10, y=-1)
            list.pop()
        while len(listx) > 0:
            listx.pop()
        for x in casillero:
            x.place(x=-1000, y=2)
        while len(ca1) > 0:
            ca1[len(ca1) - 1].place(x=-10, y=-1)
            ca1.pop()

        while len(ca2) > 0:
            ca2[len(ca2) - 1].place(x=-10, y=-1)
            ca2.pop()
        while len(ca3) > 0:
            ca3[len(ca3) - 1].place(x=-10, y=-1)
            ca3.pop()
        while len(ca4) > 0:
            ca4[len(ca4) - 1].place(x=-10, y=-1)
            ca4.pop()
        while len(ca5) > 0:
            ca5[len(ca5) - 1].place(x=-10, y=-1)
            ca5.pop()
        while len(capi) > 0:
            capi.pop()
        ex = (main.winfo_width() - (w1.get() * 10)) / 2
        for x in range(w1.get()):
            listx.append(ex)
            ran = random.randrange(500) + 1
            list.append(Label(frame, text='', bg='black', height=ran))
            list[x].place(x=ex, y=10, width=8, height=ran)
            ex += 10
            generar.config(state=DISABLED)
            w1.config(state=DISABLED)
            reset.config(state=NORMAL)
            metodo.config(state=NORMAL)
            iniciar.config(state=NORMAL)

    def resetear():
        generar.config(state=NORMAL)
        iniciar.config(state=DISABLED)
        w1.config(state=NORMAL)
        while len(list) > 0:
            list[len(list) - 1].place(x=-10, y=-1)
            list.pop()
        while len(listx) > 0:
            listx.pop()
        for x in casillero:
            x.place(x=-1000, y=2)
        while len(ca1) > 0:
            ca1[len(ca1) - 1].place(x=-10, y=-1)
            ca1.pop()
        while len(ca2) > 0:
            ca2[len(ca2) - 1].place(x=-10, y=-1)
            ca2.pop()
        while len(ca3) > 0:
            ca3[len(ca3) - 1].place(x=-10, y=-1)
            ca3.pop()
        while len(ca4) > 0:
            ca4[len(ca4) - 1].place(x=-10, y=-1)
            ca4.pop()
        while len(ca5) > 0:
            ca5[len(ca5) - 1].place(x=-10, y=-1)
            ca5.pop()
        while len(capi) > 0:
            capi.pop()

    # Frame contenedor

    frame = Frame(main)
    frame.pack(fill=BOTH, expand=YES)

    # Menus Desplegables
    style = {'bg': "#102A43", 'fg': "white",
             'activebackground': "#243B53", 'activeforeground': "white"}
    menubarra = Menu(main, relief=RAISED, bd=10)
    menuarchivo = Menu(menubarra, tearoff=0, **style, relief=SOLID, bd=0)
    menuconfig = Menu(menuarchivo, tearoff=0, **style, relief=RIDGE, borderwidth='8')
    menutema = Menu(menuconfig, tearoff=0, **style)

    '''menuarchivo.config(bg = "GREEN",fg='white')
    menuconfig.configure(activebackground="#009496")
    menutema.configure(activebackground="#009496")
    menubarra.configure(bg = "GREEN",fg='white')'''

    menuarchivo.add_command(label="Guardar")
    menuarchivo.add_cascade(label="Configuracion", menu=menuconfig)
    menuconfig.add_cascade(label="Tema", menu=menutema)
    menutema.add_command(label="Tema Claro", command=claro)
    menutema.add_command(label="Tema Oscuro", command=oscuro)
    menuarchivo.add_separator()
    menuarchivo.add_command(label="Salir", command=lambda: main.destroy())
    menubarra.add_cascade(label="Weas", menu=menuarchivo)

    main.config(menu=menubarra)

    # Componentes
    # Scala Deslizante
    w1 = Scale(frame, from_=0, to=100, tickinterval=10, orient=HORIZONTAL)
    # Botones
    generar = Button(frame, text='Generar', command=generar)

    reset = Button(frame, text='Resetear', command=resetear)
    reset.config(state=DISABLED)

    metodo = Combobox(frame, values=['Ordenamiento de burbuja', 'Ordenamiento de burbuja bidirecional',
                                     'Ordenamiento por inserción', 'Ordenamiento por casilleros'])
    metodo.current(0)
    metodo.config(state=DISABLED)

    iniciar = Button(frame, text='Iniciar', command=ini)
    iniciar.config(state=DISABLED)

    vel = Label(frame, text='Velocidad:')
    velmin = Label(frame, text='X1')
    velmax = Label(frame, text='X10')

    progressbar = Label(frame, bg='red')

    def cambio(event):
        progressbar.place(width=((30 - velo.get()) * 100) / 30)
        if velo.get() > 0 and velo.get() <= 5:
            progressbar.configure(bg='red')
        elif velo.get() > 5 and velo.get() <= 15:
            progressbar.configure(bg='orange')
        elif velo.get() > 15:
            progressbar.configure(bg='green')

    velo = ttk.Scale(frame, from_=30, to=0, orient=HORIZONTAL, command=cambio)
    velo.set(0)

    # Evento cambio de tamaño de la ventana

    frame.bind("<Configure>", resize)

    band = 0
    for x in range(4):
        if band == 0:
            color = '#CDCDCD'
            band = 1
        elif band == 1:
            color = '#E1E1E1'
            band = 0
        casillero.append(Label(frame, text='', bg=color, height=50))
        casillero[x].place(x=-10, y=-2)
    casillero.append(Label(frame, text='', bg='#CDCDCD', height=50))
    casillero[x + 1].place(x=-10, y=-2)
    main.update()

    main.mainloop()

m()
