from tkinter import *
from time import *

fnameList=["bear.gif", "bee.gif", "cupid.gif", "dog.gif", "dog2.gif", "sun.gif", "sun2.gif", "tractor.gif", "unicorn.gif"]
photoList=[None]*9
num=0

def clickNext() :
    global num
    num+= 1
    if num>8:
        num=0
    photo = PhotoImage(file="C:\\Users\\smh\\Documents\\신명호\\4학년 1학기\\파이썬프로그래밍\\9주차\\.dist\\WindowProgramming\\"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo

def clickPrev() :
    global num
    num-= 1
    if num < 0:
        num=8
    photo = PhotoImage(file="C:\\Users\\smh\\Documents\\신명호\\4학년 1학기\\파이썬프로그래밍\\9주차\\.dist\\WindowProgramming\\"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<<이전", command = clickPrev)
btnNext = Button(window, text = "다음>>", command = clickNext)

photo = PhotoImage(file="C:\\Users\\smh\\Documents\\신명호\\4학년 1학기\\파이썬프로그래밍\\9주차\\.dist\\WindowProgramming\\"+fnameList[0])
pLabel= Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x=15,y=50)

window.mainloop()
