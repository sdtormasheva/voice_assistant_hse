from behave import *
from modules import maps_functions, record_audio, ya_speech
from modules import additional_funcs, locations


@when('User says delete {name}')
def delete_location_name(context, name):
    context.name_active = name.lower()
    context.name_active_loc = locations.get_by_name(context.name_active)
    pass


@then('VA repeats place name and address')
def step_impl(context):
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
    context.name_active = None
    ya_speech.synthesize('Удалено', context.va)
    assert ya_speech.recognize(context.va) == "удалено"


@when('User says edit {name}')
def step_impl(context, name):
    context.name_active = name.lower()
    context.name_active_loc = locations.get_by_name(context.name_active)


@then('VA asks "Confirm?"')
def step_impl(context):
    ya_speech.synthesize('Все верно?', context.va)
    pass


@then(u'VA asks "What would you like to change, name or address?"')
def step_impl(context):
    assert context.name_active_loc != 'not found'
    ya_speech.synthesize('Вы хотите изменить имя или адрес?', context.va)
    pass


@when('user says "Change name"')
def step_impl(context):
    context.change_property = 'name'
    pass


@then(u'VA asks "What is the new name?"')
def step_impl(context):
    ya_speech.synthesize('Задайте новое имя', context.va)
    pass


@when('User says new name is {name}')
def location_name_new(context, name):
    if name != 'nothing':
        assert context.name_active is not None
        context.name_new = name.lower()
    else:
        context.name_new = ya_speech.recognize('audio_files/empty_file.wav')
        assert context.name_new is None


@then(u'VA names updated location and asks "Confirm?"')
def step_impl(context):
    if context.change_property == 'name':
        address = maps_functions.get_address(context.name_active_loc)
        assert address is not None
        name = context.name_new
    elif context.change_property == 'address':
        address = context.address_new
        name = context.name_active
    else:
        assert False
    ya_speech.synthesize(address, context.va)
    # address_clean = additional_funcs.clear_address(address)
    # assert ya_speech.recognize(context.va) == address_clean
    # TODO тут косяк с сокращениями и вообще адресом
    ya_speech.synthesize('Подтверждаете?', context.va)
    assert ya_speech.recognize(context.va) == "подтверждаете"


@then('VA updates location and says "Location is updated"')
def confirm_location_upd(context):
    if context.change_property == 'name':
        loc = context.name_active_loc
        assert loc is not None
        name_new = context.name_new
        name_old = context.name_active
    elif context.change_property == 'address':
        loc = maps_functions.get_geo(context.address_new)
        assert loc is not None
        name_new = context.name_active
        name_old = name_new
    else:
        assert False
    res = locations.remove_location(name_old)
    assert res == "ok"
    res = locations.add_location(name_new, loc)
    assert res == "ok"
    context.name_active = None
    ya_speech.synthesize('Место изменено', context.va)
    assert ya_speech.recognize(context.va) == "место изменено"


@when('user says "Change address"')
def step_impl(context):
    context.change_property = 'address'
    pass


@then(u'VA asks "What is the new address?"')
def step_impl(context):
    ya_speech.synthesize('Задайте новое местоположение', context.va)
    pass


@when('User says new address is {address}')
def step_impl(context, address):
    context.address_new = address
    pass


@then(u'VA says \'Can\'t recognize new name\'')
def location_name_error(context):
    assert context.name_new is None
