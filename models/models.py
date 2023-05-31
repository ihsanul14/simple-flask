from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr

Base = declarative_base()


class Project(Base):
    __tablename__ = 'project'

    project_id = Column(String, primary_key=True)
    project_name = Column(String(50))


class UpdateProjectRequest(BaseModel):
    project_id: constr(strict=True, min_length=1)
    project_name: constr(strict=True, min_length=1)
