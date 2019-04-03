from functools import wraps

from django.conf import settings
from django.contrib import messages

import requests

from . import settings as app_settings
from . import utils


def check_recaptcha(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):

        request.recaptcha_is_valid = None
        if utils.recaptcha_is_valid(request):
            request.recaptcha_is_valid = True
        else:
            request.recaptcha_is_valid = False

        return view_func(request, *args, **kwargs)
    return _wrapped_view
