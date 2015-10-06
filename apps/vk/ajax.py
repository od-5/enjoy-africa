# coding=utf-8
from annoying.decorators import ajax_request
from .models import VkUser


@ajax_request
def check(request):
    if request.method == 'POST':
        profile_id = request.POST.get('profile_id')
        ip = request.META['REMOTE_ADDR']
        try:
            exist_user = VkUser.objects.get(profile_id=int(profile_id))
            return {
                'success': u'Уже посещал'
            }
        except:
            exist_user = None
            return {
                'success': u'Ещё не посещал!'
            }
    else:
        return {
            'success': u'Ошибка!'
        }
