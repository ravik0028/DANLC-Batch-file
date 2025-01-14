class ListSplitter:
    def __init__(self, original_list):
        self.original_list = original_list

    def split_list(self, split_length):
        first_part = []
        second_part = []
        if split_length < 0:
            return "Split length cannot be negative."
        if split_length > len(self.original_list):
            return "Split length exceeds the length of the list."

        index = 0
        while index < len(self.original_list):
            if index < split_length:
                first_part.append(self.original_list[index])
            else:
                second_part.append(self.original_list[index])
            index += 1

        return first_part, second_part

original_list = [1, 1, 2, 3, 4, 4, 5, 1]
split_length = 3
splitter = ListSplitter(original_list)
first_part, second_part = splitter.split_list(split_length)
print("Splitted the said list into two parts:", (first_part, second_part))
