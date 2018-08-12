from flask import Flask

app = Flask(__name__)

# 载入自定义配置文件
#app.config.from_object('config')
# 获取配置文件的内容
#print(app.config['AUTHOR'])

# 使用装饰器进行路由注册
@app.route("/hello")
def hello():
    # 基于类的视图(即插视图)
    return 'Hello, Muye'

# 注册路由的另一种方法
# app.add_url_rule('/hello', view_func=hello)

# 确保生产环境（nginx + uwsgi）下此代码不会被执行
if __name__ == "__main__":
    # 开启调试模式 指定端口 开放网络 启动内置服务器
    app.run(host='0.0.0.0', debug=True, port=5000)
