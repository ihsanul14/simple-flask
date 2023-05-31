from .response import resp, except_response, list_project
from repository import repository


def get_data():
    result = {}
    result['data'] = []
    try:
        result['code'] = 200
        result['message'] = "success retrieve data"
        project = repository.get_data()
        result = list_project(result, project)
    except Exception as err:
        result = except_response(result, err)
        result.pop('data')
    print(result)
    return result


def get_data_by_id(data):
    result = {}
    result['data'] = []
    result['code'] = 200
    result['message'] = "success retrieve projects data with id = {}".format(
        data)
    project = repository.get_data_by_id(data)
    result = list_project(result, project)
    result['data'] = result['data']
    return result


def add_data(data):
    print()
    result = {}
    result['data'] = repository.add_data(data)
    result['code'] = 200
    result['message'] = "success insert data"
    result = resp(result)
    return result


def update_data(data):
    result = {}
    result['data'] = repository.update_data(data)
    result['code'] = 200
    result['message'] = "success update data with id = {}".format(
        data['project_id'])
    result = resp(result)
    return result


def delete_data(data):
    result = {}
    result['data'] = repository.delete_data(data)
    result['code'] = 200
    result['message'] = "success delete data with id = {}".format(data)
    result = resp(result)
    return result
