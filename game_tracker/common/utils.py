import json

def character_to_slider_opts(character_opts):
    if character_opts == None or len(character_opts) < 0:
        return "[]"

    new_list = "["

    character_opts = json.loads(character_opts)

    for option in character_opts:
        if option == 0:
            new_list += "\"&#9760;\"," # HTML entity for Skull & Crossbones.
        else:
            new_list += ("\"" + str(option) + "\",")

    new_list = new_list[:-1]
    new_list += "]"

    return new_list
