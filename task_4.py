import types


def flat_generator(list_of_list):
    cursor = 0
    elements = get_elem_of_list(list_of_list)
    while cursor < len(elements):
        yield elements[cursor]
        cursor += 1

def get_elem_of_list(iter_list):
    result = []
    for elem in iter_list:
        if isinstance(elem, list):
            result.extend(get_elem_of_list(elem))
        else:
            result.append(elem)
    return result

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
