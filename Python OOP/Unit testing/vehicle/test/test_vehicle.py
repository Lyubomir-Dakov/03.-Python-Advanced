from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def test_if_vehicle_is_initialized_correct(self):
        vehicle = Vehicle(40, 300)
        self.assertEqual(40, vehicle.fuel)
        self.assertEqual(40, vehicle.capacity)
        self.assertEqual(300, vehicle.horse_power)
        self.assertEqual(1.25, vehicle.fuel_consumption)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_vehicle_drive_and_decrease_fuel(self):
        vehicle = Vehicle(40, 300)
        self.assertEqual(40, vehicle.fuel)
        vehicle.drive(10)
        self.assertEqual(27.5, vehicle.fuel)
        vehicle.drive(15)
        self.assertEqual(8.75, vehicle.fuel)

    def test_vehicle_drive_not_enough_fuel_raise(self):
        vehicle = Vehicle(5, 300)
        with self.assertRaises(Exception) as ex:
            vehicle.drive(50)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_vehicle_refuel_with_proper_amount_of_fuel(self):
        vehicle = Vehicle(40, 300)
        self.assertEqual(40, vehicle.fuel)
        vehicle.drive(25)
        self.assertEqual(8.75, vehicle.fuel)
        vehicle.refuel(5)
        self.assertEqual(13.75, vehicle.fuel)
        vehicle.refuel(7)
        self.assertEqual(20.75, vehicle.fuel)

    def test_vehicle_refuel_with_more_than_the_capacity(self):
        vehicle = Vehicle(40, 300)
        self.assertEqual(40, vehicle.fuel)
        vehicle.drive(25)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(50)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_vehicle_string_representation(self):
        vehicle = Vehicle(40, 300)
        self.assertEqual(f"The vehicle has {vehicle.horse_power} horse power with {vehicle.fuel} fuel left and {vehicle.fuel_consumption} fuel consumption", vehicle.__str__())


if __name__ == '__main__':
    main()