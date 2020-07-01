from sqlalchemy import DateTime, text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    """base class of all table model"""
    __abstract__ = True

    create_time = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    update_time = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
