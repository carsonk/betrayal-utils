from django.shortcuts import render

from .models import Character

def index(request):
    character_list = Character.objects.order_by('name')
    context = {'character_list': character_list, 'test': True}
    return render(request, 'game_tracker/index.html', context)
