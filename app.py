from tkinter import*
import tkinter.scrolledtext as scrolledtext
import socket


# !===============Functios=====================
def Ip_Ex():
    domin = en1.get() 
    ip = socket.gethostbyname(domin)
    text1.insert('end' , "[+]- : " , "black")
    text1.insert('end' ,domin , "green")
    text1.insert('end' , "is :\n " , "black")
    text1.insert('end' , ip , "red")

def Port_Ex():
    port = en2.get() 
    protnum = socket.getservbyport(int(port))
    text2.insert('end' , '[+] - prot: ' , 'black') 
    text2.insert('end' , port , 'green')
    text2.insert('end' , 'is : \n' , 'black')
    text2.insert('end' , protnum , 'red')

def Protocol_Ex():
    protocol = en3.get()  
    protnum = socket.getservbyname(protocol)
    text3.insert('end' , '[+] - Protocol:' ,'black')
    text3.insert('end' , protocol ,'green')
    text3.insert('end' , 'is :\n' ,'black')
    text3.insert('end' , protnum, 'red')


# ?================Root======================
root = Tk()
# ?================Size Window===============
root.geometry('900x750')
# ?================Titile Window===============
root.title('Networks [Dev : Mostafa]')
# *=================Titile======================
title = Label(root,text='Protocol Spot' , font=('JetBrainsMono' , 20 , 'bold') , bg='black' , fg='white')
title.pack(fill=X)
# *================Image========================
photo  = PhotoImage(file='images/hack.png')
photoLable = Label(root , image=photo)
photoLable.place(x=1 , y=39, width=900 , height=450)
# !================ScrolledTest===================
text1 = scrolledtext.ScrolledText(root)
text1['font'] = ('JetBrainsMono' ,' 10' , 'bold')
text1.tag_configure('red' , background='white' , foreground= 'black')
text1.tag_configure('black' , background='white' , foreground= 'red')
text1.tag_configure('green' , background='white' , foreground= 'green')
text1.place(x=1 , y=500  ,width=280 , height=150)

text2 = scrolledtext.ScrolledText(root)
text2['font'] = ('JetBrainsMono' ,' 10' , 'bold')
text2.tag_configure('red' , background='white' , foreground= 'black')
text2.tag_configure('black' , background='white' , foreground= 'red')
text2.tag_configure('green' , background='white' , foreground= 'green')
text2.place(x=310 , y=500  ,width=280 , height=150)

text3 = scrolledtext.ScrolledText(root)
text3['font'] = ('JetBrainsMono' ,' 10' , 'bold')
text3.tag_configure('red' , background='white' , foreground= 'black')
text3.tag_configure('black' , background='white' , foreground= 'red')
text3.tag_configure('green' , background='white' , foreground= 'green')
text3.place(x=600 , y=500  ,width=280 , height=150)



# ?==================Entery============================
en1 = Entry(root , font= ('JetBrainsMono' , '12') , justify= CENTER )
en1.place(x = 1 , y = 670 , width = 260 , height = 24)

en2 = Entry(root , font= ('JetBrainsMono' , '12') , justify= CENTER )
en2.place(x = 315 , y = 670 , width = 260 , height = 24)

en3 = Entry(root , font= ('JetBrainsMono' , '12') , justify= CENTER )
en3.place(x = 602 , y = 670 , width = 260 , height = 24)



# ?==================Buttons============================
button1 = Button(root , text='Ip Extraction' , width=36 , height=1 , cursor='hand2' , command=Ip_Ex)
button1.place(x = 1 , y= 700)

button2 = Button(root , text='Port Extraction' , width=36 , height=1 , cursor='hand2' ,command=Port_Ex )
button2.place(x = 315 , y= 700)

button3 = Button(root , text='Protocol Extraction' , width=36 , height=1 , cursor='hand2' , command= Protocol_Ex)
button3.place(x = 602 , y= 700)


# ?================Change Icon Window===============
iconWindow = PhotoImage(file='images/network.png')
root.iconphoto(True , iconWindow)
root.mainloop()
