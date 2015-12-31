import json

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie

from .common import utils

from .models import Character

import os

@ensure_csrf_cookie
def index(request):
    character_list = Character.objects.order_by('name')

    for character in character_list:
        character.speed_slide = \
            utils.character_to_slider_opts(character.speed_options)
        character.might_slide = \
            utils.character_to_slider_opts(character.might_options)
        character.sanity_slide = \
            utils.character_to_slider_opts(character.sanity_options)
        character.knowledge_slide = \
            utils.character_to_slider_opts(character.knowledge_options)

    context = {'character_list': character_list, 'test': True}
    return render(request, 'game_tracker/index.html', context)

def reset(request):
    if "cancel" in request.POST:
        return redirect('index')
    elif "reset" in request.POST:
        Character.objects.all().delete()

        characters = None
        characters_path = os.path.join(settings.GAME_DIR, 'data', \
            'characters.json')
        with open(characters_path) as f:
            characters_json = f.read()
            characters = json.loads(characters_json)

        organized_characters = []

        current_color = None
        for character_set in characters:
            current_color = character_set["color"]

            for character in character_set["characters"]:
                new_char = Character.objects.create()

                new_char.name = character["name"]
                new_char.color = current_color

                new_char.image = character["name"].split()[0].lower() + ".png"

                new_char.speed_options = character["speed"]
                new_char.might_options = character["might"]
                new_char.sanity_options = character["sanity"]
                new_char.knowledge_options = character["knowledge"]

                new_char.speed_index = character["default_speed"]
                new_char.might_index = character["default_might"]
                new_char.sanity_index = character["default_sanity"]
                new_char.knowledge_index = character["default_knowledge"]

                new_char.save()

        return redirect('index')
    else:
        return render(request, 'game_tracker/reset.html', None)

def update_attr(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    try:
        attribute = request.POST['attribute']
        new_index = request.POST['index']
    except KeyError as e:
        return JsonResponse({'error': "Required input not specified."})

    if attribute == "speed":
        character.speed_index = new_index
    elif attribute == "might":
        character.might_index = new_index
    elif attribute == "sanity":
        character.sanity_index = new_index
    elif attribute == "knowledge":
        character.knowledge_index = new_index
    else:
        return JsonResponse({'error': 'Invalid attribute specified.'})

    character.save()

    return JsonResponse({'success': True})

def add(request):
    context = {}
    return render(request, 'game_tracker/add.html', context)
