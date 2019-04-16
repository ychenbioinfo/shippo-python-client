import logging
import sys

logger = logging.getLogger('shippo')

__all__ = ['StringIO', 'parse_qsl', 'json', 'utf8']

try:
    # When cStringIO is available
    import io as StringIO
except ImportError:
    import io

try:
    from urllib.parse import parse_qsl
except ImportError:
    # Python < 2.6
    from cgi import parse_qsl

try:
    import json
except ImportError:
    json = None

if not (json and hasattr(json, 'loads')):
    try:
        import simplejson as json
    except ImportError:
        if not json:
            raise ImportError(
                "Shippo requires a JSON library, such as simplejson. "
                "HINT: Try installing the "
                "python simplejson library via 'pip install simplejson' or "
                "'easy_install simplejson', or contact support@goshippo.com "
                "with questions.")
        else:
            raise ImportError(
                "Shippo requires a JSON library with the same interface as "
                "the Python 2.6 'json' library.  You appear to have a 'json' "
                "library with a different interface.  Please install "
                "the simplejson library.  HINT: Try installing the "
                "python simplejson library via 'pip install simplejson' "
                "or 'easy_install simplejson', or contact support@goshippo.com"
                "with questions.")


def utf8(value):
    if isinstance(value, str) and sys.version_info < (3, 0):
        return value.encode('utf-8')
    else:
        return value
