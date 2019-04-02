from django.conf import settings

from . import settings as app_settings


def recaptcha_site_key(request):
    """
    Return the site key needed by reCAPTCHA
    """
    if settings.DEBUG:
        GOOGLE_RECAPTCHA_SITE_KEY = app_settings.GOOGLE_RECAPTCHA_SITE_KEY
    else:
        GOOGLE_RECAPTCHA_SITE_KEY = settings.GOOGLE_RECAPTCHA_SITE_KEY

    return {
        'recaptcha_site_key': GOOGLE_RECAPTCHA_SITE_KEY,
    }
