import datetime

from extensions import db

class TimestampMixin(object):
    created = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)