from tkinter import *
from tkinter import ttk

class todo:
         def __init__(self, root):
                 self.root = root
                 self.root.title("To-do-list")
                 self.root.geometry("650x410+300+150")

                 self.label =Label(self.root, text= "TO-DO-LIST-APP",font ="arial 25 bold",width=10,bd=5,bg="orange",fg="black")
                 self.label.pack(side="top",fill=BOTH)


                 self.label2 =Label(self.root, text= "Add Task",font ="arial 18 bold",width=10,bd=5,bg="orange",fg="black")
                 self.label2.place(x=40,y=55)

                 
                 self.label3 =Label(self.root, text= "Tasks",font ="arial 18 bold",width=10,bd=5,bg="orange",fg="black")
                 self.label3.place(x=320,y=54)

                 self.main_text =Listbox(self.root,height=9,bd=5,width=23,font="arial 20 italic bold")
                 self.main_text.place(x=200,y=100)

                 self.text=Text(self.root,bd=5,height=2, width=22,font="arial 10 bold")
                 self.text.place(x=20,y=100)

                 #===============add tasks==================#

                 def add():
                         content=self.text.get(1.0,END)
                         self.main_text.insert(END,content)
                         with open("data.txt","a")as file:
                                 file.write(content)
                                 file.seek(0)
                                 file.close()
                         self.text.delete(1.0,END)


                 def delete():
                          selected_index = self.main_text.curselection()
                          if selected_index: 
                                        # Ensure something is selected
                                       self.main_text.delete(selected_index)
                                       with open("data.txt", "r+") as f:
                                               lines = f.readlines()
                                               f.seek(0)
                                               for line in lines:
                                                       if line.strip() != self.main_text.get(selected_index):
                                                               
                                                            f.write(line)
                                                            f.truncate()

                             

                 with open("data.txt","r")as file:
                         read=file.readlines()
                         for i in read:
                                 ready=i.split()#it separate  the line on  list box
                                 self.main_text.insert(END,ready)                
                         file.close()

                 self.button=Button(self.root,text="Add",font="serif 20 bold italic",width=5,bd=5,bg="orange",fg="black",command=add) 
                 self.button.place(x=30,y=180)     

                 self.button2=Button(self.root,text="Delete",font="serif 20 bold italic",width=5,bd=5,bg="orange",fg="black",command=delete) 
                 self.button2.place(x=30,y=300)        
   
def main():
        root =Tk()
        ul=todo(root)
        root.mainloop()

if __name__ == "__main__":  
        main()              