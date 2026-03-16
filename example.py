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
