
def unicode(str):
    try:
        return str.decode('UTF-8')
    except UnicodeDecodeError:
        return str.decode('GBK')

def encode(unicode_str, code='UTF-8'):
    return unicode_str.encode(code)
