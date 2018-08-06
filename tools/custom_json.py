from json import JSONEncoder
from enum import Enum
import flask


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return str(obj.name)
        return super(CustomJSONEncoder, self).default(obj)


def jsonify(obj):
    try:
        return flask.jsonify(obj)
    except TypeError as error:
        if hasattr(obj, "__dict__"):
            return flask.jsonify(obj.__dict__)
        raise
