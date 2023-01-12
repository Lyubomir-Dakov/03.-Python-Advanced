import unittest


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'


class PersonTests(unittest.TestCase):
    # def setUp(self):
    #     self.person = Person("Luc", "Peterson", 25)
    #
    # def test_get_full_name(self):
    #     result = self.person.get_full_name()
    #     expected_result = "Luc Peterson"
    #     self.assertEqual(result, expected_result)
    #
    # def test_get_info(self):
    #     result = self.person.get_info()
    #     expected_result = "Luc Peterson is 25 years old"
    #     self.assertEqual(result, expected_result)

    def setUp(self):
        self.person_2 = Person('Peter', 'Ivanov', 33)

    def test_get_full_name_2(self):
        result = self.person_2.get_full_name()
        expected_result = 'Peter Ivanov'
        self.assertEqual(expected_result, result)

    def test_get_info_2(self):
        result = self.person_2.get_info()
        expected_result = 'Peter Ivanov is 33 years old'
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
