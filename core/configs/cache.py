from core.env import env

CACHE_ENABLED = env.get_value('CACHE_ENABLED', cast=bool, default=False)

if CACHE_ENABLED:
    cache_url = env.get_value('CACHE_URL')

    if cache_url:
        CACHES = {
            "default": {
                "BACKEND": "django_redis.cache.RedisCache",
                "LOCATION": cache_url,
                "OPTIONS": {
                    "CLIENT_CLASS": "django_redis.client.DefaultClient",
                }
            }
        }
    else:
        raise ValueError("CACHE_URL is not provided in the environment variables.")
