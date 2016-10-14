#!usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField
from form.category import CategoryForm


class Category(Base):
    id = PrimaryKeyField()
    name = CharField(unique=True)
    parent = IntegerField(default=0)
    created_time = IntegerField(default=int(time.time()))

    Form = CategoryForm

    @classmethod
    def top(cls):
        return cls.select().where(cls.parent == 0).order_by(cls.created_time.desc())

    @classmethod
    def sub(cls):
        return cls.select().where(cls.parent != 0).order_by(cls.created_time.desc())

    @classmethod
    def list(cls, page=1, limit=20):
        count = cls.select().count()
        page = 1 if page < 1 else page
        total_page = 0

        total_page, mod = divmod(count, limit)
        total_page = total_page + 1 if mod else total_page

        if page > total_page:
            page = total_page

        return cls.select().order_by(cls.created_time.desc()).paginate(page, limit), count, total_page

    @property
    def parent_(self):
        return '' if self.parent == 0 else self.get(Category.id == self.parent).name
