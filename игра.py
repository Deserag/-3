from  tkinter import*
from random import *
import pygame
pygame.init()
left=20
a=20
vol= 0.5
pl,pm=0,0
def bot1():
    pygame.mixer.music.pause()
    pygame.mixer.music.load("E:\pythonProject/metal.mp3")
    pygame.mixer.music.play(-1)
    ai_map = [False for _ in range(left)]
    def p1():
        global left, pl
        if pl == 0:
            u = 1
            left = left - int(u)
            if left <= 0:
                sticks.config(text="Компьютер победил")
                sticks.place(x=475, y=70)
            else:
                sticks.config(text=left * "| ")
            pl+=1

    def p2():
        global left, pl
        if pl == 0:
            u = 2
            left = left - int(u)
            if left <= 0:
                sticks.config(text="Компьютер победил")
                sticks.place(x=475, y=70)
            else:
                sticks.config(text=left * "| ")
            pl += 1

    def p3():
        global left, pl
        if pl == 0:
            u = 3
            left = left - int(u)
            if left <= 0:
                sticks.config(text="Компьютер победил")
                sticks.place(x=475, f=70)
            else:
                sticks.config(text=left * "| ")
            pl += 1
    def ps():
        global left,pl
        if pl==1:
            start_cell = 20 - left - 1
            for cell_index in range(20):
                cell = 20 - cell_index - 1
                if 0 < cell_index % (1 + 3) <= 1:
                    ai_map[cell] = True
            for x in range(start_cell, 20):
                if ai_map[x] and 1 <= x - start_cell <= 3:
                    a = x - start_cell
                elif x - start_cell > 3:
                    a = randint(1, 3)
                else:
                    a = randint(1, 3)
            left = left - int(a)
            if left <= 0:
                sticks.config(text="Игрок победил")
                sticks.place(x=140, y=70)
            else:
                sticks.config(text=left * "| ")
            pl-=1
    root = Tk()
    root.geometry("1350x700")
    root.configure(bg='black')
    text1 = Label(root, text="Сколько палочек будем брать ?",bg='black',fg='red')
    text1.config(font=("Calibri", 35, 'bold'))
    text1.pack()
    knopka1 = Button(root, text="1", command=p1,bg='lavender',fg='red')
    knopka1.config(font=("Calibri", 17, 'bold'))
    knopka1.place(x=450, y=230)
    knopka2 = Button(root, text="2", command=p2, bg='lavender',fg='red')
    knopka2.config(font=("Calibri", 17, 'bold'))
    knopka2.place(x=665, y=230)
    knopka3 = Button(root, text="3", command=p3,bg='lavender',fg='red')
    knopka3.config(font=("Calibri", 17, 'bold'))
    knopka3.place(x=900, y=230)
    sticks = Label(root, text=left * "| ")
    sticks.config(font=("Arial", 50, 'bold'), fg='red',bg='black')
    sticks.place(x=325, y=370)
    pc_knopka = Button(root, text="Ход компьютера", command=ps,bg='lavender',fg='red')
    pc_knopka.config(font=("Calibri", 17, 'bold'))
    pc_knopka.place(x=580, y=550)
    root.resizable(0, 0)
    root.title("Палочки")
    root.mainloop()
#  игра со сложным ботом сделана
def bot2():
    pygame.mixer.music.pause()
    pygame.mixer.music.load("E:\pythonProject/dobro.mp3")
    pygame.mixer.music.play(-1)
    def s1():  # первая кнопка
        global a,pm
        if pm==0:
            u = 1
            a = a - int(u)  # проверка количества палочек
            if a <= 0:  #
                sticks.config(text="Компьютер победил")
                sticks.place(x=475, y=70)
            else:
                sticks.config(text=a * "| ")  # удаление выбранных палочек
            pm+=1
    def s2():  # вторая кнопка
        global a,pm
        if pm==0:
            u = 2
            a = a - int(u)
            if a <= 0:  # проверка количества палочек
                sticks.config(text="Компьютер победил")
                sticks.place(x=475, y=70)
            else:
                sticks.config(text=a * "| ")  # показывает количество палочек
            pm+=1
    def s3():
        global a,pm
        if pm==0:
            u = 3
            a = a - int(u)
            if a <= 0:  # проверка количества палочек
                sticks.config(text="Компьютер победил")#
                sticks.place(x=475, y=70)
            else:
                sticks.config(text=a * "| ")  # показывает количество палочек
            pm+=1
    def pc():
        global a,pm
        if pm==1:
            b = randint(1, 3)
            if a == 4:  # Если осталось 4 палочки
                b = 3  # Компьютер убирает 3
            elif a == 3:  # Если осталось 3 палочки
                b = 2  # Компьютер убирает 2
            elif a == 2:  # Если осталось 2 палочки
                b = 1  # Компьютер убирает 1
            a = a - b
            if a <= 0:
                sticks.config(text="Игрок победил")#
                sticks.place(x=140, y=70)
            else:
                sticks.config(text=a * "| ")
            pm-=1
    root = Tk()
    root.geometry("1350x700")#настройка окна
    root.configure(bg='powderblue')
    text1 = Label(root, text="Палочки",bg='powderblue',fg='lawngreen')#настройка текста палочки на поле
    text1.config(font=("Arial", 35, 'bold'))
    text1.pack()
    wbutt1 = Button(root, text="1", command=s1,bg='white', fg='lawngreen')#настройка кнопки 1 палочка  на поле
    wbutt1.config(font=("Arial", 17, 'bold'))
    wbutt1.place(x=450, y=230)
    wbutt2 = Button(root, text="2", command=s2,bg='white', fg='lawngreen')#настройка кнопки 2 палочки  на поле
    wbutt2.config(font=("Arial", 17, 'bold'))
    wbutt2.place(x=665, y=230)
    wbutt3 = Button(root, text="3", command=s3,bg='white', fg='lawngreen')#настройка кнопки 3 палочки  на поле
    wbutt3.config(font=("Arial", 17, 'bold'))
    wbutt3.place(x=900, y=230)
    sticks = Label(root, text=left * "| ",)
    sticks.config(font=("Arial", 50, 'bold'), fg='lawngreen',bg='powderblue')#настройка палочек на поле
    sticks.place(x=325, y=370)
    pc_butt = Button(root, text="Ход компьютера", command=pc,bg='white', fg='lawngreen')# настройка кнопки ход компьютера на поле
    pc_butt.config(font=("Arial", 17, 'bold'))
    pc_butt.place(x=570, y=550)
    root.resizable(0, 0)
    root.title("Палочки")
    root.mainloop()
#2 игра с сложным ботом сделана
def music():
    def bis():
        global vol
        vol+= 0.1
    def min ():
        global vol
        vol-= 0.1
    root = Tk()
    root.geometry("450x300")# настройка окна
    root.configure(bg='white')
    textura1 = Label(root, text="Громкость ",bg='white', fg='lawngreen')#настройка громкоти
    textura1.config(font=("Argial",15))
    textura1.pack()
    gromko= Button(root, text="увеличить громкость",command=bis,bg='white', fg='lawngreen')
    gromko.config(font=("Arial", 14, 'bold'))
    gromko.place(x=125,y=75)# кнопкка на увеличение громкости увеличена
    tixo= Button(root, text="уменьшить громкость",command=min,bg='white', fg='lawngreen')
    tixo.config(font=("Arial", 14, 'bold'))
    tixo.place(x=125, y=150)# кнопка на уменьшение громкости сделана
    # музыка настроена
#настройка громкости
def bot4():
    root = Tk()
    textura1 = Label(root, text="1.на игровом поле присутствует 20 палочек \n 2.игрок может выбрать от 1 до 3 палочек \n 3.после выбора количества палочек, они удаляются с поля \n 4.побеждает тот, кто оставляет одну палочку на поле")
    textura1.pack()
    root.mainloop()
# правила сделаны
pygame.mixer.music.pause()
pygame.mixer.music.load("E:\pythonProject/eva.mp3")
pygame.mixer.music.play(-1)
root = Tk()
root.geometry("350x300")# настройка поля
root.configure(bg='black')
textura1 = Label(root, text="Палочки",bg='orange', fg='white')#
textura1.config(font=("Argial",15, 'bold'))
textura1.pack()
qbutt1 = Button(root, text="Игра с  легким ботом",command= bot2,bg='orange', fg='white')#настройка кнопки игра с легким ботом  на поле
qbutt1.place(x=110, y=50)
qbutt4 = Button(root, text="Игра с умным ботом",command= bot1,bg='orange', fg='white')#настройка кнопки игра с умным ботом  на поле
qbutt4.pack(padx=0, pady=0)
qbutt4.place(x=110, y=100)
wbutt3 = Button(root, text="громкость",command=music,bg='orange', fg='black')#настройка кнопки громкость   на поле
wbutt3.place(x=140, y=150)
qbutt5 = Button(root, text="Правила", command = bot4,bg='orange', fg='black')#настройка кнопки правила на поле
qbutt5.place(x=140, y=200)
root.title("Палочки")
root.mainloop()#запуск окна