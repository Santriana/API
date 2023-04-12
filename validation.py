from flask import abort, make_response, jsonify, request
from marshmallow import ValidationError

def validate_schema(schema, data):
    try:
        return schema.load(data)
    except ValidationError as e:
        abort(make_response(jsonify(Status="Failed", Message=str(e.messages)), 400))