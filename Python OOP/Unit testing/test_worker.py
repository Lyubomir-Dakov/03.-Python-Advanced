class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_if_workers_is_initialized_correctly(self):
        # Arrange and Act
        worker = Worker('Gosho', 100, 10)

        # Assert
        self.assertEqual('Gosho', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_if_worker_energy_is_incremented_after_rest(self):
        worker = Worker('Gosho', 100, 10)
        self.assertEqual(10, worker.energy)

        worker.rest()
        self.assertEqual(11, worker.energy)

    def test_worker_can_not_work_with_0_energy_raises(self):
        worker = Worker('Gosho', 100, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_can_not_work_with_negative_energy(self):
        worker = Worker('Gosho', 100, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_workers_salary_is_increased_after_work(self):
        worker = Worker('Gosho', 100, 5)
        worker.work()
        self.assertEqual(100, worker.money)
        worker.work()
        self.assertEqual(200, worker.money)

    def test_if_worker_energy_is_decreased_after_work(self):
        worker = Worker('Gosho', 100, 5)
        worker.work()
        self.assertEqual(4, worker.energy)
        worker.work()
        self.assertEqual(3, worker.energy)

    def test_if_get_info_returns_the_proper_string(self):
        worker = Worker('Gosho', 100, 5)
        self.assertEqual('Gosho has saved 0 money.', worker.get_info())
        worker.work()
        self.assertEqual('Gosho has saved 100 money.', worker.get_info())


if __name__ == '__main__':
    main()




