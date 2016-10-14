#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa

from _base import BaseHandler, AdminHandler
from misc._route import route


@route('/login')
class Login(BaseHandler):
    def get(self):
        self.render()


@route('/')
class Index(AdminHandler):
    def get(self):
        self.render()


@route('/logout')
class Logout(AdminHandler):
    def get(self):
        self.clear_cookie('user')
        self.redirect('/')
