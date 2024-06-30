import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ID БПЛА | Время полета (минуты) | Расстояние (километры) | Средняя скорость (км/ч) | Высота полета (метры)
drones_data = np.array([[1, 30, 10, 20, 500],
                        [2, 45, 15, 20, 600],
                        [3, 25, 8, 19.2, 550],
                        [4, 60, 25, 25, 700],
                        [5, 35, 12, 20.6, 580]])
print("Drone flight data")
print(drones_data)

flight_time = drones_data[:, 1]  # :, указывает, что рассм. все строки, в т.ч. нулевую)
average_flight_time = np.mean(flight_time)
print(f"Average flight time {average_flight_time} minutes")

print("\n----------------------------------------------------------------\n")

altitudes = drones_data[:, 4]  # запрос ко всему массиву, выбор последнего столбца. 4, т.к. нумерация с нуля
max_altitude = np.max(altitudes)  # получение макс. скорости
print(f"Max altitude: {max_altitude} m")

total_dist = np.sum(drones_data[:, 2])
print(f"Total distance: {total_dist} km")
print()
longest_flight = drones_data[drones_data[:, 1] > 30]
print(f"Drones flying longer 30 min:")
print(longest_flight)

# Задаем параметры для вывода графика в NumPy
drone_ids = drones_data[:, 0]
flight_times = drones_data[:, 1]
altitudes = drones_data[:, 4]
plt.figure(figsize=(10, 5))  # задаем размер графика


# Каждый отдельный график внутри общего вывода задается отдельным блоком
plt.subplot(1, 2, 1)  # 1 строка, 2 столбца, 1й график)
plt.bar(drone_ids, flight_times, color="red")
plt.xlabel('ID БПЛА')
plt.ylabel('Время полета (минуты)')
plt.title('Время полета БПЛА')

plt.subplot(1, 2, 2)  # 1 строка, 2 столбца, 2й график)
plt.bar(drone_ids, altitudes, color="blue")
plt.xlabel('ID БПЛА')
plt.ylabel('Высота полета (метры)')
plt.title('Высота полета БПЛА')
plt.show()

conversion_matrix = np.array([
    [1, 0],
    [0, 0.277778]
    ])

speed_kmh = drones_data[:, 3]
speed_ms = speed_kmh * conversion_matrix[1, 1]

print(f"Speed km/h: {speed_kmh}, \n speed m/s {speed_ms}")

# Теперь пробуем обработать массив с помощью библиотеки Pandas
drones_data2 = {
    "ID drone": [1, 2, 3, 4, 5],
    "Flight time": [30, 45, 25, 60, 35],
    "Distance": [10, 15, 8, 25, 12],
    "Average speed": [20, 20, 19.2, 25, 20.6],
    "Flight height": [500, 600, 550, 700, 580]
}

drones_df = pd.DataFrame(drones_data2)
print("\n----------------------------------------------------------------\n")
print("Drone flight data")
print(drones_df)

average_flight_time = drones_df["Flight time"].mean()
print(f"Average flight time {average_flight_time} minutes")

# drones_df.plot(x='ID drone', y='Flight time', kind='bar')
# plt.xlabel('ID БПЛА')
# plt.ylabel('Время полета (минуты)')
# plt.title('Время полета БПЛА')
# plt.show()
