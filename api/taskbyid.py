from flask_restful import Resource
import logging as logger

class TaskById(Resource):

    def get(self, task_id):
        logger.debug("inside get method of task by id")
        return {"message": f"Inside Get Method of task id and Task_ID={task_id}"}, 200

    def post(self, task_id):
        logger.debug("inside post method of task by id")
        return {"message": f"Inside Post Method of task id and Task_ID={task_id}"}, 200

    def put(self, task_id):
        logger.debug("inside put method of task by id")
        return {"message": f"Inside Put Method of task id and Task_ID={task_id}"}, 200

    def delete(self, task_id):
        logger.debug("inside delete method of task by id")
        return {"message": f"Inside Delete Method of task id and Task_ID={task_id}"}, 200