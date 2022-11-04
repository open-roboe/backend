from flask import Blueprint,request

from app.course_api.event import event_api
from app.course_api.entity import entity_api
from app.course_api.layout import layout_api

course_api = Blueprint('api',__name__)

course_api.register_blueprint (event_api,url_prefix='/event')
course_api.register_blueprint (entity_api,url_prefix='/entity')
course_api.register_blueprint (layout_api,url_prefix='/layout')