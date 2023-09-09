# А/В калькулятор

import tkinter as tk
from tkinter import messagebox as mb
import os
import math
from scipy.stats import norm

# Функция форматирования процентов
def num_percent(num):
    return '{:.2f}'.format(num * 100).rjust(10) + '%'

# Функция очистки полей ввода
def clear_all():
    entVisitors1.delete(0, tk.END)
    entVisitors1.insert(tk.END, '0')
    entConversions1.delete(0, 'end')
    entConversions1.insert(tk.END, '0')
    entVisitors2.delete(0, 'end')
    entVisitors2.insert(tk.END, '0')
    entConversions2.delete(0, 'end')
    entConversions2.insert(tk.END, '0')

    # set focus on the entVisitors1 entry box 
    entVisitors1.focus_set()

def do_processing():
    # Считывание данных из полей ввода
    n1 = int(entVisitors1.get())
    c1 = int(entConversions1.get())
    n2 = int(entVisitors2.get())
    c2 = int(entConversions2.get())
    
    # Проверка данных из полей ввода
    if n1 <= 0 or n2 <= 0:
        mb.showerror(title='Ошибка', message='Неверное количество посетителей!')
        return
    
    # Открытие окна результатов
    popup_window(n1, c1, n2, c2)

# Функция вызова окна результата
def popup_window(n1, c1, n2, c2):
    window = tk.Toplevel()
    window.geometry('500x520+685+400')
    window.title('А/В результат')
    window.resizable(False, False)
    
    # Добавление окна вывода текста
    txtOutput = tk.Text(window, font=('Courier New', 10, 'bold'))
    txtOutput.place(x=15, y=125, width=470, height=340)
    
    # Добавление заголовка
    txtOutput.insert(tk.END, '                                 Контрольная    Тестовая' + os.linesep)
    txtOutput.insert(tk.END, '                                 группа         группа' + os.linesep)
    txtOutput.insert(tk.END, '---------------------------------------------------------' + os.linesep)

    # Добавление вывода конверсии и стандартного отклонения
    p1 = c1 / n1
    p2 = c2 / n2
    txtOutput.insert(tk.END, 'Конверсия                     ' + num_percent(p1)
    + '   ' + num_percent(p2) + os.linesep)

    sigma1 = math.sqrt(p1 * (1 - p1) / n1)
    sigma2 = math.sqrt(p2 * (1 - p2) / n2) 
    txtOutput.insert(tk.END, 'Стандартное отклонение        ' + num_percent(sigma1)
    + '   ' + num_percent(sigma2) + os.linesep)
    txtOutput.insert(tk.END, '---------------------------------------------------------' + os.linesep)

    # Добавление вывода возможных разбросов
    z90 = 1.645
    lower1_90 = p1 - z90 * sigma1
    if lower1_90 < 0:
        lower1_90 = 0
    upper1_90 = p1 + z90 * sigma1
    if upper1_90 > 1:
        upper1_90 = 1
    
    lower2_90 = p2 - z90 * sigma2
    if lower2_90 < 0:
        lower2_90 = 0
    upper2_90 = p2 + z90 * sigma2
    if upper2_90 > 1:
        upper2_90 = 1
    
    txtOutput.insert(tk.END, '90% Возможный разброс  ' + os.linesep)
    txtOutput.insert(tk.END, '                   От         ' + num_percent(lower1_90)
    + '   ' + num_percent(lower2_90) + os.linesep)
    txtOutput.insert(tk.END, '                   До         ' + num_percent(upper1_90)
    + '   ' + num_percent(upper2_90) + os.linesep)
    txtOutput.insert(tk.END, '---------------------------------------------------------' + os.linesep)

    z95 = 1.96
    lower1_95 = p1 - z95 * sigma1
    if lower1_95 < 0:
        lower1_95 = 0
    upper1_95 = p1 + z95 * sigma1
    if upper1_95 > 1:
        upper1_95 = 1
    
    lower2_95 = p2 - z95 * sigma2
    if lower2_95 < 0:
        lower2_95 = 0
    upper2_95 = p2 + z95 * sigma2
    if upper2_95 > 1:
        upper2_95 = 1
    
    txtOutput.insert(tk.END, '95% Возможный разброс  ' + os.linesep)
    txtOutput.insert(tk.END, '                   От         ' + num_percent(lower1_95)
    + '   ' + num_percent(lower2_95) + os.linesep)
    txtOutput.insert(tk.END, '                   До         ' + num_percent(upper1_95)
    + '   ' + num_percent(upper2_95) + os.linesep)
    txtOutput.insert(tk.END, '---------------------------------------------------------' + os.linesep)
    
    z99 = 2.575
    lower1_99 = p1 - z99 * sigma1
    if lower1_99 < 0:
        lower1_99 = 0
    upper1_99 = p1 + z99 * sigma1
    if upper1_99 > 1:
        upper1_99 = 1
    
    lower2_99 = p2 - z99 * sigma2
    if lower2_99 < 0:
        lower2_99 = 0
    upper2_99 = p2 + z99 * sigma2
    if upper2_99 > 1:
        upper2_99 = 1
    
    txtOutput.insert(tk.END, '99% Возможный разброс  ' + os.linesep)
    txtOutput.insert(tk.END, '                   От         ' + num_percent(lower1_99)
    + '   ' + num_percent(lower2_99) + os.linesep)
    txtOutput.insert(tk.END, '                   До         ' + num_percent(upper1_99)
    + '   ' + num_percent(upper2_99) + os.linesep)
    txtOutput.insert(tk.END, '---------------------------------------------------------' + os.linesep)
    
    # Вычисление Z и P
    z_score = (p2 - p1) / math.sqrt(sigma1 ** 2 + sigma2 ** 2)
    txtOutput.insert(tk.END, 'Z = ' + '{:.7f}'.format(z_score) + os.linesep)
    
    p_value = norm.sf(x=z_score, loc=0, scale=1)
    txtOutput.insert(tk.END, 'P = ' + '{:.7f}'.format(p_value) + os.linesep)
    
    # Добавление оценки результатов
    confidence_90 = False
    if p_value < 0.05 or p_value > 0.95:
        confidence_90 = True
    
    confidence_95 = False
    if p_value < 0.025 or p_value > 0.975:
        confidence_95 = True
    
    confidence_99 = False
    if p_value < 0.005 or p_value > 0.995:
        confidence_99 = True

    lblComment_90 = tk.Label(window, text='90% уверенность:', font=('Helvetica', 10, 'bold'), fg='#0000cc')
    lblComment_90.place(x=25, y=25)
    
    if confidence_90:
        lblResult_90 = tk.Label(window, text='ДА', font=('Helvetica', 12, 'bold'), fg='#008800')
        lblResult_90.place(x=160, y = 25)
    else:
        lblResult_90 = tk.Label(window, text='НЕТ', font=('Helvetica', 12, 'bold'), fg='#ff0000')
        lblResult_90.place(x=160, y = 25)
    
    lblComment_95 = tk.Label(window, text='95% уверенность:', font=('Helvetica', 10, 'bold'), fg='#0000cc')
    lblComment_95.place(x=25, y=55)
    
    if confidence_95:
        lblResult_95 = tk.Label(window, text='ДА', font=('Helvetica', 12, 'bold'), fg='#008800')
        lblResult_95.place(x=160, y = 55)
    else:
        lblResult_95 = tk.Label(window, text='НЕТ', font=('Helvetica', 12, 'bold'), fg='#ff0000')
        lblResult_95.place(x=160, y = 55)
    
    lblComment_99 = tk.Label(window, text='99% уверенность:', font=('Helvetica', 10, 'bold'), fg='#0000cc')
    lblComment_99.place(x=25, y=85)
    
    if confidence_99:
        lblResult_99 = tk.Label(window, text='ДА', font=('Helvetica', 12, 'bold'), fg='#008800')
        lblResult_99.place(x=160, y = 85)
    else:
        lblResult_99 = tk.Label(window, text='НЕТ', font=('Helvetica', 12, 'bold'), fg='#ff0000')
        lblResult_99.place(x=160, y = 85)
    
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
    btnClosePopup.place(x=185, y=475, width=80, height=30)
    
    # Перевод фокуса на созданное окно
    window.focus_force()

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
                    command=do_processing)
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
