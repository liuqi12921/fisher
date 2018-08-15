
def is_isbn_or_key(word):
    """
    判断输入是否为isbn
    :param word: 用于判断的字符串
    :return: key or isbn
    """
    isbn_or_key = 'key'

    # 判断是否为isbn13
    # isbn13 13个0-9的数字组成
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    # 判断是否为isbn10
    # isbn10 10个0-9的数字，包含'-'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key