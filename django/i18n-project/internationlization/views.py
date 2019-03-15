from django.shortcuts import render
from django.http import HttpResponse
from django.utils import translation
from django.utils.translation import ugettext as _


def test(request):
    user_language = request.GET.get('lang_code', 'en')  # 接受url的参数，设置语音
    translation.activate(user_language)  # 将全局语言设置为user_language
    output = _('hello my world!')
    return HttpResponse(output)


def hello(request):
    user_language = request.GET.get('lang_code', 'en')
    translation.activate(user_language)
    output = _('i am back to forward')
    return render(request, 'test.html', {'data': output})
