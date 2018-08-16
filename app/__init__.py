from flask import Flask
from app.models.book import db

def create_app():
    app = Flask(__name__)
    # 加载配置文件
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    # 注册蓝图
    register_blueprint(app)
    # 关联db和核心对象
    db.init_app(app)
    db.create_all(app=app)
    return app

# 将蓝图注册到app核心对象上
def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)