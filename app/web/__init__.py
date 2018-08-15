
from flask import Blueprint

# 使用Flask蓝图用以分离视图函数
web = Blueprint('web', __name__)

# 需要导入这些模块，不然无法注册成功
# 这里虽然存在循环导入，但是python中一个模块只能被导入一次
# 这里的语句需要放在 web = Blueprint('web', __name__) 之后 思考？
from app.web import book
from app.web import user

