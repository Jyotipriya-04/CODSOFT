from tkinter import *

def click(event):
         global scvalue
         text= event.widget.cget("text")
         print(text)
         if text == "=":
                 if scvalue.get().isdigit():
                         value =int(scvalue.get())
                 else:
                         try:
                                value=eval(screen.get())
                         except Exception as e:
                                  print(e)
                                  value ="Error"     

                 scvalue.set(value)
                 screen.update()       
         elif text == "c":
                 scvalue.set("")
                 screen.update()
         else:
                 scvalue.set(scvalue.get() + text)
                 screen.update()

root= Tk()
root.geometry("500x1000")
root.title("CaLcuLator")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar= scvalue, font= "lucida 40 bold")
screen.pack(fill=X, ipadx=8,pady=10,padx=10)


f= Frame(root, bg="grey")
b= Button(f,text="9",padx=5,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b= Button(f,text="8",padx=5,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b= Button(f,text="7",padx=5,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root, bg="grey")
b= Button(f,text="6",padx=5,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b= Button(f,text="5",padx=5,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b= Button(f,text="4",padx=5,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root, bg="grey")
b= Button(f,text="3",padx=5,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b= Button(f,text="2",padx=5,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b= Button(f,text="1",padx=5,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root, bg="grey")
b= Button(f,text="0",padx=6,pady=6,font="lucida 35 bold")
b.pack(side=LEFT,padx=6,pady=6)
b.bind("<Button-1>",click)

b= Button(f,text="-",padx=6,pady=6,font="lucida 35 bold")
b.pack(side=LEFT,padx=6,pady=6)
b.bind("<Button-1>",click)

b= Button(f,text="*",padx=8,pady=8,font="lucida 35 bold")
b.pack(side=LEFT,padx=6,pady=6)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root, bg="grey")
b= Button(f,text="/",padx=5,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b= Button(f,text="%",padx=3,pady=3,font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)
b= Button(f,text="+",padx=5,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

f.pack()

f= Frame(root, bg="grey")
b= Button(f,text="c",padx=3,pady=3,font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)


b= Button(f,text="00",padx=1,pady=1,font="lucida 35 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b= Button(f,text="=",padx=3,pady=3,font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()