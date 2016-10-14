#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Route(object):
    def __init__(self):
        self.url_list = list()

    def __call__(self, url):
        def _(cls):
            self.url_list.append((url, cls))

            return cls

        return _

route = Route()
