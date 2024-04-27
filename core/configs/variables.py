from core.env import env

DOMAIN = env.get_value('DOMAIN')
TIME_ZONE = env.get_value('TIMEZONE', default='Africa/Nairobi')

# Email
EMAIL_PORT = env.get_value('EMAIL_PORT')
EMAIL_HOST = env.get_value('EMAIL_HOST')
EMAIL_HOST_USER = env.get_value('EMAIL_HOST_USER')
EMAIL_USE_TLS = env.get_value('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = env.get_value('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = env.get_value('EMAIL_HOST_PASSWORD')


# Celery
CELERY_TIMEZONE = env.get_value('TIMEZONE', default='Africa/Nairobi')
CELERY_BROKER_URL = env.get_value("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env.get_value("CELERY_RESULT_BACKEND")

# Rest Framework
PAGINATION_PAGE_SIZE = env.get_value('PAGINATION_PAGE_SIZE')
