# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2011 NovaReto GmbH

import grok
import uvc.menus.components
import uvcsite
import uvcsite.browser
import uvcsite.browser
import uvcsite.interfaces

from fanstatic import Library, Resource
from megrok.pagetemplate import PageTemplate
from uvcsite.interfaces import IUVCSite
from zope.component import getMultiAdapter
from zope.interface import Interface, implementer
from zope.pagetemplate.interfaces import IPageTemplate


grok.templatedir('templates')

library = Library('uvc.landingpage', 'static')
landing_css = Resource(library, 'landing.css')


class StartSeiteMenus(uvcsite.browser.Page):
    grok.context(uvcsite.interfaces.IUVCSite)
    grok.name('index')

    title = ""
    description = ""

    def update(self):
        landing_css.need()

    def render(self):
        template = getMultiAdapter((self, self.request), IPageTemplate)
        return template()


class StartSeite(PageTemplate):
    grok.view(StartSeiteMenus)


class StartSeiteAdapters(uvcsite.browser.Page):
    grok.context(uvcsite.interfaces.IUVCSite)
    grok.name('index')

    title = ""
    description = ""
    grok.baseclass()

    def my_iterator(self, l):
        i = 0
        s = len(l)
        while i < s:
            if i <= s - 2:
                yield l[i], l[i + 1]
            if i == s - 1:
                yield l[i],
            i += 2


class IStartSeiteItems(Interface):
    """
    MarkerInterface StartSeite
    """


@implementer(IStartSeiteItems)
class StartSeiteItems(uvc.menus.components.Menu):
    grok.name('uvc.ssi')

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
