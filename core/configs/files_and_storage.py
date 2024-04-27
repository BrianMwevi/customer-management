from core.env import env

MEDIA_URL = env.get_value('MEDIA_URL')
STATIC_URL = env.get_value('STATIC_URL')
STATIC_ROOT = env.get_value('STATIC_ROOT')