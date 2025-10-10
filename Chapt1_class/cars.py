# 从一个模块同时导入多个类
from car import Car, ElectricCar    
from car import Battery

# 创建一辆奥迪汽车实例：品牌 audi，型号 a4，年份 2020
my_car = Car('audi', 'a4', 2020)
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.odometer_reading = 23
my_car.read_odometer()
my_car.update_odometer(50)
my_car.read_odometer()

# 创建一辆特斯拉电动车实例：品牌 tesla，型号 model s，年份 2020
my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.battery_size = 100 
my_tesla.battery.get_range()

# 直接创建一个 Battery 实例
my_battery = Battery(85)
my_battery.describe_battery()
my_battery.get_range()

