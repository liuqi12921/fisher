
from app import create_app

app = create_app()

if __name__ == "__main__":
    # 进行调试的时候需要将debug设置为False以阻止Flask的调试
    app.run(host='0.0.0.0', debug=False, port=5000)