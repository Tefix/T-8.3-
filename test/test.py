from tkinter import *
k=0
def vajutatud():
    global k
    k+=1
    pealkiri.config(text=f"sa vajutasid nuppu! {k} korda", bg="lightgreen", fg="black")
    nupp.config(text="Vajuta mind uuesti!", bg="blue", fg="white")
def vajutatudPK(event):
    global k
    k-=1
    pealkiri.config(text=f"sa vajutasid nuppu! {k} korda", bg="lightgreen", fg="black")
    nupp.config(text="Vajuta mind uuesti!", bg="blue", fg="white")
def tuhista(event):
    sisetus.delete(0, END)
   
    
aken=Tk()
aken.title("Teema 8")
aken.geometry("400x400")
aken.configure(bg="lightblue")
aken.resizable(width=False, height=False)
aken.iconbitmap("pict.ico")
pealkiri=Label(aken, text="Tere tulemast!", bg="white", font=("Arial", 16), fg="black")

nupp=Button(aken, text="Vajuta mind!", bg="green", fg="white", font=("Arial", 12), relief=GROOVE, command=vajutatud)
nupp.bind("<Button-3>",vajutatudPK)
sisetus=Entry(aken, bg="white", font=("Arial", 12), fg="black")
sisetus.insert(0, "Sisesta midagi siia") #END
sisetus.bind("<FocusIn>", tuhista)


pealkiri.pack(pady=20)
nupp.pack(pady=20)
sisetus.pack(pady=20)





aken.mainloop()