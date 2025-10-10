# 从 car 模块导入 ElectricCar 类
from car import ElectricCar

# 创建一辆特斯拉电动车实例：品牌 tesla，型号 model s，年份 2020
my_tesla = ElectricCar('tesla', 'model s', 2020)

# 打印车辆的完整描述信息（例如：2020 Tesla Model S）
print(my_tesla.get_descriptive_name())

# 打印电池的规格信息（如电池容量）
my_tesla.battery.describe_battery()

# 根据电池容量估算并打印续航里程
my_tesla.battery.get_range()
