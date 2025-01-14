class DictionaryConcatenator:
    def __init__(self, *dicts):
        self.dicts = dicts

    def concatenate_dicts(self):
        concatenated_dict = {}
        index = 0

        while index < len(self.dicts):
            current_dict = self.dicts[index]
            for key in current_dict:
                concatenated_dict[key] = current_dict[key]
            index += 1

        return concatenated_dict

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
concatenator = DictionaryConcatenator(dic1, dic2, dic3)
result = concatenator.concatenate_dicts()
print("Concatenated Dictionary:", result)
