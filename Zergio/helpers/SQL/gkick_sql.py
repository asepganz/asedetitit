try:
    from Zergio.helpers.SQL import BASE, SESSION
except ImportError:
    raise AttributeError

from sqlalchemy import Column, String


class GKick(BASE):
    __tablename__ = "gkick"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


GKick.__table__.create(checkfirst=True)


def is_gkicked(sender):
    try:
        ret = SESSION.query(GKick).filter(GKick.sender == str(sender)).all()
        return len(ret) > 0
    except BaseException:
        return None
    finally:
        SESSION.close()


def gkicked_users():
    try:
        return SESSION.query(GKick).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def gkick(sender):
    adder = gkick(str(sender))
    SESSION.add(adder)
    SESSION.commit()


def ungkick(sender):
    rem = SESSION.query(gkick).get((str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()
