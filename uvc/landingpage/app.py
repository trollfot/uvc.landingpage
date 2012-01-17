# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2011 NovaReto GmbH

import grok
import uvcsite

from fanstatic import Library, Resource
from zope.interface import Interface


grok.templatedir('templates')

library = Library('uvc.landingpage', 'static')
landing_css = Resource(library, 'landing.css')


class StartSeite(uvcsite.Page):
    grok.context(uvcsite.IUVCSite)
    grok.name('index')
    title = ""
    description = ""

    def update(self):
        landing_css.need()


class IStartSeiteItems(Interface):
    """
    MarkerInterface StartSeite
    """


class StartSeiteItems(uvcsite.Menu):
    grok.name('uvc.ssi')
    grok.implements(IStartSeiteItems)

    def my_iterator(self, l):
        i = 0
        s = len(l)
        while i < s:
            if i <= s - 2:
                yield l[i], l[i + 1]
            if i == s - 1:
                yield l[i],
            i += 2

    def getTupleItems(self):
        return self.my_iterator(self.getMenuItems())
