from flask import Flask
from helper import is_isbn_or_key

app = Flask(__name__)

@app.route("/book/search/<q>/<page>")
def search(q, page):
    """
    q :用户输入的查询参数
    page
    """
    isbn_or_key = is_isbn_or_key(q)
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
