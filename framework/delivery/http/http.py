from usecase import Usecase
from flask import Response, abort, request, Flask
import json
from framework.validator.validator import Validate
from models.models import UpdateProjectRequest
from framework.error.error import Error

router_group = "/api/v1/project"


class Delivery:
    error = Error()
    usecase = Usecase

    def __init__(self, app: Flask):
        self.app = app

    def delivery_http(self):
        @self.app.before_request
        def init_usecase():
            self.usecase = Usecase()

        @self.app.get(router_group)
        def list_project():
            try:
                response = self.usecase.get_data()
                return Response(json.dumps(response), status=response['code'], content_type='application/json')
            except Exception as e:
                return self.error.error(e)

        @self.app.get(f'{router_group}/<string:id>')
        def list_project_by_id(id):
            try:
                response = self.usecase.get_data_by_id(id)
                return Response(json.dumps(response), status=response['code'], content_type='application/json')
            except Exception as e:
                return self.error.error(e, id)

        @self.app.post(f'{router_group}')
        def create_project():
            try:
                if not request.json:
                    abort(400)
                response = self.usecase.add_data(request.json)
                return Response(json.dumps(response), status=response['code'], content_type='application/json')
            except Exception as e:
                return self.error.error(e)

        @self.app.put(f'{router_group}/<string:id>')
        def update_project(id):
            try:
                request.json['project_id'] = id
                if Validate(request.json, UpdateProjectRequest):
                    return Response(json.dumps({'message': str(Validate(request.json, UpdateProjectRequest))}), status=400, content_type='application/json')
                response = self.usecase.project_handler.update_data(
                    request.json)
                return Response(json.dumps(response), status=response['code'], content_type='application/json')
            except Exception as e:
                return self.error.error(e, id)

        @self.app.delete(f'{router_group}/<string:id>')
        def delete_project(id):
            try:
                response = self.usecase.delete_data(id)
                return Response(json.dumps(response), status=response['code'], content_type='application/json')
            except Exception as e:
                return self.error.error(e, id)
