# 文件读写基础

import os

# 确保示例文件存在的目录
data_dir = os.path.dirname(__file__)

# 1. 写入文本文件
print("===== 写入文本文件 =====")

filename = os.path.join(data_dir, 'sample.txt')

# 写入模式 'w' - 覆盖原有内容
with open(filename, 'w', encoding='utf-8') as file:
    file.write("第一行文本\n")
    file.write("第二行文本\n")
    file.write("第三行文本\n")

print(f"已写入文件: {filename}")

# 2. 读取文本文件
print("\n===== 读取文本文件 =====")

# 读取整个文件
with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()
    print("文件内容:")
    print(content)

# 逐行读取
print("\n逐行读取:")
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())  # strip() 去除换行符

# 读取所有行到列表
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f"\n总共 {len(lines)} 行")

# 3. 追加文本
print("\n===== 追加文本 =====")

# 追加模式 'a' - 在文件末尾添加
with open(filename, 'a', encoding='utf-8') as file:
    file.write("第四行文本（追加）\n")
    file.write("第五行文本（追加）\n")

with open(filename, 'r', encoding='utf-8') as file:
    print("追加后的文件内容:")
    print(file.read())

# 4. 使用 with 语句的优势
print("\n===== with 语句的优势 =====")

# 不使用 with（不推荐）
file = open(filename, 'r', encoding='utf-8')
content = file.read()
file.close()  # 必须手动关闭

# 使用 with（推荐）
with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()
    # 文件会自动关闭，即使发生异常

print("with 语句会自动关闭文件，更安全")

# 5. 读取文件的不同方法
print("\n===== 读取方法对比 =====")

# read() - 读取全部内容
with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()
    print(f"read() 返回类型: {type(content)}")

# readlines() - 读取所有行到列表
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f"readlines() 返回类型: {type(lines)}, 长度: {len(lines)}")

# readline() - 每次读取一行
with open(filename, 'r', encoding='utf-8') as file:
    first_line = file.readline()
    second_line = file.readline()
    print(f"第一行: {first_line.strip()}")
    print(f"第二行: {second_line.strip()}")

# 6. 文件指针操作
print("\n===== 文件指针操作 =====")

with open(filename, 'r', encoding='utf-8') as file:
    print(f"初始位置: {file.tell()}")
    file.read(10)  # 读取10个字符
    print(f"读取10个字符后位置: {file.tell()}")
    file.seek(0)  # 回到文件开头
    print(f"seek(0) 后位置: {file.tell()}")

# 7. 处理文件不存在的情况
print("\n===== 处理文件不存在 =====")

try:
    with open('nonexistent_file.txt', 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print("错误: 文件不存在")

# 8. 检查文件是否存在
print("\n===== 检查文件是否存在 =====")

if os.path.exists(filename):
    print(f"文件 {filename} 存在")
    print(f"文件大小: {os.path.getsize(filename)} 字节")
else:
    print(f"文件 {filename} 不存在")

# 9. 写入多行
print("\n===== 写入多行 =====")

lines_to_write = [
    "Python 是一门强大的编程语言\n",
    "它简洁、易学、功能丰富\n",
    "适合初学者和专业开发者\n"
]

multiline_file = os.path.join(data_dir, 'multiline.txt')
with open(multiline_file, 'w', encoding='utf-8') as file:
    file.writelines(lines_to_write)

print(f"已写入 {len(lines_to_write)} 行到 {multiline_file}")

# 读取并显示
with open(multiline_file, 'r', encoding='utf-8') as file:
    print("文件内容:")
    print(file.read())

# 10. 二进制文件操作
print("\n===== 二进制文件操作 =====")

binary_file = os.path.join(data_dir, 'binary_data.bin')

# 写入二进制数据
data = bytes([65, 66, 67, 68, 69])  # ASCII: ABCDE
with open(binary_file, 'wb') as file:
    file.write(data)

print(f"已写入二进制数据: {data}")

# 读取二进制数据
with open(binary_file, 'rb') as file:
    read_data = file.read()
    print(f"读取的二进制数据: {read_data}")
    print(f"转换为字符串: {read_data.decode('ascii')}")

print("\n文件操作完成！")
