events = {}


def register_event(event):
    events[event.__name__] = event
    return event


@register_event
class EventA:
    pass


class EventB:
    pass


class EventC:
    pass


# events = {
#     "EventA": EventA,
#     "EventC": EventC,
# }
print(events)
