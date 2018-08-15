from flask import Flask

def create_app():
    app = Flask(__name__)
    # 加载配置文件
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    # 注册蓝图
    register_blueprint(app)
    return app

# 将蓝图注册到app核心对象上
def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)