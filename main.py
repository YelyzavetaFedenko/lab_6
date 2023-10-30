# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.


class Transport:
    # введіть свій код тут
    speed = 0
    power = 0
    name = ""

    def __init__(self, name, start_speed=0, start_power=0):
        self.speed = start_speed
        self.power = start_power
        self.name = name

    def accelerate(self, speed):
        self.speed = self.speed + speed


class Car(Transport):
    fuel = 0

    def __init__(self, name, start_speed=0, start_power=0, start_fuel=0):
        super().__init__(name, start_speed, start_power)
        self.fuel = start_fuel

    def __str__(self):
        return f" «{self.name}» has Speed: {self.speed}, Power: {self.power}, and Fuel: {self.fuel}"


class Bicycle(Transport):
    pedals_count = 0

    def __init__(self, name, start_speed=0, start_power=0, start_pedals_count=2):
        super().__init__(name, start_speed, start_power)
        self.pedals_count = start_pedals_count

    def __str__(self):
        return f" «{self.name}» has Speed: {self.speed}, Power: {self.power}, and Pedals Count: {self.pedals_count}"


print(f"Hello! You have 2 available transports:")
yellow_car = Car("Yellow Car", 72, 100, 40)
red_bicycle = Bicycle("Red Bicycle", 5, 10, 2)
print(f"{yellow_car} \n{red_bicycle}")

yellow_car.fuel = 30
red_bicycle.pedals_count = 4

print(f"Opps, sorry you got wrong information. Here is the right one: \n{yellow_car} \n{red_bicycle}")
print("Do you want to accelerate your vehicles by 5 km/h? [Yes/No]")

while True:
    answer = input()

    if answer.lower() == "yes" or answer.lower() == "y":
        yellow_car.accelerate(5)
        red_bicycle.accelerate(5)
        print(f"{yellow_car} \n{red_bicycle}")
        break
    elif answer.lower() == "no" or answer.lower() == "n":
        print("Okay then, have a good day.")
        break
    else:
        print("Please enter Yes or No.")
