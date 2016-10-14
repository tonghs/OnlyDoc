#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa

from pub_config import MYSQL
from peewee import Model, MySQLDatabase

from playhouse.shortcuts import model_to_dict, dict_to_model

db = MySQLDatabase(MYSQL.DB, user=MYSQL.USER, password=MYSQL.PWD, host=MYSQL.HOST)


class Base(Model):

    def to_dict(self, **kwargs):
        return model_to_dict(self, **kwargs)

    @classmethod
    def from_dict(cls, d):
        return dict_to_model(cls, d) if d else None

    class Meta:
        database = db


def init_db():
    from model.user import User
    from model.doc import Doc

    # 创建表
    # db.create_tables([User])
    db.create_tables([Doc])


def drop_table():
    from model.user import User
    from model.local_auth import LocalAuth

    db.drop_tables([User, LocalAuth])
