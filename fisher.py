#import json
from flask import Flask
from flask import jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook



app = Flask(__name__)

@app.route("/book/search/<q>/<page>")
def search(q, page):
    """
    q :用户输入的查询参数
    page
    """
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    # dict序列化 使用python自带json模块
    # return json.dumps(result), 200, {'content-type':'application/json'}

    # dict序列化 使用flask的jsonify
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
