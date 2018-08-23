from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Rain
from django.template.loader import get_template
import random
import re
# Create your views here.

def homepage(request):
    terminal = request.META.get('HTTP_USER_AGENT')  #接受user-agent
    rains = Rain.objects.all()
    rain = random.choice(rains)
    title = rain.title
    content = rain.content
    if re.search('iPhone', terminal) or re.search('Android', terminal):
        template = get_template('rain/index_mt.html')
        html = template.render(locals())
        return HttpResponse(html)
    else:
        template = get_template('rain/index_pc.html')
        html = template.render(locals())
        return HttpResponse(html)