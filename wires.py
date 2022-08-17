from tkinter import *
root = Tk()
cnv = Canvas(root,height=600,width=1000,bg='black')
cnv.pack()
l_n = 0
wires = []
def wire_start(e):
    
    global coords,l_n
    e.widget.startX = e.x
    e.widget.startY = e.y
    cnv.bind("<Motion>",wire_motion)
    try:
        coords = ''
        for i in cnv.coords(wires[-1]):
            coords += str(i)+','
        eval(f'cnv.coords({wires[-1]},{coords}e.x,e.y)')
       
    except Exception as b:
        print(b)
        l_n = len(wires)+1
        print(l_n)
        exec(f'l{l_n} = cnv.create_line({e.x},{e.y},{e.x},{e.y},width=8,capstyle="round",fill="grey",tags="l{l_n}")',globals())
        wires.append(f'l{l_n}')
        print(wires)
        

    

def wire_motion(e):
    global coords
    x = e.x
    y = e.y
    
    
    if coords != '':
        if abs(e.widget.startX-x) >= abs(e.widget.startY-y):
            eval(f'cnv.coords({wires[-1]},{coords}x,{coords.split(",")[-2]})')
        else:
            eval(f'cnv.coords({wires[-1]},{coords}{coords.split(",")[-3]},y)')

    else:
        if abs(e.widget.startX-x) > abs(e.widget.startY-y):
            eval(f'cnv.coords({wires[-1]},e.widget.startX,e.widget.startY,x,e.widget.startY)')
        else:
            eval(f'cnv.coords({wires[-1]},e.widget.startX,e.widget.startY,e.widget.startX,y)')
    
def wire_remove(e):
    
    exec(f'cnv.delete({wires[-1]})')
    wires.pop(-1)
    cnv.unbind("<Motion>")
cnv.bind("<Button-1>",wire_start)
cnv.bind("<Button-3>",wire_remove)





root.mainloop()
