class ListSummer:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum_items(self):
        total_sum = 0
        index = 0
        while index < len(self.numbers):
            if isinstance(self.numbers[index], (int, float)):
                total_sum += self.numbers[index]
            index += 1
        return total_sum

numbers = [10, 20, 30, 40, 50]
summer = ListSummer(numbers)
result = summer.sum_items()
print("The sum of all items in the list is:", result)
