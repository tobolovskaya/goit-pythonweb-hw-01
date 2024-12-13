from typing import Type
import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        car = Car(f"{make} {model}", "(US Spec)")
        logger.info(f"Створено автомобіль: {car.make} {car.model}")
        return car

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        motorcycle = Motorcycle(f"{make} {model}", "(US Spec)")
        logger.info(f"Створено мотоцикл: {motorcycle.make} {motorcycle.model}")
        return motorcycle


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        car = Car(f"{make} {model}", "(EU Spec)")
        logger.info(f"Створено автомобіль: {car.make} {car.model}")
        return car

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        motorcycle = Motorcycle(f"{make} {model}", "(EU Spec)")
        logger.info(f"Створено мотоцикл: {motorcycle.make} {motorcycle.model}")
        return motorcycle


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    us_car = us_factory.create_car("Ford", "Mustang")
    us_car.start_engine()

    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_motorcycle.start_engine()

    eu_car = eu_factory.create_car("Volkswagen", "Golf")
    eu_car.start_engine()

    eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1250")
    eu_motorcycle.start_engine()
