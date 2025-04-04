# 1. ความถูกต้องของฟังก์ชัน
def calculate_area(radius):
    # ลืมคูณด้วยค่าคงที่ pi
    return 2 * radius ** 2

# 2.ประสิทธิภาพ
def find_max(nums):
    max_value = nums[0]
    for i in nums:
        for j in nums:
            if i > max_value:
                max_value = i
    return max_value

# 3.ความง่ายในการอ่าน (Readability)
def do_something(a, b):
    return a + b

# 4.การจัดรูปแบบ (Formatting)
def do_math(x,y):
    return x+y

# 5.ความสามารถในการบำรุงรักษา (Maintainability)
def process_data(data):
    for i in range(len(data)):
        data[i] *= 2

    sum_data = 0
    for item in data:
        sum_data += item
    
    return sum_data / len(data)

# 6.การรักษาความปลอดภัย (Security)
def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    execute_database_query(query)


# 7.การจัดการข้อผิดพลาด (Error Handling)
def divide(a, b):
    return a / b

# 8.เอกสาร (Documentation)
def calculate_total(price, tax):
    return price + (price * tax)

# 9.การทดสอบ (Testing)
def add(a, b):
    return a + b

# 10.การพึ่งพา (Dependencies)
import numpy as np

def calculate_sum(a, b):
    return np.sum([a, b])

# 11.การใช้งานร่วมกับระบบอื่น (Interoperability)
def get_data():
    return {'key1': 'value1', 'key2': 'value2'}

def process_data(data):
    # คาดหวังเป็นลิสต์ ไม่ใช่ดิกชันนารี
    for item in data:
        print(item)

# 12.มาตรฐานและแนวทางปฏิบัติที่ดีที่สุด (Best Practices)
def calculate_circumference(radius):
    return 2 * 3.14159 * radius

# 13.กรณีการใช้งานที่หลากหลาย (Edge Cases)
def get_first_element(lst):
    return lst[0]
