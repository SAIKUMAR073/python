from tkinter.ttk import*
from tkinter import*
import math
def click1(*args):
    a_entry.delete(0,'end')
def click2(*args):
    b_entry.delete(0,'end')
def click3(*args):
    ur_entry.delete(0,'end')
def click4(*args):
    Er_entry.delete(0,'end')
def click5(*args):
    f_entry.delete(0,'end')
def modeparameters():
    a = a_entry.get()
    b = b_entry.get()
    m = m_choice.get()
    n = n_choice.get()
    ur = ur_entry.get()
    Er = Er_entry.get()
    f = f_entry.get()
    mode = choose_choice.get()
    u0 = 12.6*pow(10,-7)
    E0 = 8.854*pow(10,-12)
    v1 = ((1/(math.sqrt(float(ur)*u0*float(Er)*E0))))
    v = (v1/pow(10,8))
    lam = (v*pow(10,8)/(float(f)*pow(10,9)))
    eta = math.sqrt((u0*float(ur))/(float(Er)*E0))
    fc1 = (v*pow(10,8)/2)*(math.sqrt(pow((int(m)/float(a)),2)+pow((int(n)/float(b)),2)))
    fc = round(fc1/pow(10,9),1)
    lamc = (v*pow(10,8))/fc1
    if(float(f)>fc):
        k = (math.sqrt(1-(pow((fc/float(f)),2))))
        beta = (2*3.14*float(f)*pow(10,9))*(math.sqrt(float(ur)*u0*float(Er)*E0))*k
        beta_label = Label(Calculator,text="beta=%f"%(beta),font=('calibre',15,'bold'),fg='green').place(x=30,y=410)
        gamma_label = Label(Calculator,text="as f>fc (gamma=jbeta) gamma=j%f"%(beta),font=('calibre',15,'bold'),fg='green').place(x=30,y=440)
        vp1 = (v*pow(10,8))/k
        vp = vp1/pow(10,8)
        vg1 = (v*pow(10,8))*k
        vg = vg1/pow(10,8)
        lamp = lam/k
        if(mode == "TE"):
           impedTE = eta/k
           fc_label = Label(Calculator,text="The Cuttoff frequency of"+mode+m+n+"=%fHz=%fGHz"%(fc1,round(fc1/pow(10,9),1)),font=('calibre',15,'bold'),fg='green').place(x=30,y=470)
           lamc_label = Label(Calculator,text="The Cuttoff wavelength of"+mode+m+n+"=%fm=%fcm"%(lamc,lamc*100),font=('calibre',15,'bold'),fg='green').place(x=30,y=500)
           vp_label = Label(Calculator,text="The Phase velocity of"+mode+m+n+"=%f*10^8m/s"%(vp),font=('calibre',15,'bold'),fg='green').place(x=30,y=530)
           vg_label = Label(Calculator,text="The Group velocity of"+mode+m+n+"=%f*10^8m/s"%(vg),font=('calibre',15,'bold'),fg='green').place(x=30,y=560)
           lamp_label = Label(Calculator,text="The Phase wavelength of"+mode+m+n+"=%fm=%fcm"%(lamp,lamp*100),font=('calibre',15,'bold'),fg='green').place(x=30,y=590)
           impedTE_label = Label(Calculator,text="The Impedence of"+mode+m+n+"=%fohm"%(impedTE),font=('calibre',15,'bold'),fg='green').place(x=30,y=620)
        else:
            if(m !="0" and n != "0"):
                impedTM = eta*k
                fc_label = Label(Calculator,text="The Cuttoff frequency of"+mode+m+n+"=%fHz=%fGHz"%(fc1,round(fc1/pow(10,9),1)),font=('calibre',15,'bold'),fg='green').place(x=30,y=470)
                lamc_label = Label(Calculator,text="The Cuttoff wavelength of"+mode+m+n+"=%fm=%fcm"%(lamc,lamc*100),font=('calibre',15,'bold'),fg='green').place(x=30,y=500)
                vp_label = Label(Calculator,text="The Phase velocity of"+mode+m+n+"=%f*10^8m/s"%(vp),font=('calibre',15,'bold'),fg='green').place(x=30,y=530)
                vg_label = Label(Calculator,text="The Group velocity of"+mode+m+n+"=%f*10^8m/s"%(vg),font=('calibre',15,'bold'),fg='green').place(x=30,y=560)
                lamp_label = Label(Calculator,text="The Phase wavelength of"+mode+m+n+"=%fm=%fcm"%(lamp,lamp*100),font=('calibre',15,'bold'),fg='green').place(x=30,y=590)
                impedTM_label = Label(Calculator,text="The Impedence of"+mode+m+n+"=%fohm"%(impedTM),font=('calibre',15,'bold'),fg='green').place(x=30,y=620)
            else:
                label_correction = Label(Calculator,text="In TM Mode m and n must be not equal to zero"+" "*40,font=('calibre',15,'bold'),fg='green').place(x=30,y=410)
                label_dummy1 = Label(Calculator,text=" "*120,font=('calibre',15,'bold'),bg='grey').place(x=30,y=440)
                label_dummy2 = Label(Calculator,text=" "*120,font=('calibre',15,'bold'),bg='grey').place(x=30,y=470)
                label_dummy3 = Label(Calculator,text=" "*120,font=('calibre',15,'bold'),bg='grey').place(x=30,y=500)
                label_dummy3 = Label(Calculator,text=" "*120,font=('calibre',15,'bold'),bg='grey').place(x=30,y=530)
                label_dummy1 = Label(Calculator,text=" "*120,font=('calibre',15,'bold'),bg='grey').place(x=30,y=560)
                label_dummy2 = Label(Calculator,text=" "*120,font=('calibre',15,'bold'),bg='grey').place(x=30,y=590)
                label_dummy3 = Label(Calculator,text=" "*120,font=('calibre',15,'bold'),bg='grey').place(x=30,y=620)
    else:
        fc_label = Label(Calculator,text="The Cuttoff frequency of"+mode+m+n+"=%fHz=%fGHz"%(fc1,round(fc1/pow(10,9),1))+" "*1,font=('calibre',15,'bold'),fg='green').place(x=30,y=410)
        lamc_label = Label(Calculator,text="The Cuttoff wavelength of"+mode+m+n+"=%fm=%fcm"%(lamc,lamc*100)+" "*22,font=('calibre',15,'bold'),fg='green').place(x=30,y=440)
        label_statement = Label(Calculator,text="As f<fc the mode does not propagate through guide"+" "*29,font=('calibre',15,'bold'),fg='green').place(x=30,y=470)
        alpha = math.sqrt((pow((int(m)*3.14/float(a)),2))+(pow((int(n)*3.14/float(b)),2))-(pow((2*3.14*float(f)*pow(10,9)),2)*float(ur)*u0*float(Er)*E0))
        alpha_label = Label(Calculator,text="alpha=%fNeper/meter=%fdB"%(alpha,alpha*8.686)+" "*70,font=('calibre',15,'bold'),fg='green').place(x=30,y=500)
        gamma_label = Label(Calculator,text="as f<fc (gamma=alpha) gamma=%f"%(alpha)+" "*50,font=('calibre',15,'bold'),fg='green').place(x=30,y=530)
        label_dummy1 = Label(Calculator,text=" "*90,font=('calibre',15,'bold'),bg='grey').place(x=30,y=560)
        label_dummy2 = Label(Calculator,text=" "*90,font=('calibre',15,'bold'),bg='grey').place(x=30,y=590)
        label_dummy3 = Label(Calculator,text=" "*90,font=('calibre',15,'bold'),bg='grey').place(x=30,y=620)
    

Calculator = Tk()
Calculator.geometry("600x600")
Calculator.title("mode parameters_WaveGuides")
Calculator.config(bg='grey')
welcome = Label(Calculator,text="Welcome",font=('Stencil Std',30,'bold'),foreground="red",bg='grey')
welcome.pack()
canvas = Canvas(Calculator,width=702,height=437)
img = PhotoImage(file="RWG.png")
canvas.create_image(0,0,anchor=NW,image=img)
a = StringVar()
b = StringVar()
ur = StringVar()
Er = StringVar()
f = StringVar()
mode = StringVar()
m = StringVar()
n = StringVar()
a_label = Label(Calculator,text='a:',font=('calibre',15,'bold'),bg='grey')
b_label = Label(Calculator,text='b:',font=('calibre',15,'bold'),bg='grey')
a_entry = Entry(Calculator,textvariable=a,width=60)
a_entry.insert(0,'Enter a in meters(m)')
a_entry.bind("<Button>",click1)
b_entry = Entry(Calculator,textvariable=b,width=60)
b_entry.insert(0,'Enter b in meters(m)')
b_entry.bind("<Button>",click2)
ur_label = Label(Calculator,text='ur:',font=('calibre',15,'bold'),bg='grey')
Er_label = Label(Calculator,text='Er:',font=('calibre',15,'bold'),bg='grey')
f_label = Label(Calculator,text='f:',font=('calibre',15,'bold'),bg='grey')
ur_entry = Entry(Calculator,textvariable=ur,width=60)
ur_entry.insert(0,'Enter ur')
ur_entry.bind("<Button>",click3)
Er_entry = Entry(Calculator,textvariable=Er,width=60)
Er_entry.insert(0,'Enter Er')
Er_entry.bind("<Button>",click4)
f_entry = Entry(Calculator,textvariable=f,width=60)
f_entry.insert(0,'Enter frequency given in GHz')
f_entry.bind("<Button>",click5)
choose_label = Label(Calculator,text='Choose Mode:',font=('calibre',15,'bold'),bg='grey')
choose_choice = Combobox(Calculator,width=30,textvariable=mode,values=["TE","TM"],state='readonly') 
m_label = Label(Calculator,text='m:',font=('calibre',15,'bold'),bg='grey')
m_choice = Combobox(Calculator,width=30,textvariable=m,values=['0','1','2','3','4','5','6','7','8','9'],state='readonly') 
n_label = Label(Calculator,text='n:',font=('calibre',15,'bold'),bg='grey')
n_choice = Combobox(Calculator,width=30,textvariable=n,values=['0','1','2','3','4','5','6','7','8','9'],state='readonly') 
Calculate_button = Button(Calculator,text="Calculate",activebackground="red",fg="white",font=('calibre',15,"bold"),bg="blue",command=modeparameters)
a_label.place(x=30,y=45)
a_entry.place(x=60,y=50)
b_label.place(x=30,y=85)
b_entry.place(x=60,y=90)
ur_label.place(x=30,y=125)
ur_entry.place(x=60,y=130)
Er_label.place(x=30,y=165)
Er_entry.place(x=60,y=170)
f_label.place(x=30,y=205)
f_entry.place(x=60,y=210)
choose_label.place(x=0,y=245)
choose_choice.place(x=140,y=250)
m_label.place(x=30,y=285)
m_choice.place(x=60,y=290)
n_label.place(x=30,y=325)
n_choice.place(x=60,y=330)
Calculate_button.place(x=270,y=355)
canvas.place(x=670,y=100)
Calculator.mainloop()