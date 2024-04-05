from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()
    def boil_water(self):
        print("Кипятим воду")
    @abstractmethod
    def brew(self):
        pass
    def pour_in_cup(self):
        print("Наливаем в чашку")
    @abstractmethod
    def add_condiments(self):
        pass

class Tea(Beverage):
    def brew(self):           print("Завариваем чай")
    def add_condiments(self): print("Добавляем лимон")

class Coffee(Beverage):
    def brew(self):           print("Завариваем кофе")
    def add_condiments(self): print("Добавляем сахар и молоко")

preference = input("Выберите: Чай или Кофе >> ")
if preference == "Чай":    tea = Tea().prepare_beverage()
elif preference == 'Кофе': coffee = Coffee().prepare_beverage()
else:                      raise ValueError("Напитка не существует")