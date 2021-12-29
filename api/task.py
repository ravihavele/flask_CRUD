from flask_restful import Resource
import logging as logger

class Task(Resource):

    def get(self):
        logger.debug("inside get method")
        return {"message": "Inside Get Method"}, 200

    def post(self):
        logger.debug("inside post method")
        return {"message": "Inside Post Method"}, 200

    def put(self):
        logger.debug("inside put method")
        return {"message": "Inside Put Method"}, 200

    def delete(self):
        logger.debug("inside delete method")
        return {"message": "Inside Delete Method"}, 200