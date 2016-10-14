#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import os
import json
import mako.lookup
import mako.template
import tornado.web
from tornado.escape import json_encode

from config import STATIC_HOST, APP, DEBUG, NAME
from model.user import User
from model._base import db


class Static(object):
    def __getattr__(self, name):
        type_ = name.replace('load_', '')
        app = APP
        if type_.endswith('_'):
            app = ''

        def load(src):
            return self.load_static(app, type_, src)

        return load

    def load_static(self, app, type_, src):
        type_ = type_.replace('_', '')
        if DEBUG:
            return '/static/{type_}/{app}/{src}'.format(app=app, type_=type_, src=src)
        else:
            return '{static_host}/{type_}/{app}/{src}'.format(static_host=STATIC_HOST, type_=type_, app=app, src=src)


class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        db.connect()
        return super(BaseHandler, self).prepare()

    def on_finish(self):
        if not db.is_closed():
            db.close()

        return super(BaseHandler, self).on_finish()

    def initialize(self):
        template_path = os.path.join(os.path.dirname(__file__), '..', 'template')
        self.lookup = mako.lookup.TemplateLookup(directories=template_path,
                                                 input_encoding='utf-8',
                                                 output_encoding='utf-8')

    def render_string(self, filename, **kwargs):
        kwargs["current_user"] = self.current_user
        template = self.lookup.get_template(filename)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)

        return template.render(**namespace)

    def render(self, **kwargs):
        filename = "{0}.html".format(self._camel_to_underline(self.__class__.__name__))
        filename = "{0}{1}".format(filename[0].lower(), filename[1:])
        path = '/'.join(self.__module__.split('.')[1: -1])
        filename = os.path.join(path, filename)

        if isinstance(kwargs, dict):
            kwargs.update(STATIC=Static())
            kwargs.update(NAME=NAME)

        self.finish(self.render_string(filename, **kwargs))

    def get_current_user(self):
        j = self.get_secure_cookie("admin")
        return User.from_dict(json.loads(j)) if j else None

    def _camel_to_underline(self, camel_format):
        ''' 驼峰命名格式转下划线命名格式
        '''
        underline_format = ''
        if isinstance(camel_format, str):
            for i, _s_ in enumerate(camel_format):
                if i == 0:
                    underline_format += _s_ if _s_.islower() else _s_.lower()
                else:
                    underline_format += _s_ if _s_.islower() else '_' + _s_.lower()

        return underline_format

    @property
    def arguments(self):
        return {k: self.get_argument(k) for k, v in self.request.arguments.iteritems()}


class AdminHandler(BaseHandler):
    def prepare(self):
        if not self.current_user:
            self.redirect('/login')
        else:
            super(AdminHandler, self).prepare()


class AdminJsonBaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        j = self.get_secure_cookie("admin")
        return User.from_dict(json.loads(j)) if j else None

    def finish(self, data=None):
        if data:
            if not isinstance(data, str):
                data = json_encode(data)

            self.set_header('Content-Type', 'application/json; charset=UTF-8')
        super(AdminJsonBaseHandler, self).finish(data)

    @property
    def arguments(self):
        return {k: self.get_argument(k) for k, v in self.request.arguments.iteritems()}
