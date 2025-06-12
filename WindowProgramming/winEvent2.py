from tkinter import *
from tkinter import messagebox

def clickImage(event) :
    messagebox.showinfo("마우스", "강아지에서 마우스가 클릭됨")

window = Tk()
window.geometry("400x400")

photo=PhotoImage(file="C:\\Users\\smh\\Documents\\신명호\\4학년 1학기\\파이썬프로그래밍\\9주차\\.dist\\WindowProgramming\\dog.gif")
label1 = Label(window, image=photo)

window.bind("<Button>", clickImage)

label1.pack(expand=1, anchor= CENTER)
window.mainloop()