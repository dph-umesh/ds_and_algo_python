from .dynamic_array import DynamicArray


def test_1():
    array = DynamicArray()
    assert len(array) == 0

    array.append(4)
    array.append(5)
    assert len(array) == 2


def test_2():
    array = DynamicArray()
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    array.append(5)
    assert len(array) == 5

    array.insert_at(index=3, value=8)
    assert len(array) == 6
    assert str(array) == "1, 2, 3, 8, 4, 5"


def test_3():
    array = DynamicArray()
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    array.append(5)
    assert len(array) == 5

    popped_value = array.pop()
    assert popped_value == 5

    popped_value = array.pop()
    assert popped_value == 4
    assert len(array) == 3

    array.append(4)
    array.append(5)
    assert str(array) == "1, 2, 3, 4, 5"

    array.remove_at(index=2)
    assert len(array) == 4
    assert str(array) == "1, 2, 4, 5"
