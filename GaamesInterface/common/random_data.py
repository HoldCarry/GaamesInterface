import random
import string

#该py文件用于生成随机的值

#生成随机字符串，现用于生成应用详情评论所需要的包名
def random_str():
    #定义一个com开头的字符串
    str1 = "com"
    #获取a-zA-Z字母随机组成的8位长度的第一个随机字符串
    ran_str1 = ''.join(random.sample(string.ascii_letters, 8))
    # 获取a-zA-Z字母随机组成的8位长度的第二个随机字符串
    ran_str2 = ''.join(random.sample(string.ascii_letters, 8))
    #把三个字符串和.一起组成新的包名
    new_ran_str = str1 + "." + ran_str1 + "." + ran_str2
    return  new_ran_str

def random_int():
    #获取10000000-99999999之间的一个int类型的整数
    new_random_int = random.randint(10000000,99999999)
    return new_random_int

if __name__ == '__main__':
    print(random_str())
    print(random_int())
