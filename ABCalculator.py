# А/В калькулятор

import tkinter as tk

# Функция очистки полей ввода
def clear_all():
    entVisitors1.delete(0, 'end')
    entConversions1.delete(0, 'end')
    entVisitors2.delete(0, 'end')
    entConversions2.delete(0, 'end')

    # set focus on the entVisitors1 entry box 
    entVisitors1.focus()

# Функция добавления окна результата
def popup_window():
    window = tk.Toplevel()
    window.geometry('280x300+685+400')
    window.title('А/В результат')
    window.resizable(False, False)
    # Добавление кнопки закрытия окна
    btnClosePopup = tk.Button(window, text='Закрыть',
                    font=('Helvetica', 9, 'bold'),
                    bg='snow',
                    bd=3,
                    activeforeground='navy',
                    activebackground='snow3',
                    relief='raised',
                    overrelief='groove',
                    command=window.destroy)
    btnClosePopup.place(x=185, y=250, width=80, height=30)

# Функция закрытия программмы
def do_close():
    root.destroy()

# Создание главного окна
root = tk.Tk()
root.geometry('280x300+400+400')
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
entVisitors1 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='center', bd=3)
entVisitors1.place(x=140, y=85, width=100, height=20)
entVisitors1.insert(tk.END, '0')

lblConversions1 = tk.Label(root, text='Конверсии:', font=('Helvetica', 10, 'bold'))
lblConversions1.place(x=25, y=115)
entConversions1 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='center', bd=3)
entConversions1.place(x=140, y=115, width=100, height=20)
entConversions1.insert(tk.END, '0')

# Добавление метки заголовка тестовой группы
lblTitle2 = tk.Label(root, text='Тестовая группа', font=('Helvetica', 12, 'bold'), fg='orange')
lblTitle2.place(x=25, y=145)

# Добавление полей вввода тестовой группы
lblVisitors2 = tk.Label(root, text='Посетители:', font=('Helvetica', 10, 'bold'))
lblVisitors2.place(x=25, y=175)
entVisitors2 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='center', bd=3)
entVisitors2.place(x=140, y=175, width=100, height=20)
entVisitors2.insert(tk.END, '0')

lblConversions2 = tk.Label(root, text='Конверсии:', font=('Helvetica', 10, 'bold'))
lblConversions2.place(x=25, y=205)
entConversions2 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='center', bd=3)
entConversions2.place(x=140, y=205, width=100, height=20)
entConversions2.insert(tk.END, '0')

# Добавление кнопки "Рассчитать"
btnProcess = tk.Button(root, text='Рассчитать',
                    font=('Helvetica', 9, 'bold'),
                    bg='snow',
                    bd=3,
                    activeforeground='navy',
                    activebackground='snow3',
                    relief='raised',
                    overrelief='groove',
                    command=popup_window)
btnProcess.place(x=17, y=250, width=80, height=30)

# Добавление кнопки "Очистить"
btnProcess = tk.Button(root, text='Очистить',
                    font=('Helvetica', 9, 'bold'),
                    bg='snow',
                    bd=3,
                    activeforeground='navy',
                    activebackground='snow3',
                    relief='raised',
                    overrelief='groove',
                    command=clear_all)
btnProcess.place(x=101, y=250, width=80, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text='Закрыть',
                    font=('Helvetica', 9, 'bold'),
                    bg='snow',
                    bd=3,
                    activeforeground='navy',
                    activebackground='snow3',
                    relief='raised',
                    overrelief='groove',
                    command=do_close)
btnClose.place(x=185, y=250, width=80, height=30)

# Запуск цикла mainloop
root.mainloop()
