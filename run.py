import tornado.ioloop
import tornado.web
from werobot import WeRoBot
from werobot.contrib.tornado import make_handler

from config import config

myrobot = WeRoBot(config=config)

print(myrobot.config)

@myrobot.handler
def hello(message):
    return 'Hello World!'

application = tornado.web.Application([
    (r"/robot/", make_handler(myrobot)),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()