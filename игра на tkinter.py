from tkinter import *
from tkinter import ttk
import tkinter as tk
import random
from tkinter import messagebox

"""Игра угадай число.
Компьютер число загадывает, пользователь - отгадывает"""

def bin_search(nums: list, n: int):
    """Бинарный поиск"""
    left_index = 0
    right_index = len(nums) - 1
    middle_index = (right_index - left_index) // 2

    while left_index <= right_index:
        guess = nums[middle_index]

        if n == guess:
            return guess
        if n < guess:
            right_index = middle_index-1
            middle_index = left_index + (right_index - left_index) // 2
        if n > guess:
            left_index = middle_index + 1
            middle_index = left_index + (right_index - left_index) // 2


def user_search(computer_number):
    """Функция принимает число компьютера, возвращает результат, когда пользователь отгадает число"""
    global n_iter
    try:

        while True:
            user = int(entry_answer.get())
            x = bin_search(list_user, user)
            n_iter += 1

            if x is None:
                result_label2.config(text="Число не найдено в списке, возможно вы его уже называли")
                break
            if x < computer_number:
                list_user.remove(x)
                result_label2.config(text="больше")
                return
            if x > computer_number:
                list_user.remove(x)
                result_label2.config(text="меньше")
                return
            if x == computer_number:
                messagebox.showinfo("Info", f"Поздравляю!\n"
                                            f"Число {computer_number} угадано с {n_iter} попытки!")
                break

    except ValueError:
        messagebox.showinfo("Info", f"Ведите число!")


def start_game():
    """Функция создает начальные данные для игры, формирует список из чисел и генерирует число компьютера"""
    global list_user, computer_number, n_iter
    n_iter = 0
    try:
        start_user = int(entry_question_len_list1.get())
        end_user = int(entry_question_len_list2.get())
        start = 1
        end = 2


        if start_user > end_user:
            start = end_user
            end = start_user
            result_label.config(text=f"Такой список не существует!\n"
                                     f"Мы составили для вас список от {start} до {end}. "
                                     f"Введите ваше число.")
        elif start_user < end_user:
            start = start_user
            end = end_user
            result_label.config(text="Игра началась! Введите ваше число.")

        elif start_user == 0 and end_user == 0:
            start = 1
            end = 100
            result_label.config(text=f"В списке должна быть как минимум 1 цифра.\n"
                                     f"Мы составили для вас список от {start} до {end}. \n"
                                     f"Введите ваше число.")
        else:
            start = start_user
            end = end_user
            result_label.config(text=f"В списке 1 цифра.\n"
                                     f"Угадать будет не просто \U0001F914, но вы постарайтесь!\n"
                                     f"Введите ваше число.")
        list_user = list(range(start, end + 1))
        computer_number = random.choice(list_user)
    except ValueError:
        messagebox.showinfo("Info", f"Ведите число!")


def show_help():
    """Функция возвращает число компьютера в качестве подсказки"""
    global computer_number
    try:
        messagebox.showinfo("Info", f"Загаданное число: {computer_number}")
    except NameError:
        messagebox.showinfo("Info", f"Игра еще не началась. Нажмите 'Начать игру'.")


window = Tk()
bg = "aliceblue"
window.configure(bg=bg)
window.title("Угадай число")
icon = PhotoImage(file="2.png")
window.iconphoto(False, icon)
window.geometry("880x580+500+150")
window.resizable(False, False)

label_name_game = Label(text="Игра «УГАДАЙ ЧИСЛО»", font=("Arial Black", 22), fg="BLUE", bg=bg)
label_name_game.pack()

label_rules = Label(text="Правила:\nя загадаю число, твоя задача - угадать мое число.\n"
                         "Я буду давать подсказки «больше-меньше»",
                    font=("Arial Black", 18), fg="GREEN3", bg=bg)
label_rules.pack()

label_question_len_list1 = Label(text="С какой цифры или числа начнется список: ",
                                 font=("Arial Black", 18), fg="maroon3", bg=bg)
label_question_len_list1.pack()

entry_question_len_list1 = tk.Entry(window, width=40, font=("Arial Black", 15),
                                    fg="black", bg="white",justify="center")
entry_question_len_list1.pack()

label_question_len_list2 = Label(text="Какой цифрой или числом закончится список: ",
                                 font=("Arial Black", 18), fg="maroon3", bg=bg)
label_question_len_list2.pack()

entry_question_len_list2 = tk.Entry(window, width=40, font=("Arial Black", 15),
                                    fg="black", bg="white", justify="center")
entry_question_len_list2.pack()

button_start_game = Button(text="Начать игру", font=("Arial Black", 15), fg="BLUE", command=start_game, bg=bg)
button_start_game.pack()

label_answer = tk.Label(text="Какое число я загадал?", font=("Arial Black", 18), fg="magenta2", bg=bg)
label_answer.pack()

entry_answer = tk.Entry(window, width=40, font=("Arial Black", 15), fg="black", bg="white", justify="center")
entry_answer.pack()

button_check = Button(text="Проверить", font=("Arial Black", 15), fg="BLUE", bg=bg,
                      command=lambda: user_search(computer_number))
button_check.pack()

result_label = tk.Label(window, text="", font=("Arial Black", 9), fg="GREEN3", bg=bg)
result_label.pack()

result_label2 = tk.Label(window, text="", font=("Arial Black", 12), fg="red", bg=bg)
result_label2.pack()

button_help = Button(text="Если устал отгадывать, то можешь посмотреть, что я загадал", font=("Arial Black", 8),
                     fg="purple3", bg=bg, command=show_help)
button_help.pack(anchor=SE)

window.mainloop()
