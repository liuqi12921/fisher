from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

print('id为' + str(id(app)) + '的app实例化')

from app.web import book

if __name__ == "__main__":
    # 进行调试的时候需要将debug设置为False以阻止Flask的调试
    app.run(host='0.0.0.0', debug=False, port=5000)

