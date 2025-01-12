from sqlalchemy import Column, Integer, String, Sequence, Float, Text
from sqlalchemy.orm import Session

from app.db import db_query, Base


class UserRequest(Base):
    """
    用户请求表
    """
    # ID
    id = Column(Integer, Sequence('id'), primary_key=True, index=True)
    # 申请用户
    req_user = Column(String(255), index=True, nullable=False)
    # 申请时间
    req_time = Column(String(40))
    # 申请备注
    req_remark = Column(String(255))
    # 审批用户
    app_user = Column(String(255), index=True, nullable=False)
    # 审批时间
    app_time = Column(String(40))
    # 审批状态 0-待审批 1-通过 2-拒绝
    app_status = Column(Integer, default=0)
    # 类型
    type = Column(String(40))
    # 标题
    title = Column(String(255))
    # 年份
    year = Column(String(40))
    # 媒体ID
    tmdbid = Column(Integer)
    imdbid = Column(String(255))
    tvdbid = Column(Integer)
    doubanid = Column(String(255))
    bangumiid = Column(Integer)
    # 季号
    season = Column(Integer)
    # 海报
    poster = Column(Text)
    # 背景图
    backdrop = Column(Text)
    # 评分，float
    vote = Column(Float)
    # 简介
    description = Column(Text)

    @staticmethod
    @db_query
    def get_by_req_user(db: Session, req_user: str, status: int = None):
        if status:
            return db.query(UserRequest).filter(UserRequest.req_user == req_user,
                                                UserRequest.app_status == status).all()
        else:
            return db.query(UserRequest).filter(UserRequest.req_user == req_user).all()

    @staticmethod
    @db_query
    def get_by_app_user(db: Session, app_user: str, status: int = None):
        if status:
            return db.query(UserRequest).filter(UserRequest.app_user == app_user,
                                                UserRequest.app_status == status).all()
        else:
            return db.query(UserRequest).filter(UserRequest.app_user == app_user).all()

    @staticmethod
    @db_query
    def get_by_status(db: Session, status: int):
        return db.query(UserRequest).filter(UserRequest.app_status == status).all()
