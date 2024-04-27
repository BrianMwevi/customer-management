import sentry_sdk
from core.env import env

sentry_sdk.init(
    # dsn=os.environ.get('SENTRY_DSN'),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    environment=env.get_value('ENV'),
    traces_sample_rate=1.0,
)
