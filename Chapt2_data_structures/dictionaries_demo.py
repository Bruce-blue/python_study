# 字典（Dictionary）- Python 中的键值对数据结构
# 字典是可变的、无序的（Python 3.7+ 保持插入顺序）

# 1. 创建字典
print("--- 创建字典 ---")
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'Beijing',
    'occupation': 'Engineer'
}
print("个人信息:", person)

# 空字典
empty_dict = {}
another_dict = dict()

# 2. 访问字典元素
print("\n--- 访问元素 ---")
print("姓名:", person['name'])
print("年龄:", person.get('age'))
print("性别:", person.get('gender', '未指定'))  # 使用默认值

# 3. 修改和添加元素
print("\n--- 修改和添加 ---")
person['age'] = 26  # 修改
person['email'] = 'alice@example.com'  # 添加
print("更新后:", person)

# 4. 删除元素
print("\n--- 删除元素 ---")
del person['email']  # 删除指定键
print("删除 email 后:", person)

occupation = person.pop('occupation')  # 删除并返回值
print("删除 occupation 后:", person)
print("删除的职业:", occupation)

# 5. 字典方法
print("\n--- 字典方法 ---")
student = {'name': 'Bob', 'age': 20, 'grade': 'A'}
print("所有键:", student.keys())
print("所有值:", student.values())
print("所有键值对:", student.items())

# 检查键是否存在
print("'name' 在字典中:", 'name' in student)
print("'score' 在字典中:", 'score' in student)

# 6. 遍历字典
print("\n--- 遍历字典 ---")
scores = {'math': 95, 'english': 88, 'physics': 92}

print("遍历键:")
for subject in scores.keys():
    print(f"  {subject}")

print("遍历值:")
for score in scores.values():
    print(f"  {score}")

print("遍历键值对:")
for subject, score in scores.items():
    print(f"  {subject}: {score}")

# 7. 字典推导式
print("\n--- 字典推导式 ---")
squares_dict = {x: x**2 for x in range(1, 6)}
print("数字的平方:", squares_dict)

# 过滤字典
high_scores = {k: v for k, v in scores.items() if v >= 90}
print("高分科目:", high_scores)

# 8. 嵌套字典
print("\n--- 嵌套字典 ---")
students = {
    'student1': {'name': 'Alice', 'age': 20, 'grade': 'A'},
    'student2': {'name': 'Bob', 'age': 21, 'grade': 'B'},
    'student3': {'name': 'Charlie', 'age': 19, 'grade': 'A'}
}

for student_id, info in students.items():
    print(f"{student_id}: {info['name']}, 年龄 {info['age']}, 成绩 {info['grade']}")

# 9. update() 方法
print("\n--- 合并字典 ---")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print("合并后:", dict1)

# 10. setdefault() 方法
print("\n--- setdefault() ---")
word_count = {}
text = "hello world hello python"
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print("单词计数:", word_count)
