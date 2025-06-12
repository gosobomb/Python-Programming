from tkinter import *
window = Tk()

label1 = Label(window, text="COOKBOOK~~ Python을")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text="공부 중입니다.", bg="magenta", width=20, height=5, anchor=SE)
# Lable() 함수가 레이블을 만들어줌
# pack() 함수로 해당 레이블 화면 표시
# text : 내용
# font : 글꼴과 크기 지정
# fg : foreground약어로 글자색 지정
# bg : background약어로 배경색 지정
# width, height : 위젯의 폭과 높이 지정
# anchor : 위젯이 어느 위치에 자리 잡을지 결정

label1.pack()
label2.pack()
label3.pack()

window.mainloop()