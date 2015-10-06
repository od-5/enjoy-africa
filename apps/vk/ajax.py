# coding=utf-8
from annoying.decorators import ajax_request
from django.views.decorators.csrf import csrf_exempt
from .models import VkUser

@csrf_exempt
@ajax_request
def check(request):
    if request.method == 'POST':
        profile_id = request.POST.get('profile_id')
        name = u'%s %s' % (request.POST.get('last_name'), request.POST.get('first_name'))
        link = request.POST.get('link')
        try:
            exist_user = VkUser.objects.get(profile_id=int(profile_id))
            exist_user.save()
            return {
                'success': u'Уже посещал'
            }
        except:
            exist_user = VkUser(name=name, profile_id=int(profile_id), link=link)
            return {
                'success': u'Ещё не посещал!'
            }
    else:
        return {
            'success': u'Ошибка!'
        }
