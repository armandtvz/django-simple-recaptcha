# django-simple-recaptcha
A Django package that is essentially a fork of [Vitor Freitas']
[simple-recaptcha] repo (licensed under MIT License). Contains a decorator
for use with reCAPTCHA v2. Thanks Vitor!

This package has no tests yet—and therefore, is not production-ready.

Also, reCAPTCHA v3 and invisible reCAPTCHA is not supported yet.

[simple-recaptcha]: https://github.com/sibtc/simple-recaptcha
[Vitor Freitas']: https://github.com/vitorfs


## Quickstart
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


## License

This project is licensed under the GPL-3.0 public license. See [LICENSE].

[LICENSE]: https://github.com/armandtvz/django-simple-recaptcha/blob/master/LICENSE
