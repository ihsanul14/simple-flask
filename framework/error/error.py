from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from flask import Response
import json


def error(e: Exception, id=""):
    err_response = {
        'code': 500,
        'message': str(e.args)
    }
    if isinstance(e, NoResultFound):
        err_response['code'] = 404
        err_response['message'] = f"No data found with id {id}"
    elif isinstance(e, IntegrityError):
        err_response['code'] = 400

    return Response(json.dumps(err_response), status=err_response['code'], content_type='application/json')
