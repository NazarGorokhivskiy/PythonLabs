from flask import Flask
from flask_restful import Resource, reqparse, fields, marshal, abort, Api

app = Flask(__name__, static_url_path="")
api = Api(app)

toys = [
    {
        'Id': 0,
        'age': 'Default',
        'size': 'Default',
        'toy_type': 'Default'
    }
]

toys_fields = {
    'id': fields.Integer,
    'age': fields.String,
    'size': fields.String,
    'toy_type': fields.String,
}


class Toy(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, required=True, help='No Id provided', location='json')
        self.reqparse.add_argument('age', type=str, default="", location='json')
        self.reqparse.add_argument('size', type=str, default="", location='json')
        self.reqparse.add_argument('toy_type', type=str, default="", location='json')
        super(Toy, self).__init__()  # super().__init__() / Good.__init__(self)

    def put(self):
        args = self.reqparse.parse_args()
        toy = {
            'Id': toys[-1]['Id'] + 1,
            'id': args['id'],
            'age': args['age'],
            'size': args['size'],
            'toy_type': args['toy_type']
        }
        toys.append(toy)
        return{'Toy': marshal(toy, toys_fields)}, 201

    def post(self):
        args = self.reqparse.parse_args()
        toy = [toy for toy in toys if toy.get('id') == args['id']]
        if len(toys) == 0:
            abort(404)
        toy = toy[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                toy[k] = v

    def get(self, id):
        toy = [toy for toy in toys if toy.get('id') == id]
        if len(toy) == 0:
            abort(404)
        return {'Toy': marshal(toy[0], toys_fields)}

    def delete(self, id):
        toy = [toy for toy in toys if toy.get('id') == id]
        if len(toy) == 0:
            abort(404)
        toys.remove(toy[0])
        return {'result': True}


api.add_resource(Toy, '/toys', endpoint='toys')
api.add_resource(Toy, '/toys/<int:id>', endpoint='toy')


if __name__ == '__main__':
    app.run(debug=True)

