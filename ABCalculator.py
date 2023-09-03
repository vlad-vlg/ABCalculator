# А/В калькулятор

import tkinter as tk

# Создание главного окна
root = tk.Tk()
root.geometry('280x300+300+200')
root.title('А/В калькулятор')

# Добавление метки заголовка
lblTitle = tk.Label(root, text='А/В калькулятор', font=('Helvetica', 16, 'bold'), fg='#0000cc')
lblTitle.place(x=55, y=25)

# Запуск цикла mainloop
root.mainloop()
