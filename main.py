import tornado.ioloop
from tornado.web import RequestHandler, Application, url
from replit import db


class HomeHandler(RequestHandler):
    def get(self):
        self.write('pranked')

class UpdateHandler(RequestHandler):
    def get(self, token, item, amount):
        if token in db.keys():
            if item in db[token].keys():
                item += amount
                self.write('success')
            else:
                self.write('err: item doesn\'t exist')
                return
        else:
            self.write('err: token doesn\'t exist.')
            return

def main():
    return Application([
        url(r'/', HomeHandler),
        url(r'/updateitem/(.+)/(.+)/(\d+)', UpdateHandler))
    ])
if __name__ == '__main__':
    app = main()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
