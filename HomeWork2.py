class Camera:  # Класс для камеры
    def __init__(self, resolution, fps):  # Инициализация камеры
        self.resolution = resolution  # Разрешение камеры
        self.fps = fps  # Кадровая частота камеры

    def capture_image(self):  # Метод захвата изображения
        print(f"Захват изображения с разрешением {self.resolution} и частотой {self.fps}")


class GPS:  # Класс для GPS
    def __init__(self, latitude, longitude, altitude):  # Инициализация GPS
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def update_location(self, new_latitude, new_longitude, new_altitude):
        self.latitude = new_latitude
        self.longitude = new_longitude
        self.altitude = new_altitude

    def get_current_location(self):  # Получение текущего местоположения
        print(f"Текущее положение: Широта: {self.latitude}, Долгота: {self.longitude}, Высота: {self.altitude}")
        return self.latitude, self.longitude, self.altitude


class FlightController:  # Класс контроллера полета
    def __init__(self, max_altitude):  # Инициализация контроллера
        self.max_altitude = max_altitude  # Максимальная высота полета
        self.is_flying = False  # Находится ли дрон в воздухе
        self.current_altitude = 0  # Текущая высота

    def take_off(self):  # Взлет
        if not self.is_flying:
            self.is_flying = True
            print("Готовность на взлет!")
        else:
            print("Дрон летит")

    def land(self):  # Посадка
        if self.is_flying:
            print("Приземляюсь!")
            self.is_flying = False
        else:
            print("Дрон уже приземлился.")

    def ascend(self, altitude_change):  # Подъем
        if self.is_flying:
            if self.current_altitude + altitude_change <= self.max_altitude:
                new_altitude = self.current_altitude + altitude_change
                print(f"Меняю высоту с {self.current_altitude} до {new_altitude} метров")
                self.current_altitude = new_altitude  # Обновление текущей высоты
            else:
                print(f"Не могу подняться выше максимальной высоты {self.max_altitude} метров")
        else:
            print("Дрон должен быть в воздухе")

    def descend(self, altitude_change):  # Спуск
        if self.is_flying:
            if self.current_altitude - altitude_change >= 0:
                self.current_altitude -= altitude_change
                print(f"Спускаюсь на {altitude_change} метров до высоты {self.current_altitude} метров")
            else:
                print(f"Не могу опуститься ниже уровня земли")
        else:
            print("Дрон должен быть в воздухе для снижения")

    def move_to_coordinates(self, latitude, longitude):  # Перемещение к координатам
        if self.is_flying:
            print(f"Перемещаюсь в точку Широта: {latitude}, Долгота: {longitude}")
        else:
            print("Дрон должен быть в воздухе для перемещения")


class FlightPlan:  # Класс для хранения и управления планом полета
    def __init__(self):
        self.waypoints = {  # Словарь точек маршрута
            "Эйфелева башня": (48.8584, 2.2945),
            "Афинский Акрополь": (37.9747, 23.7275),
            "Мэрия Геленджика": (44.5691, 38.1044)
        }

    def add_waypoints(self, name, waypoint):
        self.waypoints[name] = waypoint
        print(f"Новая точка на маршруте добавлена: {name} - {waypoint}")

    def get_next_waypoint(self):  # Получение следующей точки маршрута
        if self.waypoints:
            name, waypoint = self.waypoints.popitem()
            print(f"следующая точка маршрута: {name} - {waypoint}")
            return waypoint
        else:
            return None


class Drone:  # Класс для управления дроном
    def __init__(self, drone_id, camera, gps, flight_controller, flight_plan):  # Инициализация дрона
        self.drone_id = drone_id  # Идентификатор дрона
        self.camera = camera  # Объект камеры
        self.gps = gps  # Объект GPS
        self.flight_controller = flight_controller  # Объект контроллера полета
        self.flight_plan = flight_plan  # Объект плана полета

    def take_picture(self):  # Сделать фото
        self.camera.capture_image()

    def get_current_location(self):  # Получить текущее местоположение
        self.gps.get_current_location()

    def take_off(self):  # Взлет
        self.flight_controller.take_off()

    def land(self):  # Посадка
        self.flight_controller.land()

    def ascend(self, altitude_change):  # Подъем
        self.flight_controller.ascend(altitude_change)

    def descend(self, altitude_change):  # Спуск
        self.flight_controller.descend(altitude_change)

    def move_to_coordinates(self, latitude, longitude):  # Перемещение к координатам
        self.flight_controller.move_to_coordinates(latitude, longitude)

    def follow_flight_path(self):  # Следование маршруту
        if not self.flight_plan.waypoints:
            print("Маршрут не задан")
            return
        print(f"{self.drone_id} выдвинулся по маршруту")
        while self.flight_plan.waypoints:
            waypoint = self.flight_plan.get_next_waypoint()
            if waypoint:
                self.move_to_coordinates(*waypoint)  # Распаковка координат


drone_flight_plan = FlightPlan()
drone = Drone("Вуглускр", Camera(1920, 30), GPS(50.1121, 8.6741, 0), FlightController(500), FlightPlan())

drone.take_off()  # Взлет
drone.ascend(200)  # Подъем на 200 метров
drone.follow_flight_path()  # Следование маршруту
drone.descend(20)  # Спуск на 20 метров
drone.land()  # Посадка
