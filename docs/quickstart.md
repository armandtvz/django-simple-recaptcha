# Quickstart

1. `pip install git+https://github.com/armandtvz/django-simple-recaptcha.git`

1. Add the following to your settings.py file
```
GOOGLE_RECAPTCHA_SITE_KEY = site_key
GOOGLE_RECAPTCHA_SECRET_KEY = secret_key
```

1. Add the recaptcha context processor to the TEMPLATES setting
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                '...',
                'recaptcha.context_processors.recaptcha_site_key',
            ],
        },
    },
]
```
