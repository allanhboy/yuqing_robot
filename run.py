import tornado.ioloop
import tornado.web
from werobot import WeRoBot
from werobot.contrib.tornado import make_handler

from config import config

myrobot = WeRoBot(config=config)

print(myrobot.config)

@myrobot.subscribe
def subscribe(message):
    print(message)
    return 'Hello My Friend!'

@myrobot.unsubscribe
def unsubscribe(message):
    print(message)
    return 'Goodbye My Friend!'

application = tornado.web.Application([
    (r"/robot/", make_handler(myrobot)),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()