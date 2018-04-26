# # -*- coding: utf-8 -*-
import werobot

from config import config

robot = werobot.WeRoBot(config=config)

@robot.text
def hello_world():
    return 'Hello World!'

robot.run()
# # # assert robot.config['HOST'] == '0.0.0.0'

# client = robot.client
# grant_token = client.grant_token()
# r = client.send_template_message('oOOJCwtFidhaYcrPQWjz61Oel_LI','THB0YXpq1xUJz9UICD5QfsgTUujwKMl8tpsq_ZY4FrQ', {
#         "first": {
#             "value": "你好,你关注的企业有新的舆情",
#             "color": "#173177"
#         },
#         "keyword1": {
#             "value": "10条新的舆情",
#             "color": "#173177"
#         },
#         "keyword2": {
#             "value": "2018年4月25日 18:36",
#             "color": "#173177"
#         },
#         "remark": {
#             "value": "点击查看",
#             "color": "#173177"
#         }
#     })
# followers = client.get_followers()

# users = client.get_users_info(followers['data']['openid'])
# print(users)
# r = client.post(url='https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={0}'.format(grant_token['access_token']), data={
#     "touser": 'oOOJCwtFidhaYcrPQWjz61Oel_LI',
#     "template_id": 'SO8Yjl0gcmNI0HW-pzgkpJqlPz0GV28llZNVoBjsspA',
#     "url": '',
#     "data": {
#         "first": {
#             "value": "内存占用",
#             "color": "#173177"
#         },
#         "keyword1": {
#             "value": "黄金",
#             "color": "#173177"
#         },
#         "keyword2": {
#             "value": "2018-4-25",
#             "color": "#173177"
#         },
#         "remark": {
#             "value": "内存占用连续10分钟超过100%",
#             "color": "#173177"
#         }
#     }
# })
# print(r)

# APP_ID ='wx1154d8019b1db191'
# APP_SECRET = '7d1931f7770c112bd6eca188c08d7064'

# import requests
# import json
# r = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'.format(APP_ID, APP_SECRET))

# if r.ok:
#     response = json.loads(r.text)
# print(response['access_token'])
