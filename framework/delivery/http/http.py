import usecase
from flask import Response, abort, request
import json
from sqlalchemy.orm.exc import NoResultFound
from framework.validator.validator import Validate
from models.models import UpdateProjectRequest

router_group = "/api/v1/project"


def delivery_http(app):
    @app.get(router_group)
    def list_project():
        try:
            response = usecase.project_handler.get_data()
            return Response(json.dumps(response), status=response['code'], content_type='application/json')
        except Exception as e:
            err_response = {
                'code': 500,
                'message': str(e)
            }
            return Response(json.dumps(err_response), status=err_response['code'], content_type='application/json')

    @app.get(f'{router_group}/<string:id>')
    def list_project_by_id(id):
        response = usecase.project_handler.get_data_by_id(id)
        return Response(json.dumps(response), status=response['code'], content_type='application/json')

    @app.post(f'{router_group}')
    def create_project():
        if not request.json:
            abort(400)
        response = usecase.project_handler.add_data(request.json)
        return Response(json.dumps(response), status=response['code'], content_type='application/json')

    @app.put(f'{router_group}/<string:id>')
    def update_project(id):
        try:
            request.json['project_id'] = id
            if Validate(request.json, UpdateProjectRequest):
                return Response(json.dumps({'message': str(Validate(request.json, UpdateProjectRequest))}), status=400, content_type='application/json')
            response = usecase.project_handler.update_data(request.json)
            return Response(json.dumps(response), status=response['code'], content_type='application/json')
        except NoResultFound:
            err_response = {
                'code': 404,
                'message': f"No data found with id {id}"
            }
            return Response(json.dumps(err_response), status=err_response['code'], content_type='application/json')
        except Exception as e:
            err_response = {
                'code': 500,
                'message': str(e)
            }
            return Response(json.dumps(err_response), status=err_response['code'], content_type='application/json')

    @app.delete(f'{router_group}/<string:id>')
    def delete_project(id):
        response = usecase.project_handler.delete_data(id)
        return Response(json.dumps(response), status=response['code'], content_type='application/json')
