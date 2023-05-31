from framework.database.database import connect_pg
from sqlalchemy.orm import sessionmaker
from models.models import Project

conn = connect_pg()


def get_data():
    Session = sessionmaker(bind=conn)
    session = Session()
    result = {}
    result = session.query(Project).all()
    session.close()
    return result


def get_data_by_id(data):
    result = {}
    Session = sessionmaker(bind=conn)
    session = Session()
    result = session.query(Project).filter(Project.project_id == data).one()
    session.close()
    return result


def add_data(data):
    Session = sessionmaker(bind=conn)
    session = Session()
    query = Project(project_id=data['project_id'],
                    project_name=data['project_name'])
    session.add(query)
    session.commit()
    session.close()
    return data


def update_data(data):
    Session = sessionmaker(bind=conn)
    session = Session()
    result = session.query(Project).filter(
        Project.project_id == data['project_id']).one()
    result.project_name = data['project_name']
    session.commit()
    session.close()
    return data


def delete_data(data):
    Session = sessionmaker(bind=conn)
    session = Session()
    query = session.query(Project).filter(Project.project_id == data).one()
    session.delete(query)
    session.commit()
    session.close()
    return data
