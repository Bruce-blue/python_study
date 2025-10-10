# 从 car 模块导入 Car 类
from car import Car

my_car = Car('audi', 'a4', 2020)
print(my_car.get_descriptive_name())

my_car.read_odometer()
my_car.odometer_reading = 23
my_car.read_odometer()

