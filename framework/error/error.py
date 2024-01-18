from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from flask import Response
import json
from framework.logger import Logger


class Error:
    log = Logger()

    def error(self, e: Exception, id=""):
        err_response = {
            'code': 500,
            'message': str(e)
        }
        if isinstance(e, NoResultFound):
            err_response['code'] = 404
            err_response['message'] = f"No data found with id {id}"
        elif isinstance(e, IntegrityError):
            err_response['code'] = 400

        self.log.Error(err_response['message'])
        return Response(json.dumps(err_response), status=err_response['code'], content_type='application/json')
