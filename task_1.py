class FlatIterator:

    def __init__(self, list_of_list):
        self.lists = list_of_list

    def __iter__(self):
        self.cursor_main = 0
        self.cursor_help = -1
        return self

    def __next__(self):
        self.cursor_help += 1
        if self.cursor_help == len(self.lists[self.cursor_main]):
            self.cursor_help = 0
            self.cursor_main += 1
        if self.cursor_main == len(self.lists):
            raise StopIteration

        return self.lists[self.cursor_main][self.cursor_help]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

