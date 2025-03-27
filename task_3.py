class FlatIterator:

    def __init__(self, list_of_list):
        self.lists = list_of_list

    def __iter__(self):
        self.cursor_main = 0
        self.cursor_help = -1
        return self

    def __next__(self):
        if self.cursor_main == len(self.lists):
            raise StopIteration
        return self.get_str_of_list(self.lists[self.cursor_main])

    def get_str_of_list(self, iter_list):
        if self.cursor_help == len(iter_list):
            cursor_help = 0
            self.cursor_main += 1
        if isinstance(iter_list[self.cursor_help], list):
            self.get_str_of_list(iter_list[self.cursor_help])
        self.cursor_help += 1
        return iter_list[cursor_help]

# def test_3():
#     list_of_lists_2 = [
#         [['a'], ['b', 'c']],
#         ['d', 'e', [['f'], 'h'], False],
#         [1, 2, None, [[[[['!']]]]], []]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_2),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#     ):
#         assert flat_iterator_item == check_item
#
#     assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    # test_3()

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item in FlatIterator(list_of_lists_2):
        print(flat_iterator_item)