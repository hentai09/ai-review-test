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
    result = eval(user_data['expression'])
    
    # 问题2: 硬编码的密码
    password = "admin123"
    
    # 问题3: SQL 注入风险
    query = "SELECT * FROM users WHERE username = '" + user_data['username'] + "'"
    
    # 问题4: 没有错误处理
    file_content = open(user_data['filename']).read()
    
    return result