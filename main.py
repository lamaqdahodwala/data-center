import tornado.ioloop
from tornado.web import RequestHandler, Application, url
import string
import random
from replit import db
import json



class HomeHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
    def get(self):
        self.write('pranked')


class UpdateHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
    def get(self, token, item, amount):
        if token in db.keys():
            if item in db[token].keys():
                item += amount
                self.write('success')
                self.set_status(200)
            else:
                self.write('err: item doesn\'t exist')
                self.set_status(404)
                return
        else:
            self.write('err: token doesn\'t exist.')
            self.set_status(404)
            return

class GenerationHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
    def exists(self, token):
        if token in db.keys():
            return True
        else:
            return False
    def get(self):
        letters = list(string.ascii_letters)
        tkn = ''
        for i in range(50):
            tkn += random.choice(letters)
        if self.exists(tkn):
            self.get()
        else:
            self.write(tkn)
            with open('stock.json') as f:
                stock = json.load(f)
            db[tkn] = stock
        


def main():
    return Application([
        url(r'/', HomeHandler),
        url(r'/updateitem/(.+)/(.+)/(\d+)', UpdateHandler),
        url(r'/generate', GenerationHandler)

    ])
if __name__ == '__main__':
    app = main()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
