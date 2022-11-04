# blueprints/basic_endpoints/__ini__.py

from flask import Blueprint,request


event_api = Blueprint('event',__name__)


@event_api.route('/', methods=['GET', 'POST'])
def entities():
    if request.method == "GET":
        return {
            'message': 'This endpoint should return a list of entities',
            'method': request.method
        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an event',
            'method': request.method,
            'body': request.json
        }

@event_api.route('/<int:event_id>', methods=['GET', 'PUT', 'DELETE'])
def event(event_id):
    if request.method == "GET":
        return {
            'id': event_id,
            'message': 'This endpoint should return the event {} details'.format(event_id),
            'method': request.method
        }
    if request.method == "PUT":
        return {
            'id': event_id,
            'message': 'This endpoint should update the event {}'.format(event_id),
            'method': request.method,
            'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': event_id,
            'message': 'This endpoint should delete the event {}'.format(event_id),
            'method': request.method
        }

