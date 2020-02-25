# Quickstart
1. Install the app using:
```
pip install git+https://github.com/armandtvz/django-simple-recaptcha.git
```

1. Add "recaptcha" to your INSTALLED_APPS setting:
```python
INSTALLED_APPS = [
    ...
    'recaptcha',
]
```

1. Add the following to the MIDDLEWARE setting:
```python
MIDDLEWARE = [
    '...',
    'recaptcha.middleware.ReCaptchaCredentialMiddleware',
]
```

1. Add the following to your settings.py file (remember to always protect secret keys appropriately):
```python
# These settings will only be used in production.
GOOGLE_RECAPTCHA_SITE_KEY = <recaptcha_site_key>
GOOGLE_RECAPTCHA_SECRET_KEY = <recaptcha_secret_key>
```

1. Add the required JS to the template:
```html
<script src="https://www.google.com/recaptcha/api.js" async defer></script>
```

1. Add the reCAPTCHA checkbox to the template:
```html
<div class="g-recaptcha" data-sitekey="{{ request.recaptcha_site_key }}"></div>
<!-- Or use the checkbox template -->
{% include "recaptcha/checkbox.html" %}
```
