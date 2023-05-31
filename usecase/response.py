import json


def resp(data):
    res = {}
    res['code'] = data['code']
    if data["code"] == 200:
        res["success"] = True
    else:
        data["success"] = False
    res['data'] = data['data']
    return res


def except_response(data, err):
    print(err)
    data['code'] = 500
    data['message'] = err.args[0]
    return data


def list_project(data, projects):
    for project in projects:
        result = {}
        result['project_id'] = project.project_id
        result['project_name'] = project.project_name
        data['data'].append(result)
    return data

