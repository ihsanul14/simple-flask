from models.models import Project
from typing import List


def resp(data):
    res = {}
    res['code'] = data['code']
    if data["code"] == 200:
        res["success"] = True
    else:
        data["success"] = False
    res['data'] = data['data']
    return res


def list_project(data, projects: List[Project]):
    for project in projects:
        result = {}
        result['project_id'] = project.project_id
        result['project_name'] = project.project_name
        data['data'].append(result)
    return data


def refactored_project_by_id(project: Project):
    res = {
        'project_id': project.project_id,
        'project_name': project.project_name
    }
    return res
