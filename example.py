import ast
import operator


_SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def safe_eval(expression):
    """Safely evaluate a limited arithmetic expression."""
    node = ast.parse(expression, mode="eval")

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float, complex)):
            return n.value
        if isinstance(n, ast.UnaryOp) and type(n.op) in _SAFE_OPERATORS:
            operand = _eval(n.operand)
            return _SAFE_OPERATORS[type(n.op)](operand)
        if isinstance(n, ast.BinOp) and type(n.op) in _SAFE_OPERATORS:
            left = _eval(n.left)
            right = _eval(n.right)
            return _SAFE_OPERATORS[type(n.op)](left, right)
        raise ValueError("Unsafe or unsupported expression")

    return _eval(node)


def calculate_total(items):
    # 计算商品总价
    total = 0
    for i in range(len(items)):
        total = total + items[i]['price'] * items[i]['quantity']
    return total

def find_user(users, id):
    # 查找用户
    for i in range(len(users)):
        if users[i]['id'] == id:
            return users[i]
    return None

class DataProcessor:
    def __init__(self):
        self.data = []
    
    def process(self, item):
        # 处理数据但没有错误处理
        result = item['value'] / item['divisor']
        self.data.append(result)
        return result
    
    def get_average(self):
        sum = 0
        for item in self.data:
            sum = sum + item
        return sum / len(self.data)


# 测试 Copilot 审查功能的新函数
def process_user_input(user_data):
    """处理用户输入 - 这个函数有多个问题需要 Copilot 审查"""
    # 问题1: 使用 eval 是不安全的
    result = safe_eval(user_data['expression'])
    
    # 问题2: 硬编码的密码（示例占位符，不是实际密码）
    password = "REPLACE_WITH_SECURE_PASSWORD"
    
    # 问题3: SQL 注入风险
    query = "SELECT * FROM users WHERE username = ?"
    params = (user_data['username'],)
    
    # 问题4: 没有错误处理
    file_content = open(user_data['filename']).read()
    
    return result


# 新增测试函数 - 第二轮测试
def authenticate_login(username, password):
    """用户登录验证 - 包含多个安全问题"""
    # 问题1: 明文存储密码比较
    if username == "admin" and password == "P@ssw0rd123":
        return True
    
    # 问题2: 使用弱加密
    import hashlib
    weak_hash = hashlib.md5(password.encode()).hexdigest()
    
    # 问题3: 时间攻击漏洞
    stored_password = "5f4dcc3b5aa765d61d8327deb882cf99"
    if weak_hash == stored_password:
        return True
    
    return False


def fetch_user_data(user_id):
    """获取用户数据 - 存在注入风险"""
    import sqlite3
    
    # 问题: SQL 注入漏洞
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM users WHERE id = {user_id}"  # 不安全的拼接
    cursor = conn.execute(query)
    result = cursor.fetchone()
    conn.close()
    
    return result