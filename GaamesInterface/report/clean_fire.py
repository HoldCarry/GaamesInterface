''''allure报告可以用到'''


import os
import shutil

def clean_fire():
    path = os.path.dirname(__file__)
    if os.path.isdir("res"):
        # 删除文件，可使用以下两种方法。
        #os.remove(res_fire)\
        shutil.rmtree("res")
        return print("已经删除文件")
    else:
        return print('no such file')




if __name__ == '__main__':
    print(clean_fire())