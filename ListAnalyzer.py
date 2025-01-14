class ListAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest_and_smallest(self):
        if len(self.numbers) == 0:
            return None, None

        largest = self.numbers[0]
        smallest = self.numbers[0]
        index = 1

        while index < len(self.numbers):
            if self.numbers[index] > largest:
                largest = self.numbers[index]
            if self.numbers[index] < smallest:
                smallest = self.numbers[index]
            index += 1

        return largest, smallest

numbers = [10, 20, 5, 40, 15]
analyzer = ListAnalyzer(numbers)
largest, smallest = analyzer.find_largest_and_smallest()
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)
