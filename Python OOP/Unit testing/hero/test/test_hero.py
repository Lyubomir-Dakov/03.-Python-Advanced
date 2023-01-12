from project.hero import Hero
from unittest import TestCase, main


# class Hero:
#     username: str
#     health: float
#     damage: float
#     level: int
#
#     def __init__(self, username: str, level: int, health: float, damage: float):
#         self.username = username
#         self.level = level
#         self.health = health
#         self.damage = damage
#
#     def battle(self, enemy_hero):
#         if enemy_hero.username == self.username:
#             raise Exception("You cannot fight yourself")
#
#         if self.health <= 0:
#             raise ValueError("Your health is lower than or equal to 0. You need to rest")
#
#         if enemy_hero.health <= 0:
#             raise ValueError(f"You cannot fight {enemy_hero.username}. He needs to rest")
#
#         player_damage = self.damage * self.level
#         enemy_hero_damage = enemy_hero.damage * enemy_hero.level
#
#         self.health -= enemy_hero_damage
#         enemy_hero.health -= player_damage
#
#         if self.health <= 0 and enemy_hero.health <= 0:
#             return "Draw"
#
#         if enemy_hero.health <= 0:
#             self.level += 1
#             self.health += 5
#             self.damage += 5
#             return "You win"
#
#         enemy_hero.level += 1
#         enemy_hero.health += 5
#         enemy_hero.damage += 5
#         return "You lose"
#
#     def __str__(self):
#         return f"Hero {self.username}: {self.level} lvl\n" \
#                f"Health: {self.health}\n" \
#                f"Damage: {self.damage}\n"


class HeroTest(TestCase):
    def test_if_hero_is_initialized_correctly(self):
        hero = Hero('Don', 10, 100.0, 25.5)
        self.assertEqual('Don', hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(25.5, hero.damage)

    def test_if_hero_tries_to_fight_himself_raise(self):
        hero_1 = Hero('Don', 10, 100.0, 25.5)
        hero_2 = Hero('Don', 10, 150, 70)
        with self.assertRaises(Exception) as ex:
            hero_1.battle(hero_2)
        self.assertEqual("You cannot fight yourself", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            hero_1.battle(hero_1)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_hero_need_to_rest_because_health_is_0_raise(self):
        hero_1 = Hero('Don', 10, 0, 25.5)
        hero_2 = Hero('Kik', 10, 150, 70)
        with self.assertRaises(ValueError) as ex:
            hero_1.battle(hero_2)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_if_hero_need_to_rest_because_health_is_megative_raise(self):
        hero_1 = Hero('Don', 10, -5, 25.5)
        hero_2 = Hero('Kik', 10, 150, 70)
        with self.assertRaises(ValueError) as ex:
            hero_1.battle(hero_2)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_if_enemy_hero_need_to_rest_because_his_health_is_0_raise(self):
        hero_1 = Hero('Don', 10, 100, 25.5)
        hero_2 = Hero('Kik', 10, 0, 70)
        with self.assertRaises(ValueError) as ex:
            hero_1.battle(hero_2)
        self.assertEqual(f"You cannot fight Kik. He needs to rest", str(ex.exception))

    def test_if_enemy_hero_need_to_rest_because_his_health_is_negative_raise(self):
        hero_1 = Hero('Don', 10, 100, 25.5)
        hero_2 = Hero('Kik', 10, -5, 70)
        with self.assertRaises(ValueError) as ex:
            hero_1.battle(hero_2)
        self.assertEqual(f"You cannot fight Kik. He needs to rest", str(ex.exception))

    def test_hero_health_after_fighting(self):
        hero_1 = Hero('Don', 10, 100, 10)
        hero_2 = Hero('Kik', 10, 150, 5)
        hero_1.battle(hero_2)
        self.assertEqual(50, hero_1.health)

    def test_enemy_hero_health_after_fighting(self):
        hero_1 = Hero('Don', 10, 100, 10)
        hero_2 = Hero('Kik', 10, 150, 5)
        hero_1.battle(hero_2)
        self.assertEqual(55, hero_2.health)

    def test_if_both_heroes_have_zero_health_after_battle(self):
        hero_1 = Hero('Don', 10, 100, 10)
        hero_2 = Hero('Kik', 10, 100, 10)
        self.assertEqual('Draw', hero_1.battle(hero_2))
        self.assertEqual(0, hero_1.health)
        self.assertEqual(0, hero_2.health)

    def test_if_both_heroes_have_negative_health(self):
        hero_1 = Hero('Don', 10, 100, 200)
        hero_2 = Hero('Kik', 10, 100, 20)
        self.assertEqual('Draw', hero_1.battle(hero_2))

    def test_if_hero_wins_after_battle(self):
        hero_1 = Hero('Don', 10, 100, 20)
        hero_2 = Hero('Kik', 10, 100, 5)
        self.assertEqual('You win', hero_1.battle(hero_2))
        self.assertEqual(11, hero_1.level)
        self.assertEqual(55, hero_1.health)
        self.assertEqual(25, hero_1.damage)

    def test_if_enemy_hero_wins_battle(self):
        hero_1 = Hero('Don', 10, 100, 5)
        hero_2 = Hero('Kik', 10, 100, 20)
        self.assertEqual('You lose', hero_1.battle(hero_2))
        self.assertEqual(11, hero_2.level)
        self.assertEqual(55, hero_2.health)
        self.assertEqual(25, hero_2.damage)

    def test_string_representation(self):
        hero_1 = Hero('Don', 10, 100, 5)
        self.assertEqual(f"Hero {hero_1.username}: {hero_1.level} lvl\nHealth: {hero_1.health}\nDamage: {hero_1.damage}\n", hero_1.__str__())


if __name__ == '__main__':
    main()
