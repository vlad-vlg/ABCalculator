# А/В калькулятор

import tkinter as tk

# Функция закратия программмы
def do_close():
    root.destroy()

# Создание главного окна
root = tk.Tk()
root.geometry('280x300+300+200')
root.title('А/В калькулятор')

# Добавление метки заголовка
lblTitle = tk.Label(root, text='А/В калькулятор', font=('Helvetica', 16, 'bold'), fg='#0000cc')
lblTitle.place(x=55, y=20)

# Добавление кнопки "Рассчитать"
btnProcess = tk.Button(root, text='Рассчитать', font=('Helvetica', 10, 'bold'), activebackground='gray85',)
btnProcess.place(x=25, y=250, width=90, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text='Закрыть', font=('Helvetica', 10, 'bold'), activebackground='gray85', command=do_close)
btnClose.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
