from tkinter import *
from tkinter.filedialog import *

window=Tk()
window.geometry("400x100")

label1=Label(window, text="선택된 파일 이름")
label1.pack()

filename=askopenfilename(parent=window, filetypes=(("GIF파일","*.gif"),("모든 파일", "*.*")))
saveFp = asksaveasfile(parent = window, mode = "w", defaultextension=".jpg", filetypes=(("JPG파일","*.jpg"),("모든 파일", "*.*")))
label1.configure(text=str(filename))
saveFp.close()
window.mainloop()