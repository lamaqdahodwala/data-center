import tornado.ioloop
from tornado.web import RequestHandler, Application, url
from replit import db

class MainHandler(RequestHandler):
    def get(self):
        self.write('ur mom')
        self.write('<br>')
        self.write('<a href="https://apple.com">xdxd</a>')

class NiceHandler(RequestHandler):
    def get(self):
        self.write('nice')

def main():
    return Application([
        url(r'/', MainHandler),
        url(r'/nice', NiceHandler)
    ])


if __name__ == '__main__':
    app = main()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
