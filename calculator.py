import re
from decimal import *

def home():
    #all_books = DB.titles()
    #body = ['<h1>My Bookshelf</h1>', '<ul>']
    #item_template = '<li><a href="/book/{id}">{title}</a></li>'
    #for book in all_books:
    #    body.append(item_template.format(**book))
    #body.append('</ul>')
    return '''Welcome to a trivial calculator app!''' #'\n'.join(body)

def multiply(num1, num2):
    answer = Decimal(num1) * Decimal(num2)
    return "Hey, you're answer is {}".format(answer)

def divide(num1, num2):
    if num2 == 0:
      raise NameError
    answer = Decimal(num1) / Decimal(num2)
    return "Hey, you're answer is {}".format(answer)

def add(num1, num2):
    answer = Decimal(num1) + Decimal(num2)
    return "Hey, you're answer is {}".format(answer)

def subtract(num1, num2):
    answer = Decimal(num1) - Decimal(num2)
    return "Hey, you're answer is {}".format(answer)

def resolve_path(path):
    urls = [(r'^$', home),
            (r'^multiply/(\d+\.?\d?)/(\d+\.?\d?)$', multiply),
            (r'^divide/(\d+\.?\d?)/(\d+\.?\d?)$', divide),
            (r'^add/(\d+\.?\d?)/(\d+\.?\d?)$', add),
            (r'^subtract/(\d+\.?\d?)/(\d+\.?\d?)$', subtract),
              ]
    matchpath = path.lstrip('/')
    for regexp, func in urls:
        match = re.match(regexp, matchpath)
        if match is None:
            continue
        args = match.groups([])
        return func, args
    # we get here if no url matches
    raise NameError


def application(environ, start_response):
    headers = [("Content-type", "text/html")]
    try:
        path = environ.get('PATH_INFO', None)
        if path is None:
            raise NameError
        func, args = resolve_path(path)
        body = func(*args)
        status = "200 OK"
    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    except Exception:
        if func == divide and args[1] == 0:
            status = "500 Internal Server Error"
            body = "<h1>Internal Server Error</h1>"
        else:
            status = "404 Not Found"
            body = "<h1>Can't divide by zero!</h1>"
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        return [body]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8000, application)
    srv.serve_forever()