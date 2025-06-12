from tkinter import *
from tkinter import messagebox

def myFunc() :
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")

window=Tk()
photo = PhotoImage(file = "C:\\Users\\smh\\Documents\\신명호\\4학년 1학기\\파이썬프로그래밍\\9주차\\.dist\\WindowProgramming\\dog.gif")
button1 = Button(window, image = photo, command = myFunc)

button1.pack()
window.mainloop()