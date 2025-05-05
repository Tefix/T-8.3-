from tkinter import *
def answer1():
    try:
       
        a = float(num1.get())
        b = float(num2.get())
        c = float(num3.get())

        # Вычисляем дискриминант
        d = b ** 2 - 4 * a * c

        # Если D > 0 — два корня
        if d > 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            giveanswer.config(
                text=f"D = {d:.2f} > 0\nУравнение имеет 2 корня:\nX₁ = {x1:.2f}\nX₂ = {x2:.2f}",
                bg="lightgreen", fg="black"
            )

        # Если D == 0 — один корень
        elif d == 0:
            x = -b / (2 * a)
            giveanswer.config(
                text=f"D = {d:.2f} = 0\nУравнение имеет 1 корень:\nX = {x:.2f}",
                bg="lightyellow", fg="black"
            )

        # Если D < 0 — нет норм корней
        else:
            giveanswer.config(
                text=f"D = {d:.2f} < 0\nУравнение не имеет норм корней",
                bg="salmon", fg="black"
            )

    except ValueError:
        giveanswer.config(
            text="Ошибка! Введите только числа!",
            bg="red", fg="white"
        )
    except ZeroDivisionError:
        giveanswer.config(
            text="Ошибка! Коэффициент a не может быть 0!",
            bg="red", fg="white"
        )
aken=Tk()
aken.title("Ruutvõrrandi lahendamine")
aken.geometry("800x300")
aken.configure(bg="lightblue")
aken.resizable(width=False, height=False)
aken.iconbitmap("Funny.ico")
pealkiri=Label(aken, text="Tere tulemast!", bg="white", font=("Arial", 16), fg="black")


invis=Label(aken, text="        ", bg="lightblue", font=("Arial", 16), fg="lightblue") #отступ от края экрана для первого поля
num1=Entry(aken, bg="white", font=("Arial", 15), width=3, fg="black")
x=Label(aken, text="  x**2  ", bg="lightblue", font=("Arial", 16), fg="green")
num2=Entry(aken, bg="white", font=("Arial", 15), width=3, fg="black")
xx=Label(aken, text="  x+  ", bg="lightblue", font=("Arial", 16), fg="green")
num3=Entry(aken, bg="white", font=("Arial", 15), width=3, fg="black")
x0=Label(aken, text="  =0  ", bg="lightblue", font=("Arial", 16), fg="green")
answer=Button(aken, text="Решить", bg="green", fg="white", font=("Arial", 12), relief=GROOVE, command=answer1)
giveanswer=Label(aken, text="Решение", bg="white", font=("Arial", 16), fg="black")





pealkiri.pack(pady=20,)
giveanswer.pack(pady=20,)
invis.pack(pady=20, side=LEFT)
num1.pack(pady=20, side=LEFT)
x.pack(pady=20, side=LEFT)
num2.pack(pady=20, side=LEFT)
xx.pack(pady=20, side=LEFT)
num3.pack(pady=20, side=LEFT)
x0.pack(pady=20, side=LEFT)
answer.place(x=360, y=240,)

aken.mainloop()