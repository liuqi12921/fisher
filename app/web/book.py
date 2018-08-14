from flask import jsonify, Blueprint
from helper import is_isbn_or_key
from yushu_book import YuShuBook


# 使用Flask蓝图用以分离视图函数

web = Blueprint('web', __name__)


# 将视图函数注册到蓝图上
@web.route("/book/search/<q>/<page>")
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

    return jsonify(result)
