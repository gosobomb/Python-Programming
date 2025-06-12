from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "C:\\Users\\smh\\Documents\\신명호\\4학년 1학기\\파이썬프로그래밍\\9주차\\.dist\\WindowProgramming\\dog.gif")
photo2 = PhotoImage(file = "C:\\Users\\smh\\Documents\\신명호\\4학년 1학기\\파이썬프로그래밍\\9주차\\.dist\\WindowProgramming\\dog2.gif")
label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()