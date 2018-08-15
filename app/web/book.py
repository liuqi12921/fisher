from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web

# 将视图函数注册到蓝图上
@web.route("/book/search")
def search():
    """
    q :用户输入的查询参数
    page
    """
    # q = request.args['q']
    # page = request.args['page']

    form = SearchForm(request.args)
    # 进行验证
    if form.validate():
        # 通过form取得q和page的值
        q = form.q.data.strip() # 去除q前后的空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        return jsonify(result)
    else:
        return jsonify(form.errors)
