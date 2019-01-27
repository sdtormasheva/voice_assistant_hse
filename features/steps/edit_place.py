from behave import *
from modules import maps_functions, record_audio, ya_speech
from modules import additional_funcs, locations


@when('User says delete {name}')
def delete_location_name(context, name):
    context.name_to_drop = name.lower()
    assert context.name_to_drop is not None
    context.name_to_drop_loc = locations.get_by_name(context.name_to_drop)


@then('VA repeats place name and address and asks "Delete?"')
def delete_location_confirm(context):
    assert context.name_to_drop_loc != 'not found'
    ya_speech.synthesize('Удалить ' + context.name_to_drop + '?', context.va)
    assert ya_speech.recognize(context.va) == "удалить " + context.name_to_drop


@then('VA says "The place is not found"')
def delete_location_not_found(context):
    assert context.name_to_drop_loc == 'not found'
    ya_speech.synthesize('Место ' + context.name_to_drop + ' не найдено', context.va)
    # assert ya_speech.recognize(context.va) == "место " + context.name_to_drop + " не найдено"
