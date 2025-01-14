class Dict:
    def __init__(self, input_dict):
        self.input_dict = input_dict
        self.output_dict = {}

    def get_key_value_item(self):
        for key, value in self.input_dict.items():
            if value is not None:
                self.output_dict[key] = value
        return self.output_dict

input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
my_dict = Dict(input_dict)
output_dict = my_dict.get_key_value_item()
print("Dictionary with Empty Items Dropped:", output_dict)
