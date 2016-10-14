#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tornado.ioloop
import tornado.web

from config import PORT, DEBUG, HOST, COOKIE_SECRET
import _url  # noqa
from misc._route import route

reload(sys)
sys.setdefaultencoding('utf-8')


def make_app():
    return tornado.web.Application(route.url_list, debug=DEBUG,
                                   cookie_secret=COOKIE_SECRET)

if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)

    print 'Listening at {host}:{port}'.format(host=HOST, port=PORT)
    tornado.ioloop.IOLoop.current().start()
