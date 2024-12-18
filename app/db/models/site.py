from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, Sequence, JSON, Text
from sqlalchemy.orm import Session

from app.db import db_query, db_update, Base


class Site(Base):
    """
    站点表
    """
    id = Column(Integer, Sequence('id'), primary_key=True, index=True)
    # 站点名
    name = Column(String(255), nullable=False)
    # 域名Key
    domain = Column(String(255), index=True)
    # 站点地址
    url = Column(String(255), nullable=False)
    # 站点优先级
    pri = Column(Integer, default=1)
    # RSS地址，未启用
    rss = Column(Text)
    # Cookie
    cookie = Column(Text)
    # User-Agent
    ua = Column(Text)
    # ApiKey
    apikey = Column(String(255))
    # Token
    token = Column(String(255))
    # 是否使用代理 0-否，1-是
    proxy = Column(Integer)
    # 过滤规则
    filter = Column(String(255))
    # 是否渲染
    render = Column(Integer)
    # 是否公开站点
    public = Column(Integer)
    # 附加信息
    note = Column(JSON)
    # 流控单位周期
    limit_interval = Column(Integer, default=0)
    # 流控次数
    limit_count = Column(Integer, default=0)
    # 流控间隔
    limit_seconds = Column(Integer, default=0)
    # 超时时间
    timeout = Column(Integer, default=15)
    # 是否启用
    is_active = Column(Boolean(), default=True)
    # 创建时间
    lst_mod_date = Column(String(40), default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # 下载器
    downloader = Column(String(40))

    @staticmethod
    @db_query
    def get_by_domain(db: Session, domain: str):
        return db.query(Site).filter(Site.domain == domain).first()

    @staticmethod
    @db_query
    def get_actives(db: Session):
        result = db.query(Site).filter(Site.is_active == 1).all()
        return list(result)

    @staticmethod
    @db_query
    def list_order_by_pri(db: Session):
        result = db.query(Site).order_by(Site.pri).all()
        return list(result)

    @staticmethod
    @db_query
    def get_domains_by_ids(db: Session, ids: list):
        result = db.query(Site.domain).filter(Site.id.in_(ids)).all()
        return [r[0] for r in result]

    @staticmethod
    @db_update
    def reset(db: Session):
        db.query(Site).delete()
