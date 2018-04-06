from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import messagebox



firstwindow = Tk()
#Creo mi primera ventana
firstwindow.title("  Just another random GUI  ") #Titulo ventana
firstwindow.geometry("970x690")

#le añado la imagen principal a la primera ventana
imagen = PhotoImage(file="avatarM.gif")
etiqueta = Label(firstwindow, image = imagen).place(x = 370, y = 75)

#Añado los botones de la primera ventana
button1 = tk.Button(master = firstwindow, text = "  DISCLAIMER: This is my first GUI. Please understand.... :s  ", font=('Arial', 18, 'bold'), height = 3).pack(side = tk.TOP)
button2 = tk.Button(master = firstwindow, text = " I am a bad person and I do not want to try your first GUI, even if you worked so hard on it ¬¬ ", font=('Courier New', 16), height = 3, command = exit).pack(side = tk.BOTTOM)
#tk.Button(master = firstwindow, text = " I am a bad person and I do not want to try your first GUI, even if you worked so hard on it ¬¬ ", activebackground="#FF0000", activeforeground="#FF0000", bd=4, bg="#FF0000", fg="#FF0000", font=('Courier New', 16), command = exit).pack(side = tk.BOTTOM)
#Just me trying random configurations



#SEGUNDA VENTANA
def create_secondwindow():
    create_secondwindow1 = Tk()
    create_secondwindow1.geometry("370x290")
    create_secondwindow1.config(background="#FF9999")
    create_secondwindow1.title("Guys, I made it, here is the new window!!!")


# Hacer que se abra LA segunda ventana al darle al botón
button4 = tk.Button(master=firstwindow, text=" Cool! I support your effort, I´ll give you a chance! :) ", font=('Courier New', 16), command=create_secondwindow).pack(side=tk.BOTTOM)

"""
#Intentando meter un mensaje que aparezca al clickar en un botón de la nueva ventana
def mensaje ():
    tk.Button(master=create_secondwindow, text=" Click here Ill give you a surprise! ", font=('Courier New', 16, "bold"), height=3, command=exit)
    tk.Button.grid(row=370, column=70)
    msg = messagebox.showinfo("Hello Python", "Hello World")
    create_secondwindow = Button(TOP, text="Hello", command=exit)
    create_secondwindow.place(x=350, y=50)
"""

#button5 = tk.Button(master=create_secondwindow, text=" Click here Ill give you a surprise! ", font=('Courier New', 16), command=mensaje).pack(side=tk.TOP)

#tk.Button(master=create_secondwindow, text=" Ok, I´m ready to go now, but i´ll miss you! ", font=('Courier New', 16), command=exit).pack(side=tk.BOTTOM)


firstwindow.mainloop()




#Otras pruebas que he realizado
"""
# Create widges in the new window (en proceso)
label = tk.Label(Toplevel(secondwindow), text="A Label", fg='blue')
entry = tk.Entry(toplevel)
label.pack()
entry.pack()
"""

"""
#Ejemplo de widget. Scrollbar. Quiero añadirlo a mi SEGUNDA ventana (en proceso)
root = Tk()
l = Listbox(root, height=5) #nombrar lista
l.grid(column=100, row=600, sticky=(N,W,E,S)) #dimensiones?

s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview) #llamar a la barra y orientarla
s.grid(column=100, row=50, sticky=(N,S))

l['yscrollcommand'] = s.set

ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
for i in range(1,101):
    l.insert('end', 'Line %d of 100' % i)
root.mainloop()
"""





"""
#Ejemplo de widget. Country databases. Quiero añadirlo a mi SEGUNDA ventana (en proceso)
    # Initialize our country "databases":
    #  - the list of country codes (a subset anyway)
    #  - a parallel list of country names, in the same order as the country codes
    #  - a hash table mapping country code to population<
    countrycodes = (
    'ar', 'au', 'be', 'br', 'ca', 'cn', 'dk', 'fi', 'fr', 'gr', 'in', 'it', 'jp', 'mx', 'nl', 'no', 'es', 'se', 'ch')
    countrynames = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
                    'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway',
                    'Spain', \
                    'Sweden', 'Switzerland')
    cnames = StringVar(value=countrynames)
    populations = {'ar': 41000000, 'au': 21179211, 'be': 10584534, 'br': 185971537, \
                   'ca': 33148682, 'cn': 1323128240, 'dk': 5457415, 'fi': 5302000, 'fr': 64102140, 'gr': 11147000, \
                   'in': 1131043000, 'it': 59206382, 'jp': 127718000, 'mx': 106535000, 'nl': 16402414, \
                   'no': 4738085, 'es': 45116894, 'se': 9174082, 'ch': 7508700}

    def showPopulation(*args):
        idxs = lbox.curselection()
        if len(idxs) == 1:
            idx = int(idxs[0])
            code = countrycodes[idx]
            name = countrynames[idx]
            popn = populations[code]
            statusmsg.set("The population of %s (%s) is %d" % (name, code, popn))
        sentmsg.set('')

    lbox.bind('<<ListboxSelect>>', showPopulation)
    showPopulation()

"""



