from tkinter import *
from tkinter import messagebox

def shift_arrow(event, direction):
    messagebox.showinfo("키보드 이벤트", f"눌린 키 : Shift + {direction} 화살표")

window = Tk()
window.title("Shift + 방향키 이벤트")
window.geometry("300x200")

window.bind("<Shift-Up>", lambda e: shift_arrow(e, "위쪽"))
window.bind("<Shift-Down>", lambda e: shift_arrow(e, "아래쪽"))
window.bind("<Shift-Left>", lambda e: shift_arrow(e, "왼쪽"))
window.bind("<Shift-Right>", lambda e: shift_arrow(e, "오른쪽"))

window.mainloop()