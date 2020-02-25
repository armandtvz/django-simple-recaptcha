# django-simple-recaptcha
A Django package that is essentially a fork of [Vitor Freitas']
[simple-recaptcha] repo (licensed under MIT License). Contains a decorator
for use with reCAPTCHA v2. Thanks Vitor!

This package has no tests yet—and therefore, is not production-ready.

Also, reCAPTCHA v3 and invisible reCAPTCHA is not supported yet.

[simple-recaptcha]: https://github.com/sibtc/simple-recaptcha
[Vitor Freitas']: https://github.com/vitorfs


## Quick start
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


## Required settings
```
GOOGLE_RECAPTCHA_SECRET_KEY = ''
GOOGLE_RECAPTCHA_SITE_KEY = ''
```


## License

This project is licensed under the GPL-3.0 public license. See [LICENSE].

[LICENSE]: https://github.com/armandtvz/django-simple-recaptcha/blob/master/LICENSE
