# 异常处理基础

# 1. 基本的 try-except
print("===== 基本的 try-except =====")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("错误: 不能除以零！")

print("程序继续执行...\n")

# 2. 捕获多种异常
print("===== 捕获多种异常 =====")

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误: 除数不能为零")
    except TypeError:
        print("错误: 参数类型不正确")
    return None

print(f"10 / 2 = {divide_numbers(10, 2)}")
print(f"10 / 0 = {divide_numbers(10, 0)}")
print(f"10 / '2' = {divide_numbers(10, '2')}")

# 3. 使用 else 子句
print("\n===== try-except-else =====")

def read_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"错误: 文件 {filename} 不存在")
    else:
        # 只有在没有异常时才执行
        print(f"成功读取文件，内容长度: {len(content)} 字符")
        return content

# 创建测试文件
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("这是测试内容")

read_file_content('test.txt')
read_file_content('nonexistent.txt')

# 4. 使用 finally 子句
print("\n===== try-except-finally =====")

def process_file(filename):
    file = None
    try:
        file = open(filename, 'r', encoding='utf-8')
        content = file.read()
        print(f"文件内容: {content}")
    except FileNotFoundError:
        print(f"错误: 文件 {filename} 不存在")
    finally:
        # 无论是否发生异常都会执行
        if file:
            file.close()
            print("文件已关闭")
        print("清理完成\n")

process_file('test.txt')
process_file('missing.txt')

# 5. 捕获异常对象
print("===== 捕获异常对象 =====")

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as e:
    print(f"捕获到异常: {type(e).__name__}")
    print(f"异常信息: {e}")

# 6. 捕获所有异常
print("\n===== 捕获所有异常 =====")

def safe_operation(a, b, operation):
    try:
        if operation == 'add':
            return a + b
        elif operation == 'divide':
            return a / b
        elif operation == 'access':
            return a[b]
    except Exception as e:
        print(f"发生错误: {type(e).__name__} - {e}")
        return None

print(safe_operation(10, 5, 'add'))
print(safe_operation(10, 0, 'divide'))
print(safe_operation([1, 2], 10, 'access'))

# 7. 多个 except 块
print("\n===== 多个 except 块 =====")

def convert_to_int(value):
    try:
        # 尝试将值转换为整数并计算
        num = int(value)
        result = 100 / num
        return result
    except ValueError:
        print(f"错误: '{value}' 不是有效的数字")
    except ZeroDivisionError:
        print(f"错误: 不能除以零")
    except Exception as e:
        print(f"未知错误: {e}")
    return None

convert_to_int("50")
convert_to_int("abc")
convert_to_int("0")

# 8. 异常链
print("\n===== 异常链 =====")

try:
    try:
        result = 1 / 0
    except ZeroDivisionError:
        print("捕获到内部异常")
        raise ValueError("由 ZeroDivisionError 引起的错误")
except ValueError as e:
    print(f"捕获到外部异常: {e}")

# 9. 常见的内置异常
print("\n===== 常见的内置异常 =====")

exceptions_demo = {
    'IndexError': lambda: [1, 2, 3][10],
    'KeyError': lambda: {'a': 1}['b'],
    'ValueError': lambda: int('abc'),
    'TypeError': lambda: 1 + '2',
    'AttributeError': lambda: 'string'.nonexistent_method(),
    'ZeroDivisionError': lambda: 10 / 0,
}

for exc_name, func in exceptions_demo.items():
    try:
        func()
    except Exception as e:
        print(f"{exc_name}: {e}")

# 10. assert 语句
print("\n===== assert 语句 =====")

def calculate_average(numbers):
    assert len(numbers) > 0, "列表不能为空"
    return sum(numbers) / len(numbers)

try:
    avg = calculate_average([1, 2, 3, 4, 5])
    print(f"平均值: {avg}")
    
    avg = calculate_average([])
except AssertionError as e:
    print(f"断言失败: {e}")

# 清理测试文件
import os
if os.path.exists('test.txt'):
    os.remove('test.txt')

print("\n异常处理演示完成！")
