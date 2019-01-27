from behave import *
from modules import maps_functions, record_audio, ya_speech
from modules import additional_funcs, locations


@when('user says "Save my location"')
def get_location(context):
    save_loc = ya_speech.recognize("audio_files/save_location.wav")
    assert save_loc == "сохранить текущее местоположение"
    context.location = maps_functions.get_current_geo()
    assert context.location is not None


@then(u'VA names location and asks "Confirm?"')
def approve_location(context):
    address = maps_functions.get_address(context.location)
    assert address is not None
    ya_speech.synthesize(address, context.va)
    address_clean = additional_funcs.clear_address(address)
    print(ya_speech.recognize(context.va))
    print(address_clean)
    # assert ya_speech.recognize(context.va) == address_clean
    # TODO тут косяк с сокращениями и вообще адресом
    ya_speech.synthesize('Подтверждаете?', context.va)
    assert ya_speech.recognize(context.va) == "подтверждаете"


@then('VA asks "How to name?"')
def location_name(context):
    ya_speech.synthesize('Задай имя', context.va)
    assert ya_speech.recognize(context.va) == "задай имя"


@when('User says {name}')
def location_name(context, name):
    if name != 'nothing':
        ya_speech.synthesize(name, context.user)
        context.name_to_save = ya_speech.recognize(context.user)
        assert context.name_to_save is not None
    else:
        context.name_to_save = ya_speech.recognize('audio_files/empty_file.wav')
        assert context.name_to_save is None
    if context.name_to_save is not None:
        res = locations.add_location(context.name_to_save, context.location)
        context.save_result = res


@then('VA says "Location is saved"')
def confirm_location_saved(context):
    assert context.save_result == "ok"
    ya_speech.synthesize('Место ' + context.name_to_save + ' сохранено!', context.va)
    assert ya_speech.recognize(context.va) == "место " + context.name_to_save + " сохранено"


@then('VA says "Location already exists"')
def confirm_location_saved(context):
    assert context.save_result == "already exists"
    ya_speech.synthesize('Место ' + context.name_to_save + ' уже существует!', context.va)
    assert ya_speech.recognize(context.va) == "место " + context.name_to_save + " уже существует"


@then("VA says 'Can't determine location'")
def get_location_fail(context):
    context.location = None
    assert context.location is None
    ya_speech.synthesize('Не могу определить местоположение', context.va)
    assert ya_speech.recognize(context.va) == "не могу определить местоположение"


@then(u'VA says \'Can\'t recognize name\'')
def location_name_error(context):
    assert context.name_to_save is None
