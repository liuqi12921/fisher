from myhttp import HTTP

class DouBanBook:
    isbn_url = 'https://api.douban.com/v2/book/isbn/{}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)  # json会被转换为dict
        return result
