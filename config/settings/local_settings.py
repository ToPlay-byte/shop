from config.settings.development import *


SECRET_KEY = 'django-insecure-m4k50--bf&cz$r(e6n%zr2z#*e5iw)7@qc^^wk=%o%j%kdx=zq'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shop',
        'USER': 'postgres',
        'PASSWORD': 'doomdoom2002',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '260975407387-rkehkl0hinmid08oh123mbkdjaifo2bp.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_HOST_USER = 'oleksandr.hnylosyr@gmail.com'
EMAIL_HOST_PASSWORD = 'E6T0NGBwrgq8V19H'
EMAIL_PORT = '587'
