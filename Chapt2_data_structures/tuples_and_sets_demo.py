# 元组（Tuple）和集合（Set）

# ===== 元组（Tuple）=====
# 元组是不可变的有序序列，一旦创建就不能修改

print("===== 元组（Tuple）=====")

# 1. 创建元组
print("\n--- 创建元组 ---")
coordinates = (10, 20)
print("坐标:", coordinates)

# 单元素元组需要加逗号
single = (42,)
print("单元素元组:", single, type(single))

# 元组拆包
x, y = coordinates
print(f"x = {x}, y = {y}")

# 2. 访问元组元素
print("\n--- 访问元组 ---")
colors = ('red', 'green', 'blue', 'yellow')
print("第一个颜色:", colors[0])
print("最后一个颜色:", colors[-1])
print("前两个颜色:", colors[:2])

# 3. 元组的不可变性
print("\n--- 元组不可变 ---")
try:
    colors[0] = 'purple'  # 这会引发错误
except TypeError as e:
    print(f"错误: {e}")

# 4. 元组方法
print("\n--- 元组方法 ---")
numbers = (1, 2, 3, 2, 4, 2, 5)
print("元组:", numbers)
print("元素2出现次数:", numbers.count(2))
print("元素3的索引:", numbers.index(3))
print("元组长度:", len(numbers))

# 5. 元组作为字典的键
print("\n--- 元组作为字典键 ---")
locations = {
    (40.7128, -74.0060): 'New York',
    (34.0522, -118.2437): 'Los Angeles',
    (51.5074, -0.1278): 'London'
}
print("位置信息:", locations)
print("纽约的坐标对应:", locations[(40.7128, -74.0060)])


# ===== 集合（Set）=====
# 集合是无序的、不重复的元素集

print("\n\n===== 集合（Set）=====")

# 1. 创建集合
print("\n--- 创建集合 ---")
fruits = {'apple', 'banana', 'cherry'}
print("水果集合:", fruits)

# 从列表创建集合（自动去重）
numbers_list = [1, 2, 2, 3, 3, 3, 4, 5]
numbers_set = set(numbers_list)
print("数字集合（已去重）:", numbers_set)

# 2. 添加和删除元素
print("\n--- 添加和删除 ---")
fruits.add('date')
print("添加后:", fruits)

fruits.remove('banana')  # 如果元素不存在会报错
print("删除后:", fruits)

fruits.discard('grape')  # 如果元素不存在不会报错
print("discard 不存在的元素:", fruits)

# 3. 集合运算
print("\n--- 集合运算 ---")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("集合1:", set1)
print("集合2:", set2)
print("并集:", set1 | set2)
print("交集:", set1 & set2)
print("差集:", set1 - set2)
print("对称差集:", set1 ^ set2)

# 4. 集合方法
print("\n--- 集合方法 ---")
a = {1, 2, 3}
b = {2, 3, 4}

print("a 是否是 b 的子集:", a.issubset(b))
print("a 是否是 b 的超集:", a.issuperset(b))
print("a 和 b 是否有交集:", not a.isdisjoint(b))

# 5. 集合推导式
print("\n--- 集合推导式 ---")
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print("偶数的平方:", even_squares)

# 6. 冻结集合（Frozen Set）- 不可变集合
print("\n--- 冻结集合 ---")
frozen = frozenset([1, 2, 3, 4, 5])
print("冻结集合:", frozen)
print("可以作为字典的键:", {frozen: 'frozen set key'})

# 7. 集合的实用应用 - 去重
print("\n--- 实用应用：去重 ---")
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'date']
unique_words = list(set(words))
print("原始列表:", words)
print("去重后:", unique_words)
