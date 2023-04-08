import random
import tkinter as tk

def randnumb():
    n=random.randint(1,6)
    return
    

def rannum():
    n=random.randint(1,6)
    lbl_result["text"]=n
    return
    
window=tk.Tk()
window.title("Rolling a die!")
window.columnconfigure(0, minsize=250)
window.rowconfigure(0,minsize=150)


btn_say=tk.Button(text="Roll a die", command=rannum)
btn_say.place(x=150,y=150,height=150,width=150)
lbl_result=tk.Label()



btn_say.grid(row=0, column=0,)
lbl_result.grid(row=1, column=0, sticky="s")

window.mainloop()
