# Python 学习教程

这是一个系统的 Python 学习教程仓库，包含了从基础到进阶的各种 Python 编程概念和示例。

## 📚 目录结构

### Chapt1_class - 类与面向对象编程
学习 Python 的面向对象编程（OOP）概念。

**文件说明:**
- `car.py` - 定义了汽车类、电池类和电动汽车类，展示类的定义、继承和组合
- `my_car.py` - 创建汽车实例并使用类的方法
- `my_electric_car.py` - 创建电动汽车实例，展示继承的使用
- `cars.py` - 综合示例，演示如何导入和使用多个类

**主要概念:**
- 类的定义和实例化
- `__init__()` 方法
- 类的属性和方法
- 继承（Inheritance）
- 组合（Composition）
- 模块导入

### Chapt2_data_structures - 数据结构
学习 Python 的核心数据结构。

**文件说明:**
- `lists_demo.py` - 列表的创建、操作、切片、推导式等
- `dictionaries_demo.py` - 字典的使用、遍历、推导式、嵌套等
- `tuples_and_sets_demo.py` - 元组和集合的特性与应用

**主要概念:**
- **列表（List）**: 可变、有序的序列
- **字典（Dictionary）**: 键值对映射
- **元组（Tuple）**: 不可变、有序的序列
- **集合（Set）**: 无序、不重复的元素集
- 数据结构的选择和应用场景

### Chapt3_functions - 函数
学习 Python 函数的各种特性。

**文件说明:**
- `function_basics.py` - 函数定义、参数传递、返回值等基础知识
- `lambda_and_decorators.py` - Lambda 函数、装饰器等高级特性

**主要概念:**
- 函数定义和调用
- 参数类型：位置参数、默认参数、关键字参数
- `*args` 和 `**kwargs`
- Lambda 表达式
- 装饰器（Decorators）
- 高阶函数（map, filter, reduce）
- 函数文档字符串

### Chapt4_file_io - 文件输入输出
学习文件操作和数据持久化。

**文件说明:**
- `file_basics.py` - 文本文件的读写、文件指针操作、二进制文件等
- `json_and_csv.py` - JSON 和 CSV 格式的读写与转换

**主要概念:**
- 文件的打开、读取、写入和关闭
- `with` 语句（上下文管理器）
- 文件模式：`r`, `w`, `a`, `rb`, `wb`
- JSON 数据序列化与反序列化
- CSV 文件处理
- 文件编码处理

### Chapt5_error_handling - 异常处理
学习如何优雅地处理程序错误。

**文件说明:**
- `exception_basics.py` - 异常处理基础：try-except-else-finally
- `custom_exceptions.py` - 自定义异常、异常链、高级异常处理

**主要概念:**
- try-except 语句
- 多个 except 块
- else 和 finally 子句
- 常见的内置异常类型
- 自定义异常类
- 异常链（raise from）
- 断言（assert）
- 最佳实践

## 🚀 快速开始

### 环境要求
- Python 3.7 或更高版本

### 运行示例

每个章节的文件都可以独立运行。例如：

```bash
# 运行类的示例
python Chapt1_class/my_car.py

# 运行列表示例
python Chapt2_data_structures/lists_demo.py

# 运行函数示例
python Chapt3_functions/function_basics.py

# 运行文件操作示例
python Chapt4_file_io/file_basics.py

# 运行异常处理示例
python Chapt5_error_handling/exception_basics.py
```

## 📖 学习路径建议

1. **初学者路径**
   - Chapt2_data_structures（数据结构）→ 
   - Chapt3_functions（函数）→ 
   - Chapt1_class（类）→ 
   - Chapt4_file_io（文件操作）→ 
   - Chapt5_error_handling（异常处理）

2. **进阶学习**
   - 在掌握基础后，深入学习每个章节的高级特性
   - lambda_and_decorators.py（Lambda 和装饰器）
   - custom_exceptions.py（自定义异常）

## 💡 学习建议

1. **动手实践**: 不要只是阅读代码，要自己运行并修改示例
2. **理解概念**: 关注每个示例背后的编程概念和设计思想
3. **循序渐进**: 按照章节顺序学习，打好基础
4. **实际应用**: 尝试用学到的知识解决实际问题
5. **查阅文档**: 善用 Python 官方文档进行深入学习

## 📝 代码风格

本教程遵循以下编码规范：
- 使用 UTF-8 编码
- 中文注释帮助理解
- 清晰的代码结构
- 丰富的示例和输出

## 🤝 贡献

欢迎提出问题、建议或贡献新的学习内容！

## 📄 许可

本教程仅供学习使用。

---

**Happy Coding! 祝学习愉快！** 🎉
