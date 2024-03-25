from .response import list_project, refactored_project_by_id
from repository import Repository


class Usecase:
    repository = Repository()

    def get_data(self):
        result = {}
        result['data'] = []
        result['code'] = 200
        result['message'] = "success retrieve data"
        project = self.repository.get_data()
        result = list_project(result, project)
        return result

    def get_data_by_id(self, data):
        result = {}
        result['data'] = []
        result['code'] = 200
        result['message'] = "success retrieve projects data with id = {}".format(
            data)
        project = self.repository.get_data_by_id(data)
        result['data'] = refactored_project_by_id(project)
        return result

    def add_data(self, data):
        result = {}
        result['data'] = self.repository.add_data(data)
        result['code'] = 200
        result['message'] = "success insert data"
        return result

    def update_data(self, data):
        result = {}
        result['data'] = self.repository.update_data(data)
        result['code'] = 200
        result['message'] = "success update data with id = {}".format(
            data['project_id'])
        return result

    def delete_data(self, data):
        result = {}
        result['data'] = self.repository.delete_data(data)
        result['code'] = 200
        result['message'] = "success delete data with id = {}".format(data)
        return result
