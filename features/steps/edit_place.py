from behave import *
from modules import maps_functions, record_audio, ya_speech
from modules import additional_funcs, locations


@when('User says delete {name}')
def delete_location_name(context, name):
    context.name_active = name.lower()
    context.name_active_loc = locations.get_by_name(context.name_active)
    pass


@then('VA repeats place name and address')
def delete_location_confirm(context):
    assert context.name_active_loc != 'not found'
    address = maps_functions.get_address(context.name_active_loc)
    ya_speech.synthesize(context.name_active + ' ' + address, context.va)


@then('VA asks "Delete?"')
def delete_location_confirm(context):
    ya_speech.synthesize('Удалить?', context.va)
    pass


@then('VA says "The place is not found"')
def delete_location_not_found(context):
    assert context.name_active_loc == 'not found'
    ya_speech.synthesize('Место ' + context.name_active + ' не найдено', context.va)


@then('VA deletes place and says "Deleted"')
def delete_location(context):
    res = locations.remove_location(context.name_active)
    assert res == "ok"
    assert locations.get_by_name(context.name_active) == 'not found'
    ya_speech.synthesize('Удалено', context.va)
    assert ya_speech.recognize(context.va) == "удалено"


@when('User says edit {name}')
def delete_location_name(context, name):
    context.name_active = name.lower()
    context.name_active_loc = locations.get_by_name(context.name_active)
    pass


@then('VA asks "Confirm?"')
def delete_location_confirm(context):
    ya_speech.synthesize('Все верно?', context.va)
    pass

