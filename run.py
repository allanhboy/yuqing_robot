# -*- coding: utf-8 -*-
import datetime

import tornado.ioloop
import tornado.web
from werobot import WeRoBot
from werobot.contrib.tornado import make_handler

from config import config
from db import DBSession
from db.wechat import Wechat

from werobot.replies import SuccessReply

myrobot = WeRoBot(config=config)



@myrobot.subscribe
def subscribe(message):
    template_id = 'SO8Yjl0gcmNI0HW-pzgkpJqlPz0GV28llZNVoBjsspA'
    user = myrobot.client.get_user_info(message.source)
    if user:
        session = DBSession()
        wechat = session.query(Wechat).filter(
            Wechat.openid == user['openid']).one_or_none()
        if wechat:
            wechat.subscribe = True
            wechat.nickname = user['nickname']
            wechat.sex = user.get('sex', 0)
            wechat.city = user.get('city')
            wechat.country = user.get('country')
            wechat.province = user.get('province')
            wechat.language = user.get('language')
            wechat.headimgurl = user.get('headimgurl')
            wechat.subscribe_time = datetime.datetime.fromtimestamp(
                int(user['subscribe_time']))
            wechat.unionid = user.get('unionid')
            wechat.remark = user.get('remark')
            wechat.groupid = user.get('groupid')
            wechat.tagid_list = ','.join(
                [str(x) for x in user.get('tagid_list', [])])
            wechat.subscribe_scene = user.get('subscribe_scene')
            wechat.qr_scene_str = user.get('qr_scene_str')
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
        r = myrobot.client.post(
            url="https://api.weixin.qq.com/cgi-bin/message/template/send",
            data={
                "touser": message.source,
                "template_id": template_id,
                "data": {
                    "first": {
                        "value": "欢迎关注'千济方开发者开台'公众号",
                        "color": "#173177"
                    },
                    "keyword1": {
                        "value": "你可点击进入,进行账号绑定.",
                        "color": "#173177"
                    },
                    "keyword2": {
                        "value": "13888888888",
                        "color": "#173177"
                    },
                    "remark": {
                        "value": "如有疑问，请联系小孟",
                        "color": "#173177"
                    }
                },
                "miniprogram": {
                    "appid": "wx79edc80703771261",
                    #"pagepath": "pages/monitor/monitor"
                }
            }
        )
        return SuccessReply()
        # return 'Hello %s!' % user['nickname']
    else:
        return 'Hello My Friend!'


@myrobot.unsubscribe
def unsubscribe(message):
    session = DBSession()
    wechat = session.query(Wechat).filter(
        Wechat.openid == message.source).one_or_none()
    if wechat:
        wechat.subscribe = False
        wechat.unsubscribe_time = datetime.datetime.now()
    else:
        wechat = Wechat(openid=message.source, subscribe=False,
                        unsubscribe_time=datetime.datetime.now(), create_time=datetime.datetime.now())
        session.add(wechat)
    session.commit()
    session.close()

    return SuccessReply()


application = tornado.web.Application([
    (r"/robot/", make_handler(myrobot)),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
