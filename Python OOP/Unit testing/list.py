class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):
    def test_if_list_is_initiated_correctly(self):
        int_list = IntegerList('23', 5, 8, 'Alo')
        self.assertEqual([5, 8], int_list._IntegerList__data)

    def test_if_list_data_is_empty(self):
        int_list = IntegerList()
        self.assertEqual([], int_list._IntegerList__data)

    def test_add_operation_if_add_element_to_data(self):
        int_list = IntegerList()
        self.assertEqual([], int_list._IntegerList__data)
        int_list.add(5)
        self.assertEqual([5], int_list._IntegerList__data)

    def test_add_not_an_integer_raise(self):
        int_list = IntegerList()
        with self.assertRaises(ValueError) as ex:
            int_list.add('ho')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index(self):
        int_list = IntegerList()
        self.assertEqual([], int_list._IntegerList__data)
        int_list.add(5)
        int_list.add(10)
        self.assertEqual([5, 10], int_list._IntegerList__data)
        int_list.remove_index(1)
        self.assertEqual([5], int_list._IntegerList__data)

    def test_if_remove_index_is_invalid_index(self):
        int_list = IntegerList()
        self.assertEqual([], int_list._IntegerList__data)
        int_list.add(5)
        int_list.add(10)
        with self.assertRaises(IndexError) as ex:
            int_list.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_init_takes_only_integers(self):
        int_list = IntegerList('5', 'ho', 7, 9)
        self.assertEqual([7, 9], int_list._IntegerList__data)

    def test_if_get_function_returns_the_specific_elemnet(self):
        int_list = IntegerList()
        self.assertEqual([], int_list._IntegerList__data)
        int_list.add(5)
        int_list.add(10)
        self.assertEqual(5, int_list.get(0))

    def test_get_function_receive_invalid_index(self):
        int_list = IntegerList()
        self.assertEqual([], int_list._IntegerList__data)
        int_list.add(5)
        int_list.add(10)
        with self.assertRaises(IndexError) as ex:
            int_list.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_when_receive_integer(self):
        int_list = IntegerList()
        self.assertEqual([], int_list._IntegerList__data)
        int_list.add(7)
        int_list.insert(0, 5)
        self.assertEqual([5, 7], int_list._IntegerList__data)

    def test_insert_when_receive_invalid_index(self):
        int_list = IntegerList()
        self.assertEqual([], int_list._IntegerList__data)
        int_list.add(7)
        with self.assertRaises(IndexError) as ex:
            int_list.insert(3, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_when_receive_invalid_element(self):
        int_list = IntegerList()
        self.assertEqual([], int_list._IntegerList__data)
        int_list.add(7)
        with self.assertRaises(ValueError) as ex:
            int_list.insert(0, 'ho')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest_returns_the_biggest_number(self):
        int_list = IntegerList(5, 7, 13)
        self.assertEqual([5, 7, 13], int_list._IntegerList__data)
        int_list.get_biggest()
        self.assertEqual(13, int_list.get_biggest())

    def test_get_index(self):
        int_list = IntegerList(5, 7, 13)
        self.assertEqual([5, 7, 13], int_list._IntegerList__data)
        self.assertEqual(1, int_list.get_data().index(7))

    def test_get_index_if_received_element_is_not_in_the_list_raise(self):
        int_list = IntegerList(5, 7, 13)
        self.assertEqual([5, 7, 13], int_list._IntegerList__data)
        with self.assertRaises(ValueError) as ex:
            int_list.get_index(8)
        self.assertEqual("8 is not in list", str(ex.exception))


if __name__ == '__main__':
    main()

