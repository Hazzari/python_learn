from __future__ import annotations
from abc import ABC, abstractmethod


class CarsFactory(ABC):

    @abstractmethod
    def create_sedan(self):
        pass

    @abstractmethod
    def create_coupe(self):
        pass


class ToyotaFactory(CarsFactory):
    def create_sedan(self):
        return ToyotaSedan()

    def create_coupe(self):
        return ToyotaCoupe()


class FordFactory(CarsFactory):
    def create_sedan(self) -> Sedan:
        return FordSedan()

    def create_coupe(self):
        return FordCoupe()


class Sedan(ABC):
    @abstractmethod
    def create_sedan(self) -> str:
        pass


class Coupe(ABC):
    @abstractmethod
    def create_coupe(self) -> str:
        pass


class FordSedan(Sedan):
    def create_sedan(self) -> str:
        return 'Форд седан!'


class FordCoupe(Sedan):
    def create_sedan(self) -> str:
        return 'Форд купе!'
