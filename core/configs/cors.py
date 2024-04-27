from core.env import env

CORS_ORIGIN_ALLOW_ALL = False
ALLOWED_HOSTS = env.get_value(var='ALLOWED_HOSTS', cast=list)
CSRF_TRUSTED_ORIGINS = env.get_value(var='CSRF_TRUSTED_ORIGINS', cast=list)
CORS_ALLOWED_ORIGINS = env.get_value(var='CORS_ALLOWED_ORIGINS', cast=list, default=['127.0.0.1'])
