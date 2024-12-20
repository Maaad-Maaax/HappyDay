import time
import tkinter as tk
from tkinter import ttk
from datetime import datetime


def main():
    # Определяем текущую дату
    dt_now = datetime.today()
    # Текущая дата в формате dd.mm.yyyy
    dt_now_form = dt_now.strftime("%d.%m.%Y")
    dt_str = str(dt_now_form)
    # Объявляем пустой список для будущего вывода в окно
    out = list()
    # Построчно считываем файл с данными о сотрудниках
    with open("D:/Mirror/Рабочий стол/Исходники HAPPY_DAY/happy_day.txt", encoding="utf-8") as happy_files:
        mas_happy = happy_files.readlines()
        happy_files.close()
    # Перебираем список сотрудников
    for collaborator in mas_happy:
        # Разбиваем элемент на два ФИО и дата
        collaborator = collaborator.split(sep=',')
        # Удаляем лишние символы (пробелы и переносы строк)
        collaborator[1] = collaborator[1].strip().rstrip('\n')
        # Формируем список для вывода
        out.append(collaborator)
    # Механизм вывода уведомления
    if dt_str[:5] in str(out):
        happy_window = tk.Tk()
        # Скрыть шапку окна
        happy_window.overrideredirect(True)
        # Вывод окна на передний план
        happy_window.attributes('-topmost', True)
        # После этого отменяем вывод на передний план
        happy_window.attributes('-topmost', False)
        # Задаем прозрачность окна приложения
        happy_window.attributes('-alpha', 0.85)  # Задание прозрачности окна приложения

        # Запускаем анимацию
        cnt = 10
        frames = [tk.PhotoImage(file='//srv1/Happy_day/salute.gif',
                                format='gif -index %i' % i) for i in range(cnt)]

        # Функция вывода анимации
        def update(ind):
            time.sleep(0.1)
            frame = frames[ind]
            ind += 1
            if ind == cnt:
                ind = 0
            label_img.configure(image=frame)
            happy_window.after(100, update, ind)
        # Вывод поля анимации
        label_img = tk.Label(happy_window)
        label_img.pack()
        happy_window.after(0, update, 0)
        # Вывод окна с текстом
        label = tk.Label(happy_window,
                         text='Сегодня, ' + dt_str[:5] + ' свой день рождения празднует:',
                         fg='#ED3CCA',
                         font=('Comic Sans MS', 20),
                         padx=50,
                         pady=0)
        label.pack()
        for greeting in out:
            if dt_str[:5] in greeting[1]:
                label = tk.Label(happy_window,
                                 text=greeting[0] + '!',
                                 fg='#0000FF',
                                 font=('Comic Sans MS', 22),
                                 padx=50,
                                 pady=0)
                label.pack()
                label = tk.Label(happy_window,
                                 text=greeting[2],
                                 fg='#79553D',
                                 font=('Comic Sans MS', 14, 'underline'),
                                 padx=50,
                                 pady=0)
                label.pack()
        # Отрисовка кнопки
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Fancy.TButton", font=("Comic Sans MS", 12), foreground="white", background="green")
        style.map('Fancy.TButton', background=[('active', 'blue'), ('!disabled', "green")],
                  foreground=[('active', 'white'), ('!disabled', "white")])
        button = ttk.Button(happy_window,
                            text="Ура!",
                            style="Fancy.TButton",
                            cursor='hand2',
                            command=happy_window.destroy)
        button.pack(expand=True, pady=20)
        # Делаем центровку
        happy_window.update()
        x = (happy_window.winfo_screenwidth() - happy_window.winfo_reqwidth()) / 2
        y = (happy_window.winfo_screenheight() - happy_window.winfo_reqheight()) / 2
        happy_window.wm_geometry("+%d+%d" % (x, y))
        happy_window.mainloop()


if __name__ == "__main__":
    main()

