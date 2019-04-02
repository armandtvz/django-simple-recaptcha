from django.conf import settings

import requests

from . import settings as app_settings


def recaptcha_is_valid(request):
    if request.method == 'POST':
        if settings.DEBUG:
            GOOGLE_RECAPTCHA_SECRET_KEY = app_settings.GOOGLE_RECAPTCHA_SECRET_KEY
        else:
            GOOGLE_RECAPTCHA_SECRET_KEY = settings.GOOGLE_RECAPTCHA_SECRET_KEY

        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response,
        }
        r = requests.post(app_settings.GOOGLE_RECAPTCHA_VERIFY_URL, data=data)
        result = r.json()
        if result['success']:
            return True
        else:
            return False
    return False
