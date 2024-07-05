class Drone:  # Класс контроллера полета
    def __init__(self, battery_charge=100):
        self.is_flying = False  # Находится ли дрон в воздухе
        self.battery_charge = battery_charge

    def take_off(self):  # Взлет
        if not self.is_flying and self.battery_charge is not None and self.battery_charge >= 20:
            self.is_flying = True
            print("Готовность на взлет!")
            return "Готовность на взлет!"
        else:
            print("self.battery_charge = ", self.battery_charge)
            if self.battery_charge is None:
                print("Невозможно проверить заряд батареи")
                return "Невозможно проверить заряд батареи"
            elif self.battery_charge < 20:
                self.is_flying = False
                print("Заряд батареи слишком низкий для взлета")
                return "Заряд батареи слишком низкий для взлета"
            else:
                print("Дрон уже летит")
                return "Дрон уже летит"

    def land(self):  # Посадка
        if self.is_flying:
            self.is_flying = False
            print("Дрон уже приземлился")
            return "Дрон уже приземлился"
        else:
            self.is_flying = False
            print("Дрон на земле.")
            return "Дрон на земле"


drone1 = Drone()
print(drone1.take_off())
