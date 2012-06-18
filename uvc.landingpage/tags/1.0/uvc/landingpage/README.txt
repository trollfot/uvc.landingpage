=======
Doctest
=======

uvc.landingpage

EXAMPLES: ...

class MyItem(uvcsite.MenuItem):
    grok.viewletmanager(IStartSeiteItems)
    grok.context(uvcsite.IUVCSite)
    grok.description('BLA BLA BLA 10')
    grok.order(10)

    action = "startuaz"
    title = "unfallanzeige"
    description = "beschreibung"
    icon = "fanstatic/uvc.landingpage/unfallanzeige.gif"


class MyItemENW(uvcsite.MenuItem):
    grok.viewletmanager(IStartSeiteItems)
    grok.context(uvcsite.IUVCSite)
    grok.description('BLA BLA BLA 20')
    grok.order(20)

    action = "startuaz"
    title = "unfallanzeige"
    description = "beschreibung"
    icon = "fanstatic/uvc.landingpage/unfallanzeige.gif"


class MyItemEN(uvcsite.MenuItem):
    grok.viewletmanager(IStartSeiteItems)
    grok.context(uvcsite.IUVCSite)
    grok.description('BLA BLA BLA 30')
    grok.order(30)

    action = "startuaz"
    title = "unfallanzeige"
    description = "beschreibung"
    icon = "fanstatic/uvc.landingpage/deuv_meldung.gif"
