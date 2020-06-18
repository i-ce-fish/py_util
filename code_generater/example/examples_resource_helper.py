from flask_restful import fields, reqparse, inputs
from models.category import Category

paginate_fields = {
    'total': fields.Integer,
    'pageSize': fields.Integer,
    'current': fields.Integer
}

category_fields = {
    'id': fields.Integer,
{{output_fields}}
    'created_at': fields.String
}

category_list_fields = {
    'pagination': fields.Nested(paginate_fields),
    'list': fields.List(fields.Nested(category_fields))
}

sortable_fields = ['id',{{sortable_fields}}]

category_post_parser = reqparse.RequestParser()
{{post_parser_fields}}

category_update_parser = reqparse.RequestParser()
{{update_parser_fields}}


category_query_parser = reqparse.RequestParser()
{{query_parser_fields}}


category_query_parser.add_argument('orderby', type=str, default='id')
category_query_parser.add_argument('desc', type=int, default=0)
category_query_parser.add_argument('page', type=int)
category_query_parser.add_argument('pagesize', type=int)

def make_conditions(conditions, args):
{{conditisons}}
    return conditions

def update_all_fields(args, o):
{{update_all_fields_method}}
    return o
