#PATH C:\Users\Pasqui\Desktop\Project\ to replace with your path


from tkinter import *
import time
import zipfile
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
import webbrowser
#Impostiamo la finestra principale

root = Tk()
root.geometry("800x800")
root.title("Gecko Sport")
root.iconbitmap(r'C:\Users\Pasqui\Desktop\Project\Images\Icon2.ico')
root.configure(background="black")

#Definiamo le immagini di background con le relative posizioni sullo schermo

Image_background1=Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\Picture2.png')
Image_background1 = Image_background1.resize((75,75),Image.ANTIALIAS)
Image_background1  = ImageTk.PhotoImage(Image_background1)
canvas1 = Canvas(root, width = 70 , height = 70,borderwidth=0, highlightthickness=0)
canvas1.pack()
canvas1.place(width=65,height=60, x=100, y=500)
canvas1.create_image(33,33,image = Image_background1)

Image_background2=Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\Picture3.png')
Image_background2 = Image_background2.resize((75,75),Image.ANTIALIAS)
Image_background2  = ImageTk.PhotoImage(Image_background2)
canvas2 = Canvas(root, width = 70 , height = 70,borderwidth=0, highlightthickness=0)
canvas2.pack()
canvas2.place(width=65,height=60, x=950, y=350)
canvas2.create_image(33,33,image = Image_background2)

Image_background3=Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\Picture4.png')
Image_background3 = Image_background3.resize((75,75),Image.ANTIALIAS)
Image_background3  = ImageTk.PhotoImage(Image_background3)
canvas3 = Canvas(root, width = 70 , height = 70,borderwidth=0, highlightthickness=0)
canvas3.pack()
canvas3.place(width=65,height=60, x=200, y=200)
canvas3.create_image(33,33,image = Image_background3)

Image_background4=Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\Picture5.png')
Image_background4 = Image_background4.resize((75,75),Image.ANTIALIAS)
Image_background4  = ImageTk.PhotoImage(Image_background4)
canvas4 = Canvas(root, width = 70 , height = 70,borderwidth=0, highlightthickness=0)
canvas4.pack()
canvas4.place(width=65,height=60, x=500, y=300)
canvas4.create_image(33,33,image = Image_background4)


Image_background5=Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\Picture6.png')
Image_background5 = Image_background5.resize((75,75),Image.ANTIALIAS)
Image_background5  = ImageTk.PhotoImage(Image_background5)
canvas5 = Canvas(root, width = 70 , height = 70,borderwidth=0, highlightthickness=0)
canvas5.pack()
canvas5.place(width=65,height=60, x=499, y=699)
canvas5.create_image(33,33,image = Image_background5)

Image_background6=Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\Picture7.png')
Image_background6 = Image_background6.resize((75,75),Image.ANTIALIAS)
Image_background6  = ImageTk.PhotoImage(Image_background6)
canvas6 = Canvas(root, width = 70 , height = 70,borderwidth=0, highlightthickness=0)
canvas6.pack()
canvas6.place(width=65,height=60, x=1200, y=600)
canvas6.create_image(33,33,image = Image_background6)


Image_background7=Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\Picture8.png')
Image_background7 = Image_background7.resize((75,75),Image.ANTIALIAS)
Image_background7  = ImageTk.PhotoImage(Image_background7)
canvas7 = Canvas(root, width = 70 , height = 70,borderwidth=0, highlightthickness=0)
canvas7.pack()
canvas7.place(width=65,height=60, x=1400, y=200)
canvas7.create_image(33,33,image = Image_background7)

imagelogo=Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\gecko.jpg')
imagelogo = imagelogo.resize((250,150),Image.ANTIALIAS)
imagelogo  = ImageTk.PhotoImage(imagelogo)
canvlogo = Canvas(root, width = 350 , height = 130,bg="black",borderwidth=0, highlightthickness=0)
canvlogo.pack()
canvlogo.place(width=300,height=280, x=600, y=350)
canvlogo.create_image(150,150,image = imagelogo)

#----------------------------------
#1° Frame-- è il primo riquadro in cui verranno riposti i primi widgets

frame1 = Frame(root, width=800 , height=800)
frame1.pack(side=TOP, anchor="n")
frame1.configure(background="White")
mylabel1=Label(frame1, text = "Sei un/una: ", bg="cadetblue",font=("Helvetica",12),width=33)
mylabel1.grid(row=0, column=0,padx=3, pady=3)

#Creo le enties per nome ed età e nome

e = Entry(frame1, borderwidth=2, width=33,font=("Helvetica",9))
e2 = Entry(frame1,borderwidth=2, width=33,font=("Helvetica",9))
e.grid(row=2, column=0)
e2.grid(row=3, column=0)
e.insert(0, "Scrivi qui il tuo nome: ")
e2.insert(0, "La tua età per favore: ")
global name
global age
name = e.get()
age = e2.get()

#l'età la trasformiamo in int per la verifica nella def go_on

options = ["uomo","donna"]
#Definiamo bottone Click here per dare messaggio benvenuto
def clickme():
    Hi = "Ciao " + e.get() + """ è un piacere conoscerti.
     Benvenuto\a su GECKO SPORT. Ti faremo qualche domanda per capire
     che tipo di persona sei prima di mostrarti i nostri capi sportivi.
     Clicca su CONTINUE per andare avanti"""
    myLabel = Label(frame1, text=Hi, justify="center",font=("Helvetica",9),bg="deepskyblue")
    myLabel.grid(row=4, column=0)

# definiamo bottone continua per distruggere un frame e crearne uno nuovo
def popup_eta_name():
    messagebox.showerror("Error - Read the messagge","""Nome ed età devono essere inseriti correttamente per continuare""")
def popup_outfit():
    messagebox.showerror("Error - Read the messagge","""Seleziona almeno un item del tuo outfit per continuare""")
def popup_eta_elevata():
    messagebox.showerror("Error - Read the messagge","""Apprezziamo tanto il tuo impegno ma non dovresti essere in questo mondo.""")
def popup_eta_bassa():
    messagebox.showerror("Error - Read the messagge","""Appreziamo tanto la tua precocità però non abbiamo le soluzioni giuste per te""")
i=0
#Funzione per far funzionare in maniera dinamica il tasto "Continue"
def go_on():
    global i
    i=i+1
    #produciamo nel primo frame messaggio di errore se si clicca continua senza avere il nome oppure l'età non int.
    if i==1:
        name = e.get()
        try:
            age = int(e2.get())
        except:
            age = e2.get()

        if age=='' or type(age)!=int:
            i=i-1
            popup_eta_name()
        elif age>110:
            i=i-1
            popup_eta_elevata()
        elif age<6:
            i=i-1
            popup_eta_bassa()
        elif name.strip()=='' :
            i=i-1
            popup_eta_name()
        else:
            frame1.destroy()
            frame2.pack(side=LEFT, anchor="nw")
    elif i==2:
        #var var1 ecc.. sono le variabili per fare la get della check box pantaloni, scarpe ecc..
        #per il budget gli dico se abbiamo un budget limitato ma specificandolo uguale a zero , ho un errore
        if (int(shoes.get()) + int(shirts.get()) +int(shorts.get())) == 0:
            i=i-1
            popup_outfit()
        else:
            frame2.destroy()
            frame3.destroy()
            frame4.pack(side=TOP, anchor="n")
            frame4.configure(background="black")
            print(Shirt_budg1.get())



#Definiamo Drag and drop Menu per sesso

clicksex= StringVar()
clicksex.set(options[0])
drop_sex = OptionMenu(frame1, clicksex,*options)#oppure possiamo mettere *options per prenderci la lista)
drop_sex.grid(row=1, column=0, padx=1, pady=1)
drop_sex.configure(background="cadetblue")
clicksex.get()
myButton = Button(frame1, text="CLICCAMI E COMINCIAMO", command=clickme, bg="cadetblue",font="Helvetica 10 bold")
myButton.grid(row=4, column=0, columnspan=2)

#------ Definiamo bottone continua governato dalla funzione go_on
myButton2 = Button(root,height=40  , width=166 ,text="Continue", command=go_on)
myButton2.pack(side=RIGHT, anchor=S)
img_continue = Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\Picture1.PNG')
img_continue= img_continue.resize((175,85),Image.ANTIALIAS)
img_continue = ImageTk.PhotoImage(img_continue)
myButton2.config(image=img_continue)
#---------------Frame 2
#Definiamo i widget della seconda finestra ------------------------------------

frame2 = LabelFrame(root, text ="IL TUO SPORT:", padx=10, pady=10, font=("Helvetica",10), width=300, relief=SUNKEN)
frame2.pack_propagate(0)
frame2.configure(background="white")

#Menu per selezionare sport
var4= StringVar()
clicked2= StringVar()
drop_sport = OptionMenu(frame2, clicked2,"Running")
drop_sport.grid(row=1, column=0)
drop_sport.configure(bg="cadetblue")
#sport = Checkbutton(frame3, text="Running", variable = var4, onvalue="Yes",offvalue="no", width=6, padx=2, pady=2)
clicked2.set("Running")
#sport.pack()

avviso_sport = Label(frame2, text="Attenzione: al momento soltanto il Running è supportato", font="Helvetica 7", bg="white")
avviso_sport.grid(row=4, column=0)
#Creo funzione per far comparire terzo frame insieme al secondo
def appearbudg():
    frame3.pack(side=TOP, anchor="center")
appear_budget = Button(frame2,text = "Clicca qui per specificare outfit e budget", command=appearbudg)
appear_budget.grid(row=3, column=0)
frame2.pack_forget()

#---------------Frame 3
#------------------Creo terzo frame per outfit items e budget

frame3 = LabelFrame(root, text = "ITEMS E BUDGET", padx=10, pady=10, font=("Helvetica",10),relief=SUNKEN)
frame3.pack(padx=20, pady=20)
frame3.configure(background="white")

global budget

#Opzioni abbigliamento

shoes= StringVar()
shirts= StringVar()
shorts= StringVar()

global Maglia

Maglia = Checkbutton(frame3, text="MAGLIE", variable = shirts, onvalue="1",offvalue="0", width=20, anchor="w")
Maglia.deselect()#altrimenti c'è il check per default
Maglia.grid(row=0,column=0)
Maglia.select()
global scarpe

scarpe = Checkbutton(frame3, text="SCARPE", variable = shoes, onvalue="1",offvalue="0", width=20, anchor="w")
scarpe.deselect()#altrimenti c'è il check per default
scarpe.grid(row=2,column=0)
scarpe.select()

global Pantaloni

Pantaloni = Checkbutton(frame3, text="PANTALONI", variable = shorts, onvalue="1",offvalue="0", width=20, anchor="w")
Pantaloni.deselect()#altrimenti c'è il check per default
Pantaloni.grid(row=1,column=0)
Pantaloni.select()
#Definiamo le entries per il budget


Shirt_budg1= StringVar()
budget_shirt = Entry(frame3, textvariable=Shirt_budg1, width=33, borderwidth=2,bg="silver")
budget_shirt.grid(row=0, column=1)
budget_shirt.insert(0,"Budget maglia qui(cancellami)")

Shoes_budg1= StringVar()
budget_shoes = Entry(frame3 ,textvariable = Shoes_budg1, width=33, borderwidth=2, bg="silver")
budget_shoes.grid(row=2, column=1)
budget_shoes.insert(0,"Budget scarpe qui (cancellami)")

Shorts_budg1= StringVar()

budget_shorts = Entry(frame3,textvariable=Shorts_budg1,width=33, borderwidth=2,bg="silver")
budget_shorts.grid(row=1, column=1)
budget_shorts.insert(0,"Budget pantaloni qui(cabcellami)")

budg_shoes=StringVar()
budg_shirt=StringVar()
budg_shorts=StringVar()

#Funzioni che abilitano le celle per inserire il budget se il "NO budget " non è flaggatp - al momento non funzionano
def abilita_shoes_budg():
    global budg_shoes
    if budg_shoes.get()=="1":
        budget_shoes.config(state=DISABLED)
    elif budg_shoes.get()=="0":
        budget_shoes.config(state=NORMAL)

def abilita_shirt_budg():
    global budg_shirt
    if budg_shirt.get()=="1":
        budget_shirt.config(state=DISABLED)
    elif budg_shirt.get()=="0":
        budget_shirt.config(state=NORMAL)

def abilita_short_budg():
    global budg_shorts
    if budg_shorts.get()=="1":
        budget_shorts.config(state=DISABLED)
    elif budg_shorts.get()=="0":
        budget_shorts.config(state=NORMAL)

#Definiamo i checkbutton per il NO Budget
budgetcheck_shirt = Checkbutton(frame3, text="NO BUDGET PER MAGLIE", variable = budg_shirt,command=abilita_shirt_budg, onvalue="1",offvalue="0", anchor="w", width=33,borderwidth=2,bg="silver")
budgetcheck_shirt.grid(row=0, column=2)
budgetcheck_shirt.select()

budgetcheck_shoes = Checkbutton(frame3, text="NO BUDGET PER SCARPE",  variable = budg_shoes,command=abilita_shoes_budg, onvalue="1",offvalue="0", anchor="w", width=33,borderwidth=2,bg="silver")
budgetcheck_shoes.grid(row=2, column=2)
budgetcheck_shoes.select()

budgetcheck_shorts = Checkbutton(frame3, text="NO BUDGET PER PANTALONI", variable = budg_shorts, command= abilita_short_budg,onvalue="1",offvalue="0", anchor="w", width=33,borderwidth=2,bg="silver")
budgetcheck_shorts.grid(row=1, column=2)
budgetcheck_shorts.select()


avviso_budget = Label(frame3, text="""*Ricorda di inserire il tuo budget senza caratteri.""", bg="white").grid(row=5, column=1)
frame3.pack_forget()

#Definiamo le immagini delle domande e le riproporzioniamo
#myimg1 = Image.open("C:\\Users\\Pasqui\\Pictures\\immagine.PNG")
#myimg1 = myimg1.resize((350,250),Image.ANTIALIAS)
#myimg1 = ImageTk.PhotoImage(myimg1)
frame4 = LabelFrame(root, text = "Clicca sull'immagine che più ti rappresenta quando fai sport: ", pady=20,fg="white", borderwidth=0,font="Helvetica 13 bold")
frame4.pack(side=TOP, anchor="n")
frame4.configure(background="white")
#Label_img1 = Label(frame4, text = "Ti senti più:", padx=7, pady=7,bg="white", font="Helvetica 12 bold").pack()
#Definiamo i bottoni per la prima domanda sulla ecosostenibilità
#Fissiamo che se clicco la prima immagine fisso a 1(si) la variabile sulla ecosostenibilità4g
global Eco
global Tecnico
global Eccentrico
global Social
#Calcoliamo le funzioni da utilizzare nelle immagini delle domande per far sì che esse scompaiano una volta immagazzinata la risposta
def seleziona_distruggi1():
    global Eco
    Eco="si"
    Buttons_1_quest.destroy()
    Buttons_2_quest.destroy()
    Buttons_3_quest.pack()
    Buttons_4_quest.pack()
def seleziona_distruggi2():
    global Eco
    Eco="no"
    Buttons_1_quest.destroy()
    Buttons_2_quest.destroy()
    Buttons_3_quest.pack()
    Buttons_4_quest.pack()
def seleziona_distruggi3():
    global Tecnico
    Tecnico="si"
    Buttons_3_quest.destroy()
    Buttons_4_quest.destroy()
    Buttons_5_quest.pack()
    Buttons_6_quest.pack()
def seleziona_distruggi4():
    global Tecnico
    Tecnico="no"
    Buttons_3_quest.destroy()
    Buttons_4_quest.destroy()
    Buttons_5_quest.pack()
    Buttons_6_quest.pack()
def seleziona_distruggi5():
    global Social
    Social="si"
    Buttons_5_quest.destroy()
    Buttons_6_quest.destroy()
    Buttons_7_quest.pack()
    Buttons_8_quest.pack()
def seleziona_distruggi6():
    global Social
    Social="no"
    Buttons_5_quest.destroy()
    Buttons_6_quest.destroy()
    Buttons_7_quest.pack()
    Buttons_8_quest.pack()
def seleziona_distruggi7():
    global Eccentrico
    Eccentrico="si"
    Buttons_7_quest.destroy()
    Buttons_8_quest.destroy()
    frame4.destroy()
    frame5.pack(side=TOP, anchor="n")
def seleziona_distruggi8():
    global Eccentrico
    Eccentrico="no"
    Buttons_7_quest.destroy()
    Buttons_8_quest.destroy()
    frame4.destroy()
    frame5.pack(side=TOP, anchor="n")

#Definisco i bottoni contententi anche le immagini che esprimono il concetto che racchiude la variabile cluster
Buttons_1_quest= Button(frame4,height= 300, width=300, bg = "white",padx=30, pady=30,command=seleziona_distruggi1)
img_eco = Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\Eco.png')
img_eco= img_eco.resize((300,300),Image.ANTIALIAS)
img_eco = ImageTk.PhotoImage(img_eco)
Buttons_1_quest.config(image=img_eco)
Buttons_1_quest.pack()

Buttons_2_quest=Button(frame4, height= 300, width=300, bg = "white",padx=10, pady=10, command=seleziona_distruggi2)
img_no_eco = Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\No_eco.png')
img_no_eco= img_no_eco.resize((300,300),Image.ANTIALIAS)
img_no_eco = ImageTk.PhotoImage(img_no_eco)
Buttons_2_quest.config(image=img_no_eco)
Buttons_2_quest.pack()

Buttons_3_quest=Button(frame4, height= 300, width=300, bg = "white",padx=10, pady=10,command=seleziona_distruggi3 )
img_tecnico = Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\Tecnico.png')
img_tecnico= img_tecnico.resize((300,300),Image.ANTIALIAS)
img_tecnico = ImageTk.PhotoImage(img_tecnico)
Buttons_3_quest.config(image=img_tecnico)


Buttons_4_quest=Button(frame4, height= 300, width=300, bg = "white",padx=10, pady=10,command=seleziona_distruggi4 )
img_notecnico = Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\No_tecnico.png')
img_notecnico= img_notecnico.resize((300,300),Image.ANTIALIAS)
img_notecnico = ImageTk.PhotoImage(img_notecnico)
Buttons_4_quest.config(image=img_notecnico)


Buttons_5_quest=Button(frame4, height= 300, width=300, bg = "white",padx=10, pady=10,command=seleziona_distruggi5)
img_social = Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\Social.png')
img_social= img_social.resize((300,300),Image.ANTIALIAS)
img_social = ImageTk.PhotoImage(img_social)
Buttons_5_quest.config(image=img_social)


Buttons_6_quest=Button(frame4, height= 300, width=300, bg = "white",padx=10, pady=10,command=seleziona_distruggi6)
img_nosocial = Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\No_social.png')
img_nosocial= img_nosocial.resize((300,300),Image.ANTIALIAS)
img_nosocial = ImageTk.PhotoImage(img_nosocial)
Buttons_6_quest.config(image=img_nosocial)

Buttons_7_quest=Button(frame4, height= 300, width=300, bg = "white",padx=10, pady=10,command=seleziona_distruggi7)
img_ecc = Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\Ecc.png')
img_ecc= img_ecc.resize((300,300),Image.ANTIALIAS)
img_ecc = ImageTk.PhotoImage(img_ecc)
Buttons_7_quest.config(image=img_ecc)


Buttons_8_quest=Button(frame4, height= 300, width=300, bg = "white",padx=10, pady=10,command=seleziona_distruggi8)
img_noecc = Image.open(r'C:\Users\Pasqui\Desktop\Project\Images\No_ecc.png')
img_noecc= img_noecc.resize((300,300),Image.ANTIALIAS)
img_noecc = ImageTk.PhotoImage(img_noecc)
Buttons_8_quest.config(image=img_noecc)

frame4.pack_forget()

#----------------------------------Definiamo frame 5
frame5 = LabelFrame(root, text = "Cominciamo: ",font="Helvetica 13 bold")
frame5.pack(side=TOP, anchor="n")
frame5.configure(background="white")

Label_last_frame = Label(frame5, text = """Grazie per il tuo tempo e per avere risposto alle nostre domande. Ti basterà cliccare il pulsante sotto per cominciare! \n\n\n\n""",bg="white", padx=2, pady=2, font=("Helvetica",12)).pack()
#stagiliamo connessione al db
conn = sqlite3.connect('DB_unificato_v1.db')
c = conn.cursor()
#Creiamo le liste vuote che verranno riempite con le immagini dopo la query
list_shirt_id=[]
list_shirt_name=[]
list_shirt_brand=[]
list_shirt_colour=[]
list_shirt_price=[]
list_shirt_store=[]
list_shirt_url=[]

list_shorts_id=[]
list_shorts_name=[]
list_shorts_brand=[]
list_shorts_colour=[]
list_shorts_price=[]
list_shorts_store=[]
list_shorts_url=[]

list_shoes_id=[]
list_shoes_name=[]
list_shoes_brand=[]
list_shoes_colour=[]
list_shoes_price=[]
list_shoes_store=[]
list_shoes_url=[]

tip_frame1=''
tip_frame2=''
tip_frame3=''

URL_shirt = ""
URL_shorts = ""
URL_shoes = ""

elem = 0
elem2 = 0
elem3 = 0
#Creiamo la funzione che in un'unica finestra crea 3 frame, uno per maglia, pantaloni e scarpe ed inserisce le immagini all'interno dopo aver fatto query sql
def genera_output():
    global window_new
    window_new = Toplevel()
    window_new.geometry('1800x1800')
    window_new.title('Outfit')
    window_new.configure(background="DodgerBlue3")
    if int(shirts.get())==1:
        # le 3 righe sotto permettono di  ricominciare da zero a generare outpout se chiudiamo la finestra e la riapriamo - dimentica il passato
        global elem
        elem = 0
        global frame_shirt
        frame_shirt = LabelFrame(window_new, text="Maglie scelte per te",width=1300 , height=230)
        frame_shirt.pack_propagate(0)
        frame_shirt.pack(side=TOP, anchor ="nw")
        frame_shirt.configure(background="White")
        tip_frame2="maglia"
        #Facciamo la GET del SEX e poi la query SQL con placeholder per filtare il DB in base alle risposte
#2 Query: una se il budget è presente e l'altra se il budget non è presente
        if budg_shirt.get()=="1" :
            print("sono nel non prezzo")
            for row in c.execute("""SELECT *
            FROM Db_unificato_v1
            where Sex = ? and tipo = ? and Ecologico=? and Tecnicità=? and Socialità=? and Eccentricità=?
            order by RANDOM()
            limit 10 """,
            (clicksex.get(), tip_frame2, Eco, Tecnico, Social, Eccentrico,)):
                list_shirt_id.append(row[0])
                list_shirt_name.append(row[2].upper())
                list_shirt_brand.append(row[3].upper())
                list_shirt_colour.append(row[4])
                list_shirt_price.append(row[8])
                list_shirt_store.append(row[9].upper())
                list_shirt_url.append(row[1])
        else:
            print("sono entrato qui")
            for row in c.execute("""SELECT *
            FROM Db_unificato_v1
            where Sex = ? and tipo = ? and Ecologico=? and Tecnicità=? and Socialità=? and Eccentricità=? and Price<?
            order by RANDOM()
            limit 10 """,
            (clicksex.get(), tip_frame2, Eco, Tecnico, Social, Eccentrico, float(Shirt_budg1.get()),)):
                list_shirt_id.append(row[0])
                list_shirt_name.append(row[2].upper())
                list_shirt_brand.append(row[3].upper())
                list_shirt_colour.append(row[4])
                list_shirt_price.append(row[8])
                list_shirt_store.append(row[9].upper())
                list_shirt_url.append(row[1])

#Definiamo un messaggio se la query non restituisce valori
        if list_shirt_id==[]:
            Mess_no_shirt=Label(frame_shirt, text="Ci dispiace ma non ci sono maglie in base alle tue caratteristiche", bg="white", font="Helvetica 14 bold")
            Mess_no_shirt.pack(side=TOP, anchor="s")
#Altrimenti generiamo l'immagine
        else:
            inflist1= ("img_"+list_shirt_id[0]+".jpg")
            #mettere img_shirt come global altrimenti nonn funziona
            global img_shirt
            try:
                img_shirt  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist1}').resize((100,100),Image.ANTIALIAS))
            except:
                inflist1= ("img_img"+list_shirt_id[0]+".jpg")
                img_shirt  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist1}').resize((100,100),Image.ANTIALIAS))
            button_forward_shirt = Button(frame_shirt, text="Next", fg="red",command=forward_shirts)
            button_forward_shirt.pack(side=RIGHT, anchor="ne")

            button_backward_shirt = Button(frame_shirt, text="Back", fg="red", command=back_shirts)
            button_backward_shirt.pack(side=RIGHT, anchor="ne")

#occore mettere canvasshirt come global altrimenti poi non possiamo dimenticarla quando generiamo nuova immagine
            global canvasshirt
            canvasshirt = Canvas(frame_shirt, width = 200 , height = 200,borderwidth=1, highlightthickness=1,bg="white")
            canvasshirt.pack(side=LEFT, anchor="nw")
            canvasshirt.create_image(90,90,image = img_shirt)
            #Definiamo le caratteristiche del prodotto
            global characteristics_shirt
            characteristics_shirt = Label(frame_shirt, text= "La 1° maglia che ti proponiamo è la '" + list_shirt_name[0] +"' della " + list_shirt_brand[0] + " disponibile nel colore " + list_shirt_colour[0] +".\n\n\nPREZZO: €"+str(list_shirt_price[0]) + " \nSTORE: " +list_shirt_store[0], justify= CENTER, padx=10, pady=20, bg="white",font="Helvetica 9 bold")
            characteristics_shirt.pack(side=TOP, anchor="n")
            global URL_shirt
            URL_shirt = list_shirt_url[0]


    if int(shorts.get())==1:
        global elem2
        elem2 = 0
        global frame_shorts
        frame_shorts = LabelFrame(window_new, text="Pantaloni scelte per te",width=1300 , height=230)
        frame_shorts.pack_propagate(0)
        frame_shorts.pack(side=TOP, anchor ="nw")
        frame_shorts.configure(background="White")
        tip_frame3="pantaloni"

        if budg_shorts.get()=="1" :
            for row in c.execute("""SELECT *
            FROM Db_unificato_v1
            where Sex = ? and tipo = ? and Ecologico=? and Tecnicità=? and Socialità=? and Eccentricità=?
            order by RANDOM()
            limit 10 """,
            (clicksex.get(), tip_frame3, Eco, Tecnico, Social, Eccentrico,)):
                list_shorts_id.append(row[0])
                list_shorts_name.append(row[2].upper())
                list_shorts_brand.append(row[3].upper())
                list_shorts_colour.append(row[4])
                list_shorts_price.append(row[8])
                list_shorts_store.append(row[9].upper())
                list_shorts_url.append(row[1])
        #Definiamo un messggio se non sono presenti prodotto nella query
        else:
            for row in c.execute("""SELECT *
            FROM Db_unificato_v1
            where Sex = ? and tipo = ? and Ecologico=? and Tecnicità=? and Socialità=? and Eccentricità=? and Price<?
            order by RANDOM()
            limit 10 """,
            (clicksex.get(), tip_frame3, Eco, Tecnico, Social, Eccentrico,float(Shorts_budg1.get()),)):
                list_shorts_id.append(row[0])
                list_shorts_name.append(row[2].upper())
                list_shorts_brand.append(row[3].upper())
                list_shorts_colour.append(row[4])
                list_shorts_price.append(row[8])
                list_shorts_store.append(row[9].upper())
                list_shorts_url.append(row[1])


        if list_shorts_id==[]:
            Mess_no_shorts=Label(frame_shorts, text="Ci dispiace ma non ci sono pantaloni in base alle tue caratteristiche", bg="white", font="Helvetica 18 bold")
            Mess_no_shorts.pack(side=TOP, anchor="center")
        else:
            inflist2= ("img_"+list_shorts_id[0]+".jpg")
            global img_shorts #Definiamo global la var immagine altrimenti non funziona
            #'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\img_10280615.jpg'
            try:
                img_shorts  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist2}').resize((100,100),Image.ANTIALIAS))
            except:
                inflist2= ("img_img"+list_shorts_id[0]+".jpg")
                img_shorts  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist2}').resize((100,100),Image.ANTIALIAS))
            global canvasshort
            canvasshort = Canvas(frame_shorts, width = 200 , height = 200,borderwidth=1, highlightthickness=1,bg="white")
            button_forward_shorts = Button(frame_shorts, text="Next", fg="blue",command=forward_shorts)
            button_forward_shorts.pack(side=RIGHT, anchor="ne")

            button_backward_shorts = Button(frame_shorts, text="Back",fg="blue",command=back_shorts)
            button_backward_shorts.pack(side=RIGHT, anchor="ne")

            canvasshort.pack(side=LEFT, anchor="w")
            canvasshort.create_image(90,90,image = img_shorts)

            global characteristics_shorts
            characteristics_shorts = Label(frame_shorts, text= "Il 1° pantalone che ti proponiamo è il '" + list_shorts_name[0] +"' della " + list_shorts_brand[0] + " disponibile nel colore " + list_shorts_colour[0] +".\n\n\nPREZZO: €"+str(list_shorts_price[0]) + " \nSTORE: " +list_shorts_store[0], justify= CENTER, padx=10, pady=20, bg="white",font="Helvetica 9 bold")
            characteristics_shorts.pack(side=TOP, anchor="n")

            global URL_shorts
            URL_shorts = list_shorts_url[0]

    if int(shoes.get())==1:
        global elem3
        elem3 = 0
        global frame_shoes
        frame_shoes = LabelFrame(window_new, text="Scarpe scelte per te",width=1300 , height=230)
        frame_shoes.pack_propagate(0)
        frame_shoes.pack(side=TOP, anchor ="nw")
        frame_shoes.configure(background="White")
        tip_frame1="scarpe"

        if budg_shoes.get()=="1":
            for row in c.execute("""SELECT *
            FROM Db_unificato_v1
            where Sex = ? and tipo = ? and Ecologico=? and Tecnicità=? and Socialità=? and Eccentricità=?
            order by RANDOM()
            limit 10 """,
            (clicksex.get(), tip_frame1, Eco, Tecnico, Social, Eccentrico,)):
                list_shoes_id.append(row[0])
                list_shoes_name.append(row[2].upper())
                list_shoes_brand.append(row[3].upper())
                list_shoes_colour.append(row[4])
                list_shoes_price.append(row[8])
                list_shoes_store.append(row[9].upper())
                list_shoes_url.append(row[1])
        else:
            for row in c.execute("""SELECT *
            FROM Db_unificato_v1
            where Sex = ? and tipo = ? and Ecologico=? and Tecnicità=? and Socialità=? and Eccentricità=? and Price<?
            order by RANDOM()
            limit 10 """,
            (clicksex.get(), tip_frame1, Eco, Tecnico, Social, Eccentrico,float(Shoes_budg1.get()),)):
                list_shoes_id.append(row[0])
                list_shoes_name.append(row[2].upper())
                list_shoes_brand.append(row[3].upper())
                list_shoes_colour.append(row[4])
                list_shoes_price.append(row[8])
                list_shoes_store.append(row[9].upper())
                list_shoes_url.append(row[1])
        if list_shoes_id==[]:
            Mess_no_shoes=Label(frame_shoes, text="Ci dispiace ma non ci sono scarpe in base alle tue caratteristiche", bg="white", font="Helvetica 18 bold")
            Mess_no_shoes.pack(side=TOP, anchor="center")
        else:
            inflist3= ("img_"+list_shoes_id[0]+".jpg")
            global img_shoes #Definiamo global la var immagine altrimenti non funziona
            #'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\img_10280615.jpg'
            try:
                img_shoes  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist3}').resize((100,100),Image.ANTIALIAS))
            except:
                inflist3= ("img_img"+list_shoes_id[0]+".jpg")
                img_shoes  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist3}').resize((100,100),Image.ANTIALIAS))
            #Creiamo bottone per spostarci in avanti
            button_forward_shoes = Button(frame_shoes, text="Next", fg="green",command=forward_shoes)
            button_forward_shoes.pack(side=RIGHT, anchor="ne")

            button_backward_shoes = Button(frame_shoes, text="Back",fg="green",command=back_shoes)
            button_backward_shoes.pack(side=RIGHT, anchor="ne")

            global canvasshoes
            canvasshoes = Canvas(frame_shoes,width = 200 , height = 200,borderwidth=1, highlightthickness=1,bg="white")
            canvasshoes.pack(side=LEFT, anchor="w")
            canvasshoes.create_image(90,90,image = img_shoes)

            global characteristics_shoes
            characteristics_shoes = Label(frame_shoes, text= "Il 1° modello di scarpe che ti proponiamo sono le '" + list_shoes_name[0] +
            "'\n della " + list_shoes_brand[0] + " disponibile nel colore " + list_shoes_colour[0] +".\n\n\nPREZZO: € " + str(list_shoes_price[0]) +
            "\nSTORE: " + list_shoes_store[0], justify= LEFT, padx=10, pady=20, bg="white",font="Helvetica 9 bold")
            characteristics_shoes.pack(side=TOP,anchor="n")
#Definiamo il totale in € degli items
    global total_price_list
    total_price_list=[]
    global Label_total_price

    try:
        total_price_list.append(list_shirt_price[0])
    except:
        pass
    try:
        total_price_list.append(list_shorts_price[0])
    except:
        pass
    try:
        total_price_list.append(list_shoes_price[0])
    except:
        pass
    total_price = round(sum(total_price_list),2)
    print(total_price_list,"ciao sono il totale lunghezza lista della funzione")
    print(total_price)
    #Definiamo totale outfit
    Label_total_price = Label(window_new, text = "IL COSTO TOTALE DEL TUO OUTFIT È DI: €" + str(total_price), padx=10, pady=10, fg="black",bg="Silver", font="Helvetica 14 bold")
    #Definiamo bottone per terminare la scelta
    Button_finito = Button(window_new, text="HO FINITO  ", command=ho_finito, padx=5, pady=5,justify="left",font="Helvetica 14 bold")
    Button_finito.pack(side=TOP, anchor="e")
    Label_total_price.pack(side=TOP,anchor="center")
    global URL_shoes
    URL_shoes = list_shoes_url[0]

#Creiamo tutti i tasti avanti e indietro per scorrere gli elementi del DB--> 3 tasti avanti e 3 tasti indietro
def forward_shirts():
    global window_new
    global elem
    elem=elem+1
    print(elem)
    global img_shirt
    inflist1= ("img_"+ list_shirt_id[elem]+ ".jpg")
    try:

        img_shirt  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist1}').resize((100,100),Image.ANTIALIAS))
    except:
        inflist1= ("img_img"+ list_shirt_id[elem]+ ".jpg")
        img_shirt  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist1}').resize((100,100),Image.ANTIALIAS))
    #Definiamo global la var immagine altrimenti non funziona
    #'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\img_10280615.jpg'
    img_shirt  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist1}').resize((100,100),Image.ANTIALIAS))
    global canvasshirt
    canvasshirt.pack_forget()
    canvasshirt = Canvas(frame_shirt, width = 200 , height = 200,borderwidth=1, highlightthickness=1,bg="white")
    canvasshirt.pack(side=LEFT, anchor="nw")

    canvasshirt.create_image(90,90,image = img_shirt)
    global characteristics_shirt
    characteristics_shirt.pack_forget()
    characteristics_shirt = Label(frame_shirt, text= "La " + str(elem+1)+"° "+"maglia che ti proponiamo è la '" + list_shirt_name[elem] +   "' della " + list_shirt_brand[elem] + " disponibile nel colore " + list_shirt_colour[elem] +".\n\n\nPREZZO: € " + str(list_shirt_price[elem]) + "\nSTORE: " + list_shirt_store[elem], justify= CENTER, padx=10,
     pady=20, bg="white",font="Helvetica 9 bold")
    characteristics_shirt.pack(side=TOP, anchor="n")
    #Per creare un totale € dinamico dobbiamo indicizzare gli elementi dell'outfit(1,2,3) e dirgli ogni volta: distruggi l'elemento(pop) in posizione x e inseriscine uno nuovo in posizione x (insert)
    global total_price_list
    total_price_list.pop(0)
    global Label_total_price
    Label_total_price.destroy()
    try:
        total_price_list.insert(0, list_shirt_price[elem])
    except:
        pass

    total_price = round(sum(total_price_list),2)
    print(total_price)
    Label_total_price = Label(window_new, text = "IL COSTO TOTALE DEL TUO OUTFIT È DI: €" + str(total_price), padx=10, pady=10, fg="black",bg="Silver", font="Helvetica 14 bold")
    Label_total_price.pack(side=TOP,anchor="center")
    global URL_shirt
    URL_shirt = list_shirt_url[elem]
    print(URL_shirt)

def forward_shorts():
    global window_new
    global elem2
    elem2=elem2+1
    print(elem2)
    inflist2= ("img_"+ list_shorts_id[elem2]+ ".jpg")
    global img_shorts #Definiamo global la var immagine altrimenti non funziona
    #'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\img_10280615.jpg'
    try:
        img_shorts  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist2}').resize((100,100),Image.ANTIALIAS))
    except:
        inflist2= ("img_img"+ list_shorts_id[elem2]+ ".jpg")
        img_shorts  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist2}').resize((100,100),Image.ANTIALIAS))

    global canvasshort
    canvasshort.pack_forget()
    canvasshort = Canvas(frame_shorts, width = 200 , height = 200,borderwidth=1, highlightthickness=1,bg="white")
    canvasshort.pack(side=LEFT, anchor="w")
    canvasshort.create_image(90,90,image = img_shorts)
    global characteristics_shorts
    characteristics_shorts.pack_forget()
    characteristics_shorts = Label(frame_shorts, text= "I " + str(elem2+1)+"° "+"pantaloni che ti proponiamo sono i '" + list_shorts_name[elem2] +
    "'\n della " + list_shorts_brand[elem2] + " disponibile nel colore " + list_shorts_colour[elem2] +
    ".\n\n\nPREZZO: € " + str(list_shorts_price[elem2]) + "\nSTORE: " + list_shorts_store[elem2], justify= CENTER, padx=10, pady=20, bg="white",font="Helvetica 9 bold")
    characteristics_shorts.pack(side=TOP,anchor="n")
    global total_price_list
    #Per creare un totale € dinamico dobbiamo indicizzare gli elementi dell'outfit(1,2,3) e dirgli ogni volta: distruggi l'elemento(pop) in posizione x e inseriscine uno nuovo in posizione x (insert)
    print(total_price_list,"ciao sono il totale lunghezza lista della forward shorts")
    if len (total_price_list)==1 or len (total_price_list)==2 :
        total_price_list.pop(0)
        try:
            total_price_list.insert(0,list_shorts_price[elem2])
            print(total_price_list)
        except:
            pass
    if len(total_price_list)==3:
        total_price_list.pop(1)
        print(total_price_list,"ciao sono il totale lunghezza lista della funzione")
        try:
            total_price_list.insert(1,list_shorts_price[elem2])
            print(total_price_list,"ciao sono il totale lunghezza lista della funzione")
        except:
            pass

    global Label_total_price
    Label_total_price.destroy()

    total_price = round(sum(total_price_list),2)
    print(total_price)
    Label_total_price = Label(window_new, text = "IL COSTO TOTALE DEL TUO OUTFIT È DI: €" + str(total_price), padx=10, pady=10 ,fg="black",bg="Silver", font="Helvetica 14 bold")
    Label_total_price.pack(side=TOP,anchor="center")
    global URL_shorts
    URL_shorts = list_shorts_url[elem2]
    print(URL_shorts)

def forward_shoes():
    global window_new
    global elem3
    elem3=elem3+1
    print(elem3)
    inflist3= ("img_"+ list_shoes_id[elem3]+ ".jpg")
    print(inflist3)
    global img_shoes #Definiamo global la var immagine altrimenti non funziona
    #'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\img_10280615.jpg'
    try:
        img_shoes  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist3}').resize((100,100),Image.ANTIALIAS))
    except:
        inflist3= ("img_img"+ list_shoes_id[elem3]+ ".jpg")
        img_shoes  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist3}').resize((100,100),Image.ANTIALIAS))
    global canvasshoes
    canvasshoes.pack_forget()
    canvasshoes = Canvas(frame_shoes, width = 200 ,height = 200,borderwidth=1, highlightthickness=1,bg="white")
    canvasshoes.pack(side=LEFT, anchor="nw")
    canvasshoes.create_image(90,90,image = img_shoes)
    global characteristics_shoes
    characteristics_shoes.pack_forget()
    characteristics_shoes = Label(frame_shoes, text= "Il " + str(elem3+1)+"° modello di scarpe che ti proponiamo sono le '" + list_shoes_name[elem3] +
    "'\n della " + list_shoes_brand[elem3] + " disponibile nel colore " + list_shoes_colour[elem3] +".\n\n\nPREZZO: € " + str(list_shoes_price[elem3]) + "\nSTORE: " + list_shoes_store[elem3], justify= CENTER, padx=10, pady=20, bg="white",font="Helvetica 9 bold")
    characteristics_shoes.pack(side=TOP,anchor="n")
    global total_price_list
    #Per creare un totale € dinamico dobbiamo indicizzare gli elementi dell'outfit(1,2,3) e dirgli ogni volta: distruggi l'elemento(pop) in posizione x e inseriscine uno nuovo in posizione x (insert)

    print(len(total_price_list))
    if len(total_price_list)==1:
        total_price_list.pop(0)
        try:
            total_price_list.insert(0,list_shoes_price[elem3])
        except:
            pass
    if len(total_price_list)==2:
        total_price_list.pop(1)
        try:
            total_price_list.insert(1,list_shoes_price[elem3])
        except:
            pass
    if len(total_price_list)==3:
        total_price_list.pop(2)
        try:
            total_price_list.insert(2,list_shoes_price[elem3])
        except:
            pass

    global Label_total_price
    Label_total_price.destroy()


    total_price = round(sum(total_price_list),2)
    print(total_price)
    Label_total_price = Label(window_new, text = "IL COSTO TOTALE DEL TUO OUTFIT È DI: €" + str(total_price), padx=10, pady=10, fg="black",bg="Silver", font="Helvetica 14 bold")
    Label_total_price.pack(side=TOP,anchor="center")
    global URL_shoes
    URL_shoes = list_shoes_url[elem3]
    print(URL_shoes)

def back_shirts():
    global window_new
    global elem
    if elem>0:
        elem=elem-1
    print(elem)
    inflist1= ("img_"+ list_shirt_id[elem]+ ".jpg")
    global img_shirt #Definiamo global la var immagine altrimenti non funziona
    #'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\img_10280615.jpg'
    try:
        img_shirt  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist1}').resize((100,100),Image.ANTIALIAS))
    except:
        inflist1= ("img_img"+ list_shirt_id[elem]+ ".jpg")
        img_shirt  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist1}').resize((100,100),Image.ANTIALIAS))
    global canvasshirt
    canvasshirt.pack_forget()
    canvasshirt = Canvas(frame_shirt, width = 200 ,height = 200,borderwidth=1, highlightthickness=1,bg="white")
    canvasshirt.pack(side=LEFT, anchor="nw")
    canvasshirt.create_image(90,90,image = img_shirt)
    global characteristics_shirt
    characteristics_shirt.pack_forget()
    characteristics_shirt = Label(frame_shirt, text= "La " + str(elem+1)+"° "+"maglia che ti proponiamo è la '" + list_shirt_name[elem] +
    "' della " + list_shirt_brand[elem] + " disponibile nel colore " + list_shirt_colour[elem] +".\n\n\nPREZZO: € " + str(list_shirt_price[elem]) + "\nSTORE: " + list_shirt_store[elem], justify= CENTER, padx=10, pady=20, bg="white",font="Helvetica 9 bold")
    characteristics_shirt.pack(side=TOP, anchor="n")
    global total_price_list
    #Per creare un totale € dinamico dobbiamo indicizzare gli elementi dell'outfit(1,2,3) e dirgli ogni volta: distruggi l'elemento(pop) in posizione x e inseriscine uno nuovo in posizione x (insert)

    global Label_total_price
    total_price_list.pop(0)
    global Label_total_price
    Label_total_price.destroy()
    try:
        total_price_list.insert(0, list_shirt_price[elem])
    except:
        pass

    total_price = round(sum(total_price_list),2)
    print(total_price)
    Label_total_price = Label(window_new, text = "IL COSTO TOTALE DEL TUO OUTFIT È DI: €" + str(total_price), padx=10, pady=10, fg="black",bg="Silver", font="Helvetica 14 bold")
    Label_total_price.pack(side=TOP,anchor="center")
    global URL_shirt
    URL_shirt = list_shirt_url[elem]
    print(URL_shirt)

def back_shorts():
    global window_new
    global elem2
    if elem2>0:
        elem2=elem2-1
    print(elem2)
    inflist2= ("img_"+ list_shorts_id[elem2]+ ".jpg")
    global img_shorts #Definiamo global la var immagine altrimenti non funziona
    #'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\img_10280615.jpg'
    try:
        img_shorts  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist2}').resize((100,100),Image.ANTIALIAS))
    except:
        inflist2= ("img_img"+ list_shorts_id[elem2]+ ".jpg")
        img_shorts  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist2}').resize((100,100),Image.ANTIALIAS))
    global canvasshort
    canvasshort.pack_forget()
    canvasshort = Canvas(frame_shorts, width = 200 ,height = 200,borderwidth=1, highlightthickness=1,bg="white")
    canvasshort.pack(side=LEFT, anchor="nw")
    canvasshort.create_image(90,90,image = img_shorts)
    global characteristics_shorts
    characteristics_shorts.pack_forget()
    characteristics_shorts = Label(frame_shorts, text= "I " + str(elem2+1)+"° "+"pantaloni che ti proponiamo sono i '" + list_shorts_name[elem2] +
    "'\n della " + list_shorts_brand[elem2] + " disponibile nel colore " + list_shorts_colour[elem2] +".\n\n\nPREZZO: €" + str(list_shorts_price[elem2]) +"\nSTORE: "+ list_shorts_store[elem2], justify= CENTER, padx=10, pady=20, bg="white",font="Helvetica 9 bold")
    characteristics_shorts.pack(side=TOP,anchor="n")
    global total_price_list
    global Label_total_price
    #Per creare un totale € dinamico dobbiamo indicizzare gli elementi dell'outfit(1,2,3) e dirgli ogni volta: distruggi l'elemento(pop) in posizione x e inseriscine uno nuovo in posizione x (insert)

    Label_total_price.destroy()
    global total_price_list
    if len (total_price_list)==1 or len (total_price_list)==2:
        total_price_list.pop(0)
        try:
            total_price_list.insert(0,list_shorts_price[elem2])
        except:
            pass
    if len(total_price_list)==3:
        total_price_list.pop(1)
        try:
            total_price_list.insert(1,list_shorts_price[elem2])
        except:
            pass

    total_price = round(sum(total_price_list),2)
    print(total_price)
    Label_total_price = Label(window_new, text = "IL COSTO TOTALE DEL TUO OUTFIT È DI: €" + str(total_price), padx=10, pady=10, fg="black",bg="Silver", font="Helvetica 14 bold")
    Label_total_price.pack(side=TOP,anchor="center")
    global URL_shorts
    URL_shorts = list_shorts_url[elem2]
    print(URL_shorts)

def back_shoes():
    global window_new
    global elem3
    if elem3>0:
        elem3=elem3-1
    print(elem3)
    inflist3= ("img_"+ list_shoes_id[elem3]+ ".jpg")
    global img_shoes #Definiamo global la var immagine altrimenti non funziona
    #'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\img_10280615.jpg'
    try:
        img_shoes  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist3}').resize((100,100),Image.ANTIALIAS))
    except:
        inflist3= ("img_img"+ list_shoes_id[elem3]+ ".jpg")
        img_shoes  = ImageTk.PhotoImage(Image.open(f'C:\\Users\\Pasqui\\Desktop\\Project\\Images\\content\\{inflist3}').resize((100,100),Image.ANTIALIAS))
    global canvasshoes
    canvasshoes.pack_forget()
    canvasshoes = Canvas(frame_shoes, width = 200 , height = 200,borderwidth=1, highlightthickness=1,bg="white")
    canvasshoes.pack(side=LEFT, anchor="nw")
    canvasshoes.create_image(90,90,image = img_shoes)
    global characteristics_shoes
    characteristics_shoes.pack_forget()
    characteristics_shoes = Label(frame_shoes, text= "Il " + str(elem3+1)+"° modello di scarpe che ti proponiamo sono le '" + list_shoes_name[elem3] +
    "'\n della " + list_shoes_brand[elem3] + " disponibile nel colore " + list_shoes_colour[elem3] +".\n\n\nPREZZO: €" + str(list_shoes_price[elem3]) +"\nSTORE: "+ list_shoes_store[elem3], justify= CENTER, padx=10, pady=20, bg="white",font="Helvetica 9 bold")
    characteristics_shoes.pack(side=TOP,anchor="n")

    global Label_total_price
    #Per creare un totale € dinamico dobbiamo indicizzare gli elementi dell'outfit(1,2,3) e dirgli ogni volta: distruggi l'elemento(pop) in posizione x e inseriscine uno nuovo in posizione x (insert)

    Label_total_price.destroy()
    global total_price_list
    print(len(total_price_list))
    if len(total_price_list)==1:
        total_price_list.pop(0)
        try:
            total_price_list.insert(0,list_shoes_price[elem3])
        except:
            pass
    if len(total_price_list)==2:
        total_price_list.pop(1)
        try:
            total_price_list.insert(1,list_shoes_price[elem3])
        except:
            pass
    if len(total_price_list)==3:
        total_price_list.pop(2)
        try:
            total_price_list.insert(2,list_shoes_price[elem3])
        except:
            pass

    total_price = round(sum(total_price_list),2)
    print(total_price)
    Label_total_price = Label(window_new, text = "IL COSTO TOTALE DEL TUO OUTFIT È DI: €" + str(total_price), padx=10, pady=10 ,fg="black",bg="Silver", font="Helvetica 14 bold")
    Label_total_price.pack(side=TOP,anchor="center")
    global URL_shoes
    URL_shoes = list_shoes_url[elem3]
    print(URL_shoes)

Bottone_gen_output = Button(frame5, text = "Genera outfit", font="12", bg="black",fg="white", command=genera_output).pack()
frame5.pack_forget()

#----------------Creiamo il frame 6 finale con i link ai siti per l'acquisto
global frame6
frame6 = Frame(root, width=60 , height=200,bg="white")
frame6.pack()
frame6.pack_forget()

#Def per rendere i link cliccabili
def callback(url):
    webbrowser.open_new(url)

#Creiamo def ho finito da inserire nel bottone ho finito per creare il frame 6 e i link
def ho_finito():
    window_new.destroy()
    frame5.destroy()
    frame6.pack(side=TOP,  anchor="center")
    frame6.configure(background="white")
    Label_addio = Label(frame6, text="""Grazie per aver utilizzato GECKO SPORT. Inseriamo sotto i link da cliccare per gli acquisti dell'
    outfit che hai scelto:\n""",width=90, bg="aliceblue", font="Helvetica 11 bold")
    Label_addio.pack()

    #Creo i link alle maglie da cliccare
    global URL_shirt
    if URL_shirt!="":
        link1 = Label(frame6, text="LA TUA MAGLIA", fg="blue",font="Helvetica 10 bold",width=150, bg="white", cursor="hand2")
        link1.pack(anchor="w")
        link1.bind("<Button-1>", lambda e: callback(URL_shirt))
    global URL_shorts
    if URL_shorts!="":
        link2 = Label(frame6, text="I TUOI PANTALONI", fg="blue",font="Helvetica 10 bold",width=150, bg="white", cursor="hand2")
        link2.pack(anchor="w")
        link2.bind("<Button-1>", lambda e: callback(URL_shorts))
    global URL_shoes
    if URL_shoes!="":
        link3 = Label(frame6, text="LE TUE SCARPE", fg="blue",font="Helvetica 10 bold", width=150,bg="white",cursor="hand2")
        link3.pack(anchor="w")
        link3.bind("<Button-1>", lambda e: callback(URL_shoes))

root.mainloop()
