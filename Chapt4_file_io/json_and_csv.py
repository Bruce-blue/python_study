# JSON 和 CSV 文件操作

import json
import csv
import os

data_dir = os.path.dirname(__file__)

# ===== JSON 文件操作 =====
print("===== JSON 文件操作 =====")

# 1. 写入 JSON 文件
print("\n--- 写入 JSON ---")

user_data = {
    'name': 'Alice',
    'age': 25,
    'city': 'Beijing',
    'hobbies': ['reading', 'coding', 'music'],
    'is_student': False
}

json_file = os.path.join(data_dir, 'user_data.json')

with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(user_data, file, ensure_ascii=False, indent=2)

print(f"已写入 JSON 文件: {json_file}")

# 2. 读取 JSON 文件
print("\n--- 读取 JSON ---")

with open(json_file, 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)
    print("读取的数据:")
    print(f"  姓名: {loaded_data['name']}")
    print(f"  年龄: {loaded_data['age']}")
    print(f"  城市: {loaded_data['city']}")
    print(f"  爱好: {', '.join(loaded_data['hobbies'])}")

# 3. JSON 字符串转换
print("\n--- JSON 字符串转换 ---")

# Python 对象转 JSON 字符串
python_dict = {'x': 1, 'y': 2, 'z': 3}
json_string = json.dumps(python_dict, ensure_ascii=False)
print(f"JSON 字符串: {json_string}")

# JSON 字符串转 Python 对象
json_str = '{"name": "Bob", "age": 30}'
python_obj = json.loads(json_str)
print(f"Python 对象: {python_obj}")

# 4. JSON 处理复杂数据
print("\n--- 复杂 JSON 数据 ---")

students = [
    {'id': 1, 'name': 'Alice', 'scores': {'math': 95, 'english': 88}},
    {'id': 2, 'name': 'Bob', 'scores': {'math': 87, 'english': 92}},
    {'id': 3, 'name': 'Charlie', 'scores': {'math': 91, 'english': 85}}
]

students_file = os.path.join(data_dir, 'students.json')

with open(students_file, 'w', encoding='utf-8') as file:
    json.dump(students, file, ensure_ascii=False, indent=2)

print(f"已写入学生数据到 {students_file}")

# 读取并处理
with open(students_file, 'r', encoding='utf-8') as file:
    students_data = json.load(file)
    print("\n学生成绩:")
    for student in students_data:
        print(f"  {student['name']}: 数学={student['scores']['math']}, 英语={student['scores']['english']}")


# ===== CSV 文件操作 =====
print("\n\n===== CSV 文件操作 =====")

# 1. 写入 CSV 文件
print("\n--- 写入 CSV ---")

csv_file = os.path.join(data_dir, 'employees.csv')

# 使用列表写入
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # 写入表头
    writer.writerow(['姓名', '年龄', '部门', '工资'])
    
    # 写入数据
    writer.writerow(['Alice', 25, 'IT', 8000])
    writer.writerow(['Bob', 30, 'HR', 7000])
    writer.writerow(['Charlie', 28, 'Sales', 7500])

print(f"已写入 CSV 文件: {csv_file}")

# 2. 读取 CSV 文件
print("\n--- 读取 CSV ---")

with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # 读取表头
    headers = next(reader)
    print(f"表头: {headers}")
    
    # 读取数据
    print("员工信息:")
    for row in reader:
        print(f"  {row[0]}: 年龄{row[1]}, 部门{row[2]}, 工资{row[3]}")

# 3. 使用字典读写 CSV
print("\n--- 使用字典读写 CSV ---")

dict_csv_file = os.path.join(data_dir, 'products.csv')

# 写入
products = [
    {'name': 'Laptop', 'price': 5000, 'stock': 10},
    {'name': 'Mouse', 'price': 50, 'stock': 100},
    {'name': 'Keyboard', 'price': 200, 'stock': 50}
]

with open(dict_csv_file, 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['name', 'price', 'stock']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # 写入表头
    writer.writerows(products)  # 写入所有行

print(f"已写入产品数据到 {dict_csv_file}")

# 读取
with open(dict_csv_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    print("产品列表:")
    for row in reader:
        print(f"  {row['name']}: 价格¥{row['price']}, 库存{row['stock']}")

# 4. 处理带引号和特殊字符的 CSV
print("\n--- 处理特殊字符 ---")

special_csv = os.path.join(data_dir, 'special.csv')

with open(special_csv, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(['Name', 'Description'])
    writer.writerow(['Product 1', 'Contains "quotes" and, commas'])
    writer.writerow(['Product 2', 'Normal description'])

print(f"已写入包含特殊字符的 CSV: {special_csv}")

with open(special_csv, 'r', encoding='utf-8') as file:
    content = file.read()
    print("文件内容:")
    print(content)

# 5. CSV 转 JSON
print("\n--- CSV 转 JSON ---")

with open(csv_file, 'r', encoding='utf-8') as csvf:
    reader = csv.DictReader(csvf)
    rows = list(reader)

csv_to_json_file = os.path.join(data_dir, 'employees.json')
with open(csv_to_json_file, 'w', encoding='utf-8') as jsonf:
    json.dump(rows, jsonf, ensure_ascii=False, indent=2)

print(f"已将 CSV 转换为 JSON: {csv_to_json_file}")

with open(csv_to_json_file, 'r', encoding='utf-8') as file:
    print("转换后的 JSON:")
    print(file.read())

print("\nJSON 和 CSV 操作完成！")
