import unittest
from datetime import datetime


from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0.9, 0.4, 0.6, 0.1]

        factory = CarFactory()
        car = factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0.3, 0.1, 0.6, 0.1]

        factory = CarFactory()
        car = factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0.9, 0.1, 0.6, 0.1]

        factory = CarFactory()
        car = factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0.4, 0.3, 0.6, 0.1]

        factory = CarFactory()
        car = factory.create_glissade(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        tires_condition = [1, 0, 1, 1]

        factory = CarFactory()
        car = factory.create_palindrome(last_service_date, warning_light_is_on, tires_condition)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        warning_light_is_on = False
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_palindrome(last_service_date, warning_light_is_on, tires_condition)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_palindrome(last_service_date, warning_light_is_on, tires_condition)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_palindrome(last_service_date, warning_light_is_on, tires_condition)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        warning_light_is_on = False
        tires_condition = [1, 1, 1, 1]

        factory = CarFactory()
        car = factory.create_palindrome(last_service_date, warning_light_is_on, tires_condition)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0.8, 0.4, 0.6, 0.1]
        warning_light_is_on = False

        factory = CarFactory()
        car = factory.create_palindrome(last_service_date, warning_light_is_on, tires_condition)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [1, 1, 1, 0]

        factory = CarFactory()
        car = factory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [2, 2, 0.6, 0.1]

        factory = CarFactory()
        car = factory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0.8, 0.4, 0.6, 0.1]

        factory = CarFactory()
        car = factory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_thovex(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_thovex(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_thovex(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tires_condition = [0, 0, 0, 0]

        factory = CarFactory()
        car = factory.create_thovex(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [1, 2, 1, 0]

        factory = CarFactory()
        car = factory.create_thovex(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tires_condition = [1, 1, 0.5, 0.1]

        factory = CarFactory()
        car = factory.create_thovex(last_service_date, current_mileage, last_service_mileage, tires_condition)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
