# -*- coding: utf-8 -*-

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.dialects.mysql import TIMESTAMP, TINYINT

from . import Base


class Wechat(Base):
    __tablename__ = 'wechat'

    id = Column(Integer, primary_key=True)
    openid = Column(String)
    nickname = Column(String)
    subscribe = Column(Boolean)
    sex = Column(TINYINT(4))
    city = Column(String)
    country = Column(String)
    province = Column(String)
    language = Column(String)
    headimgurl = Column(String)
    subscribe_time = Column(TIMESTAMP)
    unionid = Column(String)
    remark = Column(String)
    groupid = Column(String)
    tagid_list = Column(String)
    subscribe_scene = Column(String)
    qr_scene = Column(String)
    qr_scene_str = Column(String)
    create_time = Column(TIMESTAMP)
    unsubscribe_time = Column(TIMESTAMP)
