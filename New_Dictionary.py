class DictionaryProcessor:
    def __init__(self, input_dict):
        self.input_dict = input_dict

    def display_key_value(self):
        count = 1
        for key in self.input_dict:
            value = self.input_dict[key]
            print(f"{count}) {key}: {value}")
            count += 1

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
processor = DictionaryProcessor(dict_num)
processor.display_key_value()
