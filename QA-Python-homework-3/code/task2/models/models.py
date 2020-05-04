from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Log(Base):
    __tablename__ = 'logs'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(40), nullable=False)
    user = Column(String(30), nullable=True)
    timestamp = Column(TIMESTAMP, nullable=False)
    method = Column(String(10), nullable=False)
    url = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False, default=0)
    referer = Column(String(30), nullable=True)
    user_agent = Column(String(200), nullable=True)
    forwarded_for = Column(String(50), nullable=True)

    def __repr__(self):
        return f"<Log(" \
               f"id='{self.id}'," \
               f"address='{self.address}', " \
               f"user='{self.user}', " \
               f"timestamp='{self.timestamp}', " \
               f"method='{self.method}', " \
               f"url='{self.url}'" \
               f"status='{self.status}', " \
               f"size='{self.size}'" \
               f"referer='{self.referer}', " \
               f"user_agent='{self.user_agent}', " \
               f"forwarded_for='{self.forwarded_for}'" \
               f")>"


class ClientError(Base):
    __tablename__ = 'client_errors'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Log(" \
               f"id='{self.id}'," \
               f"url='{self.url}'" \
               f"status='{self.status}', " \
               f"count='{self.count}'" \
               f")>"


class ServerError(Base):
    __tablename__ = 'server_errors'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Log(" \
               f"id='{self.id}'," \
               f"url='{self.url}'" \
               f"status='{self.status}', " \
               f"count='{self.count}'" \
               f")>"


class BiggestRequest(Base):
    __tablename__ = 'biggest_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    method = Column(String(10), nullable=False)
    url = Column(String(50), nullable=False)
    address = Column(String(40), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
    size = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Log(" \
               f"id='{self.id}'," \
               f"address='{self.address}', " \
               f"timestamp='{self.timestamp}', " \
               f"method='{self.method}', " \
               f"url='{self.url}'" \
               f"size='{self.size}'" \
               f")>"
