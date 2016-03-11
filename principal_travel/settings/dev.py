from .base import *

DEBUG = True

DEV_APPS = [
    'debug_toolbar',
]

INSTALLED_APPS = PREREQ_APPS + DEV_APPS + PROJECT_APPS

DEBUG_TOOLBAR_MIDDLEWARE = 'debug_toolbar.middleware.DebugToolbarMiddleware'

MIDDLEWARE_CLASSES = [ DEBUG_TOOLBAR_MIDDLEWARE ] + MIDDLEWARE_CLASSES

def show_toolbar(request):
    if request.is_ajax():
        return False
    return True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'principal_travel.settings.dev.show_toolbar',
}
