__author__ = 'hkar'

import jsonschema


class Request:
    INPUT_JSONSCHEMA = {
        "type": "object",
        "properties": {
            "public_token": {"type": "string"},
            "timestamp": {"type": "number"},
            "pipe": {"type": "string"}
        }
    }

    def __init__(self, redis):
        self.redis = redis

    def new(self, request_data):
        try:
            jsonschema.validate(request_data, self.INPUT_JSONSCHEMA)
            return True
        except jsonschema.ValidationError:
            return False