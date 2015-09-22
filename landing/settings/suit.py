# coding=utf-8

__author__ = 'alexy'

SUIT_CONFIG = {
    'ADMIN_NAME': u'ENJOY-AFRICA',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',
    'MENU': (
        'sites',
        {'label': u'Перейти на сайт', 'url': 'home' },
        {'label': u'Настройки', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group', 'core.setup', 'countdown.timer')},
        {'label': u'Аватарки', 'icon':'icon-user', 'models': ('core.avatar',)},
        {'label': u'Заявки', 'icon':'icon-user', 'models': ('core.ticket', 'core.groupticket', )},
        {'label': u'Продажи', 'icon':'icon-user', 'models': ('core.sale',)},
        {'label': u'Слайдер', 'icon':'icon-picture', 'models': ('core.slider',)},
        {'label': u'Отзывы', 'icon':'icon-comment', 'models': ('core.review',)},
        {'label': u'О нас', 'app': 'about'},
        {'label': u'Журнал путешествий', 'app': 'travel'},
        {'label': u'Групповые туры', 'app': 'groups'},
        {'label': u'Форум', 'app': 'forum'},
        {'label': u'enjoy-safari.ru', 'url': 'http://www.enjoy-safari.ru/admin'},
    ),
}
