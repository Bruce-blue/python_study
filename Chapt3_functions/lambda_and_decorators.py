# Lambda 函数和装饰器

# ===== Lambda 函数 =====
print("===== Lambda 函数 =====")

# 1. Lambda 函数基础
# lambda 参数: 表达式
add = lambda x, y: x + y
print(f"3 + 5 = {add(3, 5)}")

square = lambda x: x ** 2
print(f"5的平方 = {square(5)}")

# 2. Lambda 与内置函数配合使用
print("\n--- Lambda 与 map() ---")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"原始列表: {numbers}")
print(f"平方后: {squared}")

print("\n--- Lambda 与 filter() ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"原始列表: {numbers}")
print(f"偶数: {evens}")

print("\n--- Lambda 与 sorted() ---")
students = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 23}
]
sorted_students = sorted(students, key=lambda s: s['age'])
print("按年龄排序:")
for student in sorted_students:
    print(f"  {student['name']}: {student['age']}")

# 3. Lambda 与 reduce()
print("\n--- Lambda 与 reduce() ---")
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
product = reduce(lambda x, y: x * y, numbers)
print(f"列表: {numbers}")
print(f"求和: {sum_result}")
print(f"求积: {product}")


# ===== 装饰器（Decorators）=====
print("\n\n===== 装饰器 =====")

# 1. 简单装饰器
print("\n--- 简单装饰器 ---")

def my_decorator(func):
    """装饰器：在函数执行前后打印消息"""
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# 2. 带参数的装饰器
print("\n--- 带参数的装饰器 ---")

def my_decorator_with_args(func):
    """装饰器：处理带参数的函数"""
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}，参数: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值: {result}")
        return result
    return wrapper

@my_decorator_with_args
def add(a, b):
    return a + b

result = add(3, 5)

# 3. 计时装饰器
print("\n--- 计时装饰器 ---")

import time

def timer(func):
    """装饰器：测量函数执行时间"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.4f} 秒")
        return result
    return wrapper

@timer
def slow_function():
    """模拟耗时操作"""
    time.sleep(0.1)
    return "完成"

result = slow_function()

# 4. 缓存装饰器
print("\n--- 缓存装饰器 ---")

def memoize(func):
    """装饰器：缓存函数结果"""
    cache = {}
    def wrapper(*args):
        if args not in cache:
            print(f"计算 {args}")
            cache[args] = func(*args)
        else:
            print(f"从缓存获取 {args}")
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    """计算斐波那契数列"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("fibonacci(5):", fibonacci(5))
print("fibonacci(5) 再次调用:", fibonacci(5))

# 5. 带参数的装饰器
print("\n--- 带参数的装饰器 ---")

def repeat(times):
    """装饰器工厂：重复执行函数指定次数"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"第 {i+1} 次执行:")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"  Hello, {name}!")

greet("Alice")

# 6. 类装饰器
print("\n--- 类装饰器 ---")

class CountCalls:
    """装饰器类：统计函数调用次数"""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} 已被调用 {self.count} 次")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("  Hi!")

say_hi()
say_hi()
say_hi()

# 7. functools.wraps - 保留原函数信息
print("\n--- 使用 functools.wraps ---")

from functools import wraps

def my_decorator_proper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """包装器函数"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator_proper
def example_function():
    """这是一个示例函数"""
    pass

print(f"函数名: {example_function.__name__}")
print(f"函数文档: {example_function.__doc__}")
