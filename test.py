from db.wechat import Wechat
import datetime

user = {
    "subscribe": 1,
    "openid": "o6_bmjrPTlm6_2sgVt7hMZOPfL2M",
    "nickname": "Band",
    "sex": 1,
    "language": "zh_CN",
    "city": "广州",
    "province": "广东",
    "country": "中国",
    "headimgurl": "http://thirdwx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/0",
    "subscribe_time": 1382694957,
    "unionid": "o6_bmasdasdsad6_2sgVt7hMZOPfL",
    "remark": "",
    "groupid": 0,
    "subscribe_scene": "ADD_SCENE_QR_CODE",
    "qr_scene": 98765,
    
}
http://thirdwx.qlogo.cn/mmopen/eXMQPRQRrggRPbfrbt1sx5l7oxibFUVynk1m7e5wO6LJKPmgAUH9ZDTG1rTUGsrUWUVEG6MxLDxeic5DsI9GIrG6SOY7wiaZyVm/132
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
                    tagid_list=','.join([str(x) for x in user.get('tagid_list', [])]),
                    subscribe_scene=user.get('subscribe_scene'),
                    qr_scene_str=user.get('qr_scene_str'),
                    create_time=datetime.datetime.now()
                )

print(wechat.subscribe_time)



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
