# Common conext processor

import settings_yqn.settings

def common(request):

    return {
        "DEBUG" : settings_yqn.settings.DEBUG,
        "QUAKRAPP" : "quakrapp" in request.META['HTTP_USER_AGENT'],
    }
