class NumberCollection:
    def __init__(self, numbers: list[int]):
        self._numbers = list(numbers)

    def get_even_numbers(self) -> list[int]:
        return [n for n in self._numbers if n % 2 == 0]

    def sum_even_squares(self) -> int:
        total = 0
        for number in self._numbers:
            if number % 2 == 0:
                total += number ** 2
        return total

    def count_even_numbers(self) -> int:
        return len(self.get_even_numbers())

    def find_maximum(self) -> int:
        return max(self._numbers)

    def calculate_average(self) -> float:
        return sum(self._numbers) / len(self._numbers)


collection = NumberCollection([4, 7, 2, 9, 12, 5, 8, 3])

print(collection.get_even_numbers())
print(collection.sum_even_squares())
print(collection.count_even_numbers())
print(collection.find_maximum())
print(collection.calculate_average())

collection2 = NumberCollection([10, 15, 20, 25, 30])

print(collection2.get_even_numbers())
print(collection2.sum_even_squares())
print(collection2.count_even_numbers())
print(collection2.find_maximum())
print(collection2.calculate_average())