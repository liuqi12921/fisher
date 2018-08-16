
# 导入Flask核心对象
from flask import Flask, current_app

app = Flask(__name__)

# 手动将应用上下文压栈
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

# 一种更好的写法
# 但是这里 current_app还是unbound，还不知为何？
# with app.app_context():
#     a = current_app
#     d = current_app.config['DEBUG']


class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if tb:
            print('process exception')
        else:
            print('no exception')
        print('close resource connection')
        return False

    def query(self):
        print('query data')

try:
    with MyResource() as resource:
        resource.query()
except Exception as ex:
    pass