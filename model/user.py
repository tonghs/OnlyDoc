#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import time
import hashlib
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField


class User(Base):
    id = PrimaryKeyField()
    name = CharField()
    user_name = CharField(unique=True)
    password = CharField()
    created_time = IntegerField(default=int(time.time()))

    @classmethod
    def login(cls, user_name, password):
        admin = None
        try:
            admin = cls.get(cls.user_name == user_name,
                            cls.password == hashlib.md5(password).hexdigest())
        except cls.DoesNotExist:
            pass

        return admin

    def reset(self, new_pwd):
        self.password = hashlib.md5(new_pwd).hexdigest()
        self.save()
