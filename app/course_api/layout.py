# blueprints/basic_endpoints/__ini__.py

from flask import Blueprint,request,jsonify
from app.models.layout_model import LayoutModel,LayoutSchema
from app import db

layout_api = Blueprint('layout',__name__)

layout_schema  = LayoutSchema()
layouts_schema = LayoutSchema(many=True)

@layout_api.route('/', methods=['GET', 'POST'])
def entities():
    if request.method == "GET":
        print ('all_layouts')
        all_layouts = LayoutModel.query.all()
        return jsonify (layouts_schema.dump(all_layouts))
        #return {
        #    'message': 'This endpoint should return a list of entities',
        #    'method': request.method
        #}
    if request.method == "POST":


        print ('adding layout')
  
        l = LayoutModel(name='ppp',description='sss',parameters='aaa')
        db.session.add(l)
        db.session.commit()
        return layout_schema.jsonify(l)

       

@layout_api.route('/<int:layout_id>', methods=['GET', 'PUT', 'DELETE'])
def entity(layout_id):
    if request.method == "GET":
        return {
            'id': layout_id,
            'message': 'This endpoint should return the entity {} details'.format(layout_id),
            'method': request.method
        }
    if request.method == "PUT":
        return {
            'id': layout_id,
            'message': 'This endpoint should update the entity {}'.format(layout_id),
            'method': request.method,
            'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': layout_id,
            'message': 'This endpoint should delete the entity {}'.format(layout_id),
            'method': request.method
        }

