import random
import string

def generate_random_profile():
    """生成隨機的使用者資料"""
    # 隨機名字列表
    first_names = ["Yi", "Wei", "Ming", "Jia", "Hui", "Chia", "PeiYu", "Han", "Feng", "Hao", "Jun", "Qian", "Xiang", "Tao"]
    
    # 隨機姓氏列表
    last_names = ["Lin", "Chen", "Wang", "Zhang", "Liu", "Yang", "Huang", "Wu", "Zhou", "Zhu", 
                "Sun", "Gao", "Zheng", "Liang", "Song", "Tang"]
    
    # 隨機選擇名字和姓氏
    firstname = random.choice(first_names)
    lastname = random.choice(last_names)
    
    # 隨機生成1970-2005年間的出生年份
    birth_year = random.randint(1970, 2005)
    
    # 隨機選擇性別
    gender = random.choice(["male", "female", "non-binary", "other"])
    
    # 隨機選擇國家
    countries = ["Taiwan", "Hong Kong", "Japan", "Taiwan", "Taiwan"]
    country = random.choice(countries)
    
    # 生成隨機電子郵件
    email_providers = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"]
    username = firstname.lower() + lastname.lower() + str(random.randint(1, 999))
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    email = f"{username}{random_chars}@{random.choice(email_providers)}"
    
    return {
        "firstname": firstname,
        "lastname": lastname,
        "birth_year": birth_year,
        "gender": gender,
        "country": country,
        "email": email
    }

def run_multiple_votes_data(count=10):
    """生成多筆隨機投票資料"""
    profiles = []
    for _ in range(count):
        profiles.append(generate_random_profile())
    return profiles