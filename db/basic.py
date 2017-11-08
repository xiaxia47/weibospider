import os

from sqlalchemy import (
    create_engine, MetaData)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import get_db_args


def get_engine():
    args = get_db_args()
    password = os.getenv('DB_PASS', args['password'])
    connect_str = "{}+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(args['db_type'], args['user'], password,
                                                             args['host'], args['port'], args['db_name'])
    engine = create_engine(connect_str, encoding='utf-8')
    return engine


eng = get_engine()
#declarative_base类维持了一个从类到表的关系，通常一个应用使用一个base实例，所有实体类都应该继承此类对象
#http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/api.html?highlight=declarative_base#sqlalchemy.ext.declarative.declarative_base
Base = declarative_base()
#创建一个mysql的session,管理和维护所有和mysql相关的数据库操作
#http://docs.sqlalchemy.org/en/latest/orm/session_api.html?highlight=sessionmaker#sqlalchemy.orm.session.sessionmaker
Session = sessionmaker(bind=eng)
db_session = Session()
#创建MetaData对象，用来对表进行管理，如建新表，或者删除不需要的表。此处主要为创建缺失数据表
#http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/basic_use.html?highlight=metadata#accessing-the-metadata
metadata = MetaData(get_engine())


__all__ = ['eng', 'Base', 'db_session', 'metadata']
