from tkinter import *
root = Tk()
nodeState = {}
nodeCoords = {}
w = root.winfo_screenwidth() /2 - 530
h = root.winfo_screenwidth() /2 - 670
root.geometry(f"1060x670+{int(w)}+{int(h)}")
root.configure(bg='#201c1c')

cnv = Canvas(root,height=600,width=1015,bg='#201c14')
cnv.place(x=20,y=20)

a_n = 0
def create(e):
    global a_n
    a_n += 1
    exec(f'a{a_n}n1 = cnv.create_oval(105,535,120,550,fill="black",tags="a{a_n}")',globals())
    exec(f'a{a_n}n2 = cnv.create_oval(105,560,120,575,fill="black",tags="a{a_n}")',globals())
    exec(f'a{a_n} = Label(cnv,name="a{a_n}",text=\'AND\',fg=\'white\',activebackground=\'red\',bd=1,bg=\'red\',width=12,height=3)\na{a_n}.place(x=120,y=530)\na{a_n}.bind("<Button-1>",drag_start)\na{a_n}.bind("<B1-Motion>",drag_motion)')
    
    nodeState[f'a{a_n}'] = [0,0]
    nodeCoords[f'"a{a_n}"'] = [0,0,0,0,0,0,0,0]
    
AND = Label(root,text='AND',height=2,width=10)
AND.place(x=20,y=630) 
AND.bind('<Button-1>',create)

def out(e):
    e.widget['bd'] = 1

def drag_start(e):
    w = e.widget
    w.focus_set()    
    w.bind("<Delete>",ddd)
    w.bind("<FocusOut>",out)
    w.startX = e.x
    w.startY = e.y
    w['bd'],w['relief'] = 3,'solid'
    
def ddd(e):
    del nodeState[str(e.widget)[-2:]]
    e.widget.destroy()
    exec(f'cnv.delete({str(e.widget)[-2:]}n1)\ncnv.delete({str(e.widget)[-2:]}n2)')

def drag_motion(e):
    w = e.widget
    # nodeCoords[str(w)[-2:]][0] = w.winfo_x()-w.startX + e.x
    # nodeCoords[str(w)[-2:]][1] = w.winfo_y()-w.startY + e.y
    # print(nodeCoords)
    xxx = str(w)[-2:]
    eval(f'cnv.moveto({xxx}n1,w.winfo_x() - w.startX + e.x-15,w.winfo_y() - w.startY + e.y+5)')
    eval(f'cnv.moveto({xxx}n2,w.winfo_x() - w.startX + e.x-15,w.winfo_y() - w.startY + e.y+30)')

    
    x = w.winfo_x() - w.startX + e.x
    y = w.winfo_y() - w.startY + e.y
    w.place(x=x,y=y)


root.mainloop()
