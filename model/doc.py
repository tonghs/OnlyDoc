#!usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField


class Doc(Base):
    id = PrimaryKeyField()
    icon = CharField()
    name = CharField(unique=True)
    url = CharField(unique=True)
    order = IntegerField(default=0)
    created_time = IntegerField(default=int(time.time()))

    @classmethod
    def list(cls):
        return cls.select().order_by(cls.created_time.desc(), cls.order.desc())
