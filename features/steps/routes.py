from behave import *
from modules import maps_functions, record_audio, ya_speech
from modules import additional_funcs, locations, directions

route_modes = ['walking', 'driving', 'transit']

# Actions ----------


@when('user says Set up route from {origin} to {destination}')
def step_impl(context, origin, destination):
    context.command = 'route'
    context.route_from = origin
    context.route_to = destination


@when(u'User says go by {mode}')
def step_impl(context, mode):
    if mode == 'foot':
        context.route_mode = 'walking'
    elif mode == 'car':
        context.route_mode = 'driving'
    elif mode == 'transport':
        context.route_mode = 'transit'
    else:
        context.route_mode = None


# Outcomes ----------


@then(u'VA validates locations')
def step_impl(context):
    context.route_from = locations.get_by_name(context.route_from)
    context.route_to = locations.get_by_name(context.route_to)


@when(u'VA asks "Which way?"')
def step_impl(context):
    assert context.route_from != 'not found'
    assert context.route_to != 'not found'


@then(u'VA says time')
def step_impl(context):
    route = directions.get_directions(context.route_from,
                                      context.route_from,
                                      context.route_mode)
    assert route is not None
    dur = directions.route_duration(route)
    ya_speech.synthesize('Маршрут займет ' + str(dur) + ' минут', context.va)


@then(u'VA says "Invalid location(s)"')
def step_impl(context):
    assert context.route_from == 'not found' or context.route_to == 'not found'


@then(u'user says "Start!"')
def step_impl(context):
    ya_speech.synthesize('Начать маршрут', context.va)
