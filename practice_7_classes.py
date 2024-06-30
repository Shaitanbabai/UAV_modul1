# взлет и посадка, управление скоростью, работа с ГПС, маршрут
#
class Drone:  # basic class for drones
    def __init__(self, drone_id="ABC729",
                 max_altitude=300,
                 max_speed=50,
                 flight_time=30,
                 weight=1.5):
        self.__drone_id = drone_id
        self.__max_altitude = max_altitude
        self.__max_speed = max_speed
        self.__flight_time = flight_time
        self.__weight = weight
        self.__cur_altitude = 0
        self.__cur_speed = 0
        self.__cur_coord = (0.0, 0.0)
        self.__flight_path = []

    def set_max_altitude(self, max_altitude: float):
        if 0 < max_altitude < 3000:
            self.__max_altitude = max_altitude
        else:
            raise ValueError("Wrong max height value")

    def get_max_altitude(self):
        return self.__max_altitude

    def set_max_speed(self, max_speed: float):
        if 0 < max_speed < 100:
            self.__max_altitude = max_speed
        else:
            raise ValueError("Wrong max height value")

    def get_max_speed(self):
        return self.__max_speed

    def set_flight_time(self, flight_time: int):
        if 0 < flight_time < 45:
            self.__flight_time = flight_time
        else:
            raise ValueError("Wrong max height value")

    def get_flight_time(self):
        return self.__flight_time

# Добавление методов для управления полетом
    def set_cur_altitude(self, altitude):
        if 0 < altitude <= self.__max_altitude:
            self.__cur_altitude = altitude
        else:
            raise ValueError(f"Height must be in  range 0 - {self.__max_altitude}")

    def get_flight_path(self):
        return self.__flight_path

    def add_waypoint(self, coord: tuple):
        self.__flight_path.append(coord)
        print(f"New waypoint added: {self.__flight_path[-1]}")
        # -1 возвращает последнюю добавленную точку

    def set_cur_coord(self, coord: tuple):
        self.__cur_coord = coord

    def get_cur_coord(self):
        return self.__cur_coord

    def follow_flight_path(self):
        if not self.__flight_path:  # if self.__flight_path != []:
            print("Route not set")
            return
        print(f"{self.__drone_id} began to follow the route")
        for waypoint in self.__flight_path:
            self.set_cur_coord(waypoint)  # добавляем установку координат
            print(f"Reached waypoint: {self.__cur_coord}")


class ProfessionalDrone(Drone):
    def __init__(self, drone_id="ABC729",
                 max_altitude=300,
                 max_speed=50,
                 flight_time=30,
                 weight=1.5):
        super().__init__(drone_id, max_altitude, max_speed, flight_time, weight)
        # super задает наследование от материнского класса
        self.__night_vision = True
        # нужно задать свои геттеры и сеттеры для этого метода в этом классе


if __name__ == "__main__":  # Тест, все тесты пишем внутри этого условия
    # он не влияет на исполнение основного кода
    drone1 = Drone(drone_id="Test01", flight_time=35)
    print(drone1.__dict__)
    print(drone1.get_max_altitude())
    drone1.set_max_altitude(350)
    print(drone1.get_max_altitude())
    drone1.set_cur_coord((55.7558, 37.6176))
    drone1.add_waypoint((48.858844, 2.294351))

    drone1.follow_flight_path()
