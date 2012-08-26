
DEBUG = False
WERKZEUG_OPTS = {
    'host': '127.0.0.1',
    'port': 5000,
}

ENGINE = None

try:
    from local_settings import *
except ImportError:
    pass
