class MeanCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        total_sum = 0
        count = 0

        keys = list(self.data.keys())
        index = 0

        while index < len(keys):
            current_key = keys[index]
            total_sum += self.data[current_key]
            count += 1
            index += 1

        if count > 0:
            mean = total_sum / count
            return mean
        else:
            return None

test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
calculator = MeanCalculator(test_dict)
mean_value = calculator.calculate_mean()
print("Mean of the dictionary values is:", mean_value)
