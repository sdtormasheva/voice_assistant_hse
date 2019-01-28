from behave import *
from modules import maps_functions, record_audio, ya_speech
from modules import additional_funcs, locations


commands = ['save', 'edit', 'delete', 'route']


@given('service is working')
def listener(context):
    context.user = "audio_files/behave_user.wav"
    context.va = "audio_files/behave_va.wav"
    context.current_task = ''
    context.current_task_finished = False
    # record_audio.listen(context.user)
    pass


@when('user says "Hello, Borya"')
def hello_boris(context):
    # hello = ya_speech.recognize(context.user)
    hello = ya_speech.recognize("audio_files/hello_boris.pcm")
    assert hello == 'привет борис'


@then('VA says "Hello"')
def hello_user(context):
    ya_speech.synthesize('Привет!', context.va)
    assert ya_speech.recognize(context.va) == "привет"


@when('User says "Yes"')
def save_confirm(context):
    assert ya_speech.recognize("audio_files/da.wav") == 'да'


@when('User says "No"')
def save_confirm(context):
    assert ya_speech.recognize("audio_files/net.wav") == 'нет'


@then('VA says "Cancelled"')
def save_confirm(context):
    ya_speech.synthesize('задача отменена', context.va)
    pass
