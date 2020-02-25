from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

from . import settings as app_settings


class ReCaptchaCredentialMiddleware(MiddlewareMixin):

    """
    Middleware that sets `site` attribute to request object.
    """

    def process_request(self, request):
        GOOGLE_RECAPTCHA_SITE_KEY = None
        if settings.DEBUG:
            GOOGLE_RECAPTCHA_SITE_KEY = app_settings.GOOGLE_RECAPTCHA_SITE_KEY
        else:
            GOOGLE_RECAPTCHA_SITE_KEY = settings.GOOGLE_RECAPTCHA_SITE_KEY

        request.recaptcha_site_key = GOOGLE_RECAPTCHA_SITE_KEY
