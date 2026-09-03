numbers = [4, 7, 2, 9, 12, 5, 8, 3]
total = 0
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
        total += number ** 2

print("Чётные числа:", even_numbers)
print("Сумма квадратов:", total)
