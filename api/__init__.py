from flask_restful import Api
from app import flaskAppInstance
from .task import Task
from .taskbyid import TaskById

restserver = Api(flaskAppInstance)

restserver.add_resource(Task, "/api/v1.0/task")
restserver.add_resource(TaskById, "/api/v1.0/task/id/<string:task_id>")




