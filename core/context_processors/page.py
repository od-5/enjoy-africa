from apps.seo.models import Page

__author__ = 'alexy'


def current_page(request):
    page = '/' + request.path.split('/')[1] + '/'
    page_slug = request.path.split('/')[1]
    print(page_slug)
    try:
        qs = Page.objects.get(page=page_slug)
        print qs
    except:
        qs = False

    return {'CURRENT_PAGE': page,
            'seo': qs,
            }
