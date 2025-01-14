class ListTraverser:
    def __init__(self, original_list):
        self.original_list = original_list

    def traverse_reverse(self):
        index = len(self.original_list) - 1
        while index >= 0:
            current_element = self.original_list[index]
            print(f"Index {index}: {current_element}")
            index -= 1

original_list = ['red', 'green', 'white', 'black']
traverser = ListTraverser(original_list)
print("Traverse the said list in reverse order:")
traverser.traverse_reverse()
