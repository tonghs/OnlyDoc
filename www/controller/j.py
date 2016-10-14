#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from _base import AdminJsonBaseHandler
from misc._route import route

from model.user import User
from model.doc import Doc

from peewee import IntegrityError


@route('/j/login')
class Login(AdminJsonBaseHandler):
    def post(self):
        user_name = self.get_argument('user_name')
        password = self.get_argument('password')

        admin = User.login(user_name, password)
        if admin:
            admin_dict = dict(
                user_name=user_name,
                name=admin.name
            )
            self.set_secure_cookie("admin", json.dumps(admin_dict))
            result = dict(result=True, msg="")
        else:
            result = dict(result=False, password="用户名密码错误")

        self.finish(result)


@route('/j/user/reset_pwd')
class Pwd(AdminJsonBaseHandler):
    def post(self):
        pwd = self.get_argument('pwd')
        new_pwd = self.get_argument('new_pwd')
        re_pwd = self.get_argument('re_pwd')

        ret = dict(result=False, msg="")

        if pwd and new_pwd and re_pwd:
            if new_pwd == re_pwd:
                user = User.login(self.current_user.user, pwd)
                if user:
                    user.reset(new_pwd)
                    ret = dict(result=True, msg="修改成功！")
                else:
                    ret = dict(result=False, msg="原密码输入错误！")

            else:
                ret = dict(result=False, msg="两次输入密码不一致！")
        else:
            ret = dict(result=False, msg="全部为必填项不可为空！")

        self.finish(ret)


@route('/j/doc')
class DocHandler(AdminJsonBaseHandler):
    def post(self):
        d = dict()
        result = False
        for k, v in self.arguments.iteritems():
            if not v:
                d.update({k: '不可为空'})

        if not d:
            try:
                Doc.create(**self.arguments)
                result = True
            except IntegrityError:
                d['url'] = '该地址已经存在'

        d.update(result=result)

        self.finish(d)

    def delete(self):
        try:
            id = int(self.get_argument('id', 0))
            doc = Doc.get(Doc.id == id)
            doc.delete_instance()
        except Exception as e:
            raise e
            pass

        self.finish(dict(result=True))


@route('/j/doc/list')
class DocList(AdminJsonBaseHandler):
    def get(self):
        li = Doc.list()

        self.finish(dict(li=[o.to_dict() for o in li]))
