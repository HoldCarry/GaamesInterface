import os

def get_path():
    path = os.path.dirname(__file__)
    return path

if __name__ == '__main__':
    print("这个应该是路径",get_path())
