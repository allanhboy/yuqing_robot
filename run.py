# -*- coding: utf-8 -*-
import datetime

import tornado.ioloop
import tornado.web
from werobot import WeRoBot
from werobot.contrib.tornado import make_handler

from config import config
from db import DBSession
from db.wechat import Wechat

myrobot = WeRoBot(config=config)


@myrobot.subscribe
def subscribe(message):
    user = myrobot.client.get_user_info(message.source)
    if user:
        session = DBSession()
        wechat = session.query(Wechat).filter(
            Wechat.openid == user['openid']).one_or_none()
        if wechat:
            wechat.subscribe = True
        else:
            wechat = Wechat(
                openid=user['openid'],
                nickname=user['nickname'],
                subscribe=user['subscribe'],
                sex=user.get('sex', 0),
                city=user.get('city'),
                country=user.get('country'),
                province=user.get('province'),
                language=user.get('language'),
                headimgurl=user.get('headimgurl'),
                subscribe_time=datetime.datetime.fromtimestamp(
                    int(user['subscribe_time'])),
                unionid=user.get('unionid'),
                remark=user.get('remark'),
                groupid=user.get('groupid'),
                tagid_list=','.join([str(x)
                                        for x in user.get('tagid_list', [])]),
                subscribe_scene=user.get('subscribe_scene'),
                qr_scene_str=user.get('qr_scene_str'),
                create_time=datetime.datetime.now()
            )
            session.add(wechat)
        session.commit()
        session.close()
        return 'Hello %s!' % user['nickname']
    else:
        return 'Hello My Friend!'


@myrobot.unsubscribe
def unsubscribe(message):
    return 'Goodbye My Friend!'


application = tornado.web.Application([
    (r"/robot/", make_handler(myrobot)),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
