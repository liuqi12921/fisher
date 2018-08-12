from flask import Flask

app = Flask(__name__)

@app.route("/book/search/<q>/<page>")
def search(q, page):
    """
    q :普通关键字 isbn
    page
    """

    # isbn13 13个0-9的数字组成
    # isbn10 10个0-9的数字，包含'-'

    isbn_or_key = 'key' # 默认q为关键字

    # 判断是否为isbn13
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'

    # 判断是否为isbn10
    short_q = q.replace('-', '')
    if '-' in q and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'

    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
