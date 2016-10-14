#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import hashlib
from model._base import drop_table, init_db
from model.user import User


def main():
    # drop_table()
    init_db()


def add_admin():
    User.create(user_name="tonghs", name="tonghs",
                password=hashlib.md5('tonghs').hexdigest())


if __name__ == '__main__':
    add_admin()
