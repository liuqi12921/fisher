from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app

# 将蓝图注册到app核心对象上
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)