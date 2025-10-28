# 自定义异常和高级异常处理

# ===== 自定义异常 =====
print("===== 自定义异常 =====")

# 1. 简单的自定义异常
class InvalidAgeError(Exception):
    """年龄无效时抛出的异常"""
    pass

def set_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(f"年龄 {age} 无效，必须在 0-150 之间")
    return age

try:
    set_age(25)
    print("年龄 25 有效")
    set_age(200)
except InvalidAgeError as e:
    print(f"捕获到自定义异常: {e}")

# 2. 带属性的自定义异常
print("\n--- 带属性的自定义异常 ---")

class InsufficientFundsError(Exception):
    """余额不足时抛出的异常"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortage = amount - balance
        super().__init__(f"余额不足: 当前余额 {balance}, 需要 {amount}, 缺少 {self.shortage}")

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(1000)
try:
    account.withdraw(500)
    print(f"取款 500 成功，余额: {account.balance}")
    account.withdraw(800)
except InsufficientFundsError as e:
    print(f"取款失败: {e}")
    print(f"  当前余额: {e.balance}")
    print(f"  尝试取款: {e.amount}")
    print(f"  缺少金额: {e.shortage}")

# 3. 异常继承层次
print("\n--- 异常继承层次 ---")

class ValidationError(Exception):
    """验证错误基类"""
    pass

class EmailValidationError(ValidationError):
    """邮箱验证错误"""
    pass

class PasswordValidationError(ValidationError):
    """密码验证错误"""
    pass

def validate_email(email):
    if '@' not in email:
        raise EmailValidationError("邮箱格式无效，缺少 @ 符号")

def validate_password(password):
    if len(password) < 6:
        raise PasswordValidationError("密码长度必须至少为 6 位")

def register_user(email, password):
    try:
        validate_email(email)
        validate_password(password)
        print(f"用户注册成功: {email}")
    except EmailValidationError as e:
        print(f"邮箱验证失败: {e}")
    except PasswordValidationError as e:
        print(f"密码验证失败: {e}")
    except ValidationError as e:
        print(f"验证失败: {e}")

register_user("user@example.com", "password123")
register_user("invalid-email", "password123")
register_user("user@example.com", "12345")

# 4. 使用 raise from 进行异常链
print("\n--- 异常链 ---")

class DatabaseError(Exception):
    """数据库错误"""
    pass

def connect_to_database():
    # 模拟数据库连接失败
    raise ConnectionError("无法连接到数据库服务器")

def fetch_user_data(user_id):
    try:
        connect_to_database()
    except ConnectionError as e:
        raise DatabaseError(f"获取用户 {user_id} 数据失败") from e

try:
    fetch_user_data(123)
except DatabaseError as e:
    print(f"错误: {e}")
    print(f"原因: {e.__cause__}")

# 5. 重新抛出异常
print("\n--- 重新抛出异常 ---")

def process_data(data):
    try:
        # 尝试处理数据
        result = int(data)
        return result * 2
    except ValueError:
        print("数据处理失败，记录日志...")
        raise  # 重新抛出当前异常

try:
    process_data("invalid")
except ValueError as e:
    print(f"最终捕获: {e}")

# 6. 上下文管理器中的异常处理
print("\n--- 上下文管理器异常处理 ---")

class ManagedResource:
    """自定义资源管理器"""
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print(f"打开资源: {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"发生异常: {exc_type.__name__}: {exc_value}")
        print(f"关闭资源: {self.name}")
        # 返回 True 会抑制异常，False 会传播异常
        return False

try:
    with ManagedResource("数据库连接") as resource:
        print("使用资源...")
        raise ValueError("模拟错误")
except ValueError as e:
    print(f"外部捕获: {e}")

# 7. 异常组（Python 3.11+）
print("\n--- 自定义异常组处理 ---")

class MultipleValidationErrors(Exception):
    """包含多个验证错误的异常"""
    def __init__(self, errors):
        self.errors = errors
        messages = "; ".join(str(e) for e in errors)
        super().__init__(f"发现 {len(errors)} 个验证错误: {messages}")

def validate_user_input(data):
    errors = []
    
    if 'name' not in data or not data['name']:
        errors.append(ValueError("姓名不能为空"))
    
    if 'age' not in data or data['age'] < 0:
        errors.append(InvalidAgeError("年龄必须大于等于 0"))
    
    if 'email' not in data or '@' not in data['email']:
        errors.append(EmailValidationError("邮箱格式无效"))
    
    if errors:
        raise MultipleValidationErrors(errors)
    
    return True

try:
    validate_user_input({'name': '', 'age': -5, 'email': 'invalid'})
except MultipleValidationErrors as e:
    print(f"验证失败: {e}")
    print("详细错误:")
    for error in e.errors:
        print(f"  - {type(error).__name__}: {error}")

# 8. 最佳实践示例
print("\n--- 异常处理最佳实践 ---")

def read_config_file(filename):
    """
    读取配置文件的最佳实践示例
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            import json
            config = json.load(file)
            return config
    except FileNotFoundError:
        print(f"警告: 配置文件 {filename} 不存在，使用默认配置")
        return {'default': True}
    except json.JSONDecodeError as e:
        print(f"错误: 配置文件格式错误 - {e}")
        raise
    except Exception as e:
        print(f"未知错误: {e}")
        raise

# 测试
config = read_config_file('nonexistent_config.json')
print(f"配置: {config}")

print("\n自定义异常演示完成！")
