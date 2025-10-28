# 列表（List）- Python 中最常用的数据结构之一
# 列表是可变的、有序的序列，可以包含不同类型的元素

# 1. 创建列表
fruits = ['apple', 'banana', 'cherry', 'date']
print("水果列表:", fruits)

# 2. 访问列表元素
print("\n--- 访问元素 ---")
print("第一个水果:", fruits[0])
print("最后一个水果:", fruits[-1])
print("前两个水果:", fruits[:2])

# 3. 修改列表元素
print("\n--- 修改元素 ---")
fruits[1] = 'blueberry'
print("修改后的列表:", fruits)

# 4. 添加元素
print("\n--- 添加元素 ---")
fruits.append('elderberry')  # 在末尾添加
print("append 后:", fruits)

fruits.insert(1, 'avocado')  # 在指定位置插入
print("insert 后:", fruits)

# 5. 删除元素
print("\n--- 删除元素 ---")
fruits.remove('cherry')  # 删除指定值
print("remove 后:", fruits)

popped_fruit = fruits.pop()  # 删除并返回最后一个元素
print("pop 后:", fruits)
print("弹出的元素:", popped_fruit)

# 6. 列表切片
print("\n--- 列表切片 ---")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("原始列表:", numbers)
print("前5个元素:", numbers[:5])
print("后5个元素:", numbers[5:])
print("从索引2到7:", numbers[2:8])
print("步长为2:", numbers[::2])
print("反转列表:", numbers[::-1])

# 7. 列表推导式（List Comprehension）
print("\n--- 列表推导式 ---")
squares = [x**2 for x in range(10)]
print("0-9的平方:", squares)

even_numbers = [x for x in range(20) if x % 2 == 0]
print("0-19的偶数:", even_numbers)

# 8. 常用列表方法
print("\n--- 常用方法 ---")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("原始列表:", numbers)
print("列表长度:", len(numbers))
print("最大值:", max(numbers))
print("最小值:", min(numbers))
print("求和:", sum(numbers))

numbers.sort()  # 排序（就地修改）
print("排序后:", numbers)

numbers.reverse()  # 反转（就地修改）
print("反转后:", numbers)

print("元素1出现次数:", numbers.count(1))
print("元素5的索引:", numbers.index(5))

# 9. 复制列表
print("\n--- 复制列表 ---")
original = [1, 2, 3]
shallow_copy = original.copy()  # 浅拷贝
another_copy = original[:]       # 切片也可以复制

shallow_copy.append(4)
print("原始列表:", original)
print("拷贝列表:", shallow_copy)
