from tkinter import *
window = Tk()

photo = PhotoImage(file = "C:\\Users\\smh\\Documents\\신명호\\4학년 1학기\\파이썬프로그래밍\\9주차\\.dist\\WindowProgramming\\dog.gif")
label1 = Label(window, image = photo)

label1.pack()
window.mainloop()