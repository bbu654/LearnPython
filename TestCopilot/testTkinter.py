from tkinter import *
root = Tk()
#v = IntVar()
#Label(root, root.title('Options'), text="""Choose a preferred language:""",justify=LEFT,padx=20).pack()
#Radiobutton(root,text='Python',padx=20,variable=v,value=1).pack(anchor=W)
#Radiobutton(root,text='C++',padx=20,variable=v,value=2).pack(anchor=W)
def var_states():    #sticky=North,East,South,West  row=separateRows
    print("Warrior: %d,Mage: %d"  % (var1.get(),var2.get()))
Label(root,root.title("Adventure Game"),text=">>>>>>>>>>>Your adventure role<<<<<<<<<<").grid(row=0,sticky=N)
var1=IntVar()
Checkbutton(root,text='Warrior',variable=var1).grid(row=1,sticky=W)
var2=IntVar()
Checkbutton(root,text='Mage',variable=var2).grid(row=2,sticky=W)
Button(root,text='Quit', command=root.destroy).grid(row=3,sticky=W,pady=4)
Button(root,text='Show', command=var_states).grid(row=3,sticky=E,pady=4)
mainloop()