# -*- coding: utf-8 -*-
import os

from sqlalchemy import (BigInteger, Boolean, Column, DateTime, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

env_dist = os.environ
connect_str = env_dist.get('MYSQL_CONNECTSTRING', 'mysql+pymysql://root:addie5kaiK3@localhost:3306/syzb_spider_db?charset=utf8')

engine = create_engine(connect_str)

DBSession = sessionmaker(bind=engine)
