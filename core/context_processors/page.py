__author__ = 'alexy'


def current_page(request):
    page = '/' + request.path.split('/')[1] + '/'
    return {'CURRENT_PAGE': page, }
