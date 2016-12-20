import logging

from flask import request
from flask_restplus import Resource
from rest_api.api.blog.business import create_category, delete_category, update_category
from rest_api.api.blog.serializers import category, category_with_posts
from rest_api.api.restplus import api
from rest_api.database.models import NGO,NGO_Branch

log = logging.getLogger(__name__)

ns = api.namespace('beyondGiving/ngo', description='Operations related to ngo Creation')


@ns.route('/')
class NGOCollection(Resource):

    @api.marshal_list_with(category)
    def get(self):
    	ngos = NGO.query.all()
    	return ngos

    @api.response(201, 'Category successfully created.')
    @api.expect(category)
    def post(self):
        """
        Creates a new NGO Instance
        """
        data = request.json
        create_category(data)
        return None, 201


