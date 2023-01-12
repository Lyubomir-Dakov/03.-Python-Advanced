from unittest import TestCase, main
from project.mammal import Mammal


class MammalTest(TestCase):
    def test_if_mammal_initialized_correctly(self):
        mammal = Mammal('Jack', 'Dolphin', 'kiki')
        self.assertEqual('Jack', mammal.name)
        self.assertEqual('Dolphin', mammal.type)
        self.assertEqual('kiki', mammal.sound)
        self.assertEqual('animals', mammal._Mammal__kingdom)

    def test_make_sound_method(self):
        mammal = Mammal('Jack', 'Dolphin', 'kiki')
        self.assertEqual('Jack makes kiki', mammal.make_sound())

    def test_get_kingdom_method(self):
        mammal = Mammal('Jack', 'Dolphin', 'kiki')
        self.assertEqual('animals', mammal.get_kingdom())

    def test_info_method(self):
        mammal = Mammal('Jack', 'Dolphin', 'kiki')
        self.assertEqual("Jack is of type Dolphin", mammal.info())


if __name__ == '__main__':
    main()