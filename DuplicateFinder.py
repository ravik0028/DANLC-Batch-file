class DuplicateFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_duplicates(self):
        duplicates = []
        seen = []
        index = 0

        while index < len(self.numbers):
            current_number = self.numbers[index]
            if current_number in seen:
                if current_number not in duplicates:
                    duplicates.append(current_number)
            else:
                seen.append(current_number)
            index += 1

        return duplicates

numbers = [10, 20, 30, 10, 40, 20, 50, 30]
finder = DuplicateFinder(numbers)
duplicates = finder.find_duplicates()
print("Duplicate values in the list are:", duplicates)
