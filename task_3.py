class FlatIterator:

    def __init__(self, list_of_list):
        self.lists = list_of_list

    def __iter__(self):
        self.elements = self.get_str_of_list(self.lists)
        self.cursor_main = -1
        return self

    def __next__(self):
        self.cursor_main += 1
        all_elements = self.elements
        if self.cursor_main == len(all_elements):
            raise StopIteration
        return all_elements[self.cursor_main]

    def get_str_of_list(self, iter_list):
        result = []
        for elem in iter_list:
            if isinstance(elem, list):
                result.extend(self.get_str_of_list(elem))
            else:
                result.append(elem)
        return result


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
