import tkinter as tk

numbers = [4, 7, 2, 9, 12, 5, 8, 3]


def calculate():
    try:
        numbers = [int(n) for n in entry.get().split()]
        result = sum(n ** 2 for n in numbers if n % 2 == 0)
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка: введите только числа")


root = tk.Tk()
root.title("Парадигмы программирования")

entry = tk.Entry(root)
entry.pack(padx=20, pady=10)

result_label = tk.Label(root, text="Введите числа через пробел")
result_label.pack(padx=20, pady=10)

button = tk.Button(root, text="Вычислить", command=calculate)
button.pack(padx=20, pady=10)

root.mainloop()