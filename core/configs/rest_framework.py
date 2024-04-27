from core.env import env
from datetime import timedelta


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': env.get_value('PAGINATION_PAGE_SIZE', cast=int),
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=14),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=14),
    "USER_ID_CLAIM": "id",
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Customer Management API',
    'DESCRIPTION': 'Api for collecting and managing customer information',
    'VERSION': 'v1',
    'CONTACT': {
        'email': "mwevibrian@gmail.com",
    },
    'SERVE_INCLUDE_SCHEMA': False,
    'SCHEMA_PATH_PREFIX_INSERT': env.get_value('SCHEMA_PREFIX', default='')
}
