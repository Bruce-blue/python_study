# 一个模块存储多个类
class Car:
    def __init__(self, make, model, year):
        # 初始化汽车的基本信息
        self.make = make   # 品牌
        self.model = model # 型号
        self.year = year   # 出厂年份
        self.odometer_reading = 0  # 里程表初始值为 0

    def get_descriptive_name(self):
        # 返回格式化后的车辆描述信息
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        # 打印当前里程表读数
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        # 更新里程表读数，禁止回退（只能增大或保持不变）
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        # 将里程表读数增加指定的英里数
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't increment the odometer with negative miles!")

class Battery:
    def __init__(self, battery_size=75):
        # 初始化电池容量，默认值为 75 kWh
        self.battery_size = battery_size

    def describe_battery(self):
        # 打印电池容量信息
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        # 根据电池容量计算并打印续航里程
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = 200  # 默认续航里程

        print(f"This car can go approximately {range} miles on a full charge.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        # 初始化父类属性
        super().__init__(make, model, year)
        # 初始化电动汽车特有的电池属性
        self.battery = Battery()  # 创建一个 Battery 实例作为属性