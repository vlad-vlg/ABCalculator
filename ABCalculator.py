# А/В калькулятор

import tkinter as tk

# Функция закратия программмы
def do_close():
    root.destroy()

# Создание главного окна
root = tk.Tk()
root.geometry('280x300+300+200')
root.title('А/В калькулятор')
root.resizable(False, False)

# Добавление метки заголовка
lblTitle = tk.Label(root, text='А/В калькулятор', font=('Helvetica', 16, 'bold'), fg='#0000cc')
lblTitle.place(x=55, y=15)

# Добавление метки заголовка контрольной группы
lblTitle1 = tk.Label(root, text='Контрольная группа', font=('Helvetica', 12, 'bold'), fg='green')
lblTitle1.place(x=25, y=55)

# Добавление полей вввода контрольной группы
lblVisitors1 = tk.Label(root, text='Посетители:', font=('Helvetica', 10, 'bold'))
lblVisitors1.place(x=25, y=85)
entVisitors1 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='right', bd=3)
entVisitors1.place(x=140, y=85, width=90, height=20)

lblConversions1 = tk.Label(root, text='Конверсии:', font=('Helvetica', 10, 'bold'))
lblConversions1.place(x=25, y=115)
entConversions1 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='right', bd=3)
entConversions1.place(x=140, y=115, width=90, height=20)

# Добавление метки заголовка тестовой группы
lblTitle2 = tk.Label(root, text='Тестовая группа', font=('Helvetica', 12, 'bold'), fg='orange')
lblTitle2.place(x=25, y=145)

# Добавление полей вввода тестовой группы
lblVisitors2 = tk.Label(root, text='Посетители:', font=('Helvetica', 10, 'bold'))
lblVisitors2.place(x=25, y=175)
entVisitors2 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='right', bd=3)
entVisitors2.place(x=140, y=175, width=90, height=20)

lblConversions2 = tk.Label(root, text='Конверсии:', font=('Helvetica', 10, 'bold'))
lblConversions2.place(x=25, y=205)
entConversions2 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='right', bd=3)
entConversions2.place(x=140, y=205, width=90, height=20)

# Добавление кнопки "Рассчитать"
btnProcess = tk.Button(root, text='Рассчитать',
                    font=('Helvetica', 9, 'bold'),
                    bg='snow2',
                    bd=3,
                    activeforeground='navy',
                    activebackground='snow3',
                    relief='raised',
                    overrelief='groove')
btnProcess.place(x=25, y=250, width=80, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text='Закрыть',
                    font=('Helvetica', 9, 'bold'),
                    bg='snow2',
                    bd=3,
                    activeforeground='navy',
                    activebackground='snow3',
                    relief='raised',
                    overrelief='groove',
                    command=do_close)
btnClose.place(x=160, y=250, width=80, height=30)

# Запуск цикла mainloop
root.mainloop()
