# 函数基础（Function Basics）

# 1. 定义简单函数
print("===== 定义简单函数 =====")

def greet():
    """打印问候语"""
    print("Hello, World!")

greet()

# 2. 带参数的函数
print("\n===== 带参数的函数 =====")

def greet_person(name):
    """向指定的人问好"""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# 3. 带返回值的函数
print("\n===== 带返回值的函数 =====")

def add(a, b):
    """返回两个数的和"""
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

def get_formatted_name(first_name, last_name):
    """返回格式化的全名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

name = get_formatted_name("john", "doe")
print(f"格式化的姓名: {name}")

# 4. 默认参数值
print("\n===== 默认参数值 =====")

def greet_with_title(name, title="Mr."):
    """使用称谓问候，默认为 Mr."""
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")           # 使用默认值
greet_with_title("Johnson", "Ms.")  # 提供自定义值

# 5. 关键字参数
print("\n===== 关键字参数 =====")

def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print(f"我有一只{animal_type}，名字叫{pet_name}")

describe_pet(animal_type="dog", pet_name="旺财")
describe_pet(pet_name="咪咪", animal_type="cat")  # 顺序可以不同

# 6. 任意数量的参数 (*args)
print("\n===== 任意数量的参数 =====")

def make_pizza(*toppings):
    """制作披萨，可以添加任意数量的配料"""
    print("\n制作披萨，配料有:")
    for topping in toppings:
        print(f"  - {topping}")

make_pizza("mushrooms")
make_pizza("pepperoni", "cheese", "olives")

# 7. 任意数量的关键字参数 (**kwargs)
print("\n===== 任意数量的关键字参数 =====")

def build_profile(first, last, **user_info):
    """创建用户档案"""
    profile = {
        'first_name': first,
        'last_name': last
    }
    profile.update(user_info)
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics',
                             age=76)
print("用户档案:", user_profile)

# 8. 返回多个值
print("\n===== 返回多个值 =====")

def get_dimensions():
    """返回长、宽、高"""
    return 10, 20, 30

length, width, height = get_dimensions()
print(f"尺寸: 长={length}, 宽={width}, 高={height}")

# 9. 函数作为参数
print("\n===== 函数作为参数 =====")

def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply_operation(func, value):
    """应用给定的函数到值上"""
    return func(value)

print(f"5的平方: {apply_operation(square, 5)}")
print(f"5的立方: {apply_operation(cube, 5)}")

# 10. 文档字符串（Docstring）
print("\n===== 文档字符串 =====")

def calculate_area(radius):
    """
    计算圆的面积
    
    参数:
        radius: 圆的半径
    
    返回:
        圆的面积
    """
    import math
    return math.pi * radius ** 2

area = calculate_area(5)
print(f"半径为5的圆的面积: {area:.2f}")
print(f"函数文档: {calculate_area.__doc__}")
