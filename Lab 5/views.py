from app import app
from flask import request
from app import db
from Toy import Toy

@app.route('/')
def index():
    firstmember = Toy.query.first()
    return '<h1> Here you can find toys list! </h1>'

@app.route('/toys')
def view():
    toys = Toy.query.first()
    if toys is not None:
        return str('First member name \n' + toys.__str__())
    else:
        return "Toy with this id does not exist"

@app.route('/toys/<id>')
def get_toys(id):
    toys = Toy.query.get(id)
    if toys is not None:
        return toys.__str__()
    else:
        return "Toy with this id does not exist"

@app.route('/toys', methods=['POST'])
def add_toys():
    toy_id = request.json['id']
    toy_size = request.json['size']
    toy_age = request.json['age']

    new_toys = Toy()
    new_toys.toy_id = toy_id
    new_toys.toy_size = toy_size
    new_toys.toy_age = toy_age

    db.session.add(new_toys)
    db.session.commit()

    return str(new_toys.__str__())

@app.route('/toys/<id>', methods=['PUT'])
def toys_update(id):
    toy_size = request.json['size']
    toy_age = request.json['age']

    new_toys = Toy.query.get(id)
    new_toys.toy_id = id
    new_toys.toy_size = toy_size
    new_toys.toy_age = toy_age

    db.session.commit()

    return new_toys.__str__()

@app.route('/toys/<id>', methods=['DELETE'])
def toys_delete(id):
    toys = Toy.query.get(id)
    db.session.delete(toys)
    db.session.commit()

    return str("Deleting succssesful")