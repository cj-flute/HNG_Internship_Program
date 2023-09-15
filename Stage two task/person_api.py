#!/urs/bin/python3
"""
    A REST API for person that can CREAT, READ, UPDATE, and DELETE
    From the API
"""

import json
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

persons = [
    {'id': 1, 'name': 'Chijioke Michael', 'gender': 'male',
        'height': '6', 'complexion': 'fair'},
    {'id': 2, 'name': 'Maxwell Chidera', 'gender': 'male',
        'height': '6.2', 'complexion': 'dark'},
    {'id': 3, 'name': 'Debora Nwafor', 'gender': 'female',
        'height': '5.8', 'complexion': 'fair'},
    {'id': 4, 'name': 'Hope Ogene', 'gender': 'female',
        'height': '4.8', 'complexion': 'dark'},
    {'id': 5, 'name': 'Pual Chibueze', 'gender': 'male',
        'height': '5.10', 'complexion': 'fair'},
]


# ID validation
def id_validation(person_id):
    if isinstance(person_id, str):
        return {'data': 'Invalid ID', 'isValid': False}

    for person in persons:
        if person['id'] == person_id:
            return {'data': person, 'isValid': True}

    return {'data': 'Person not found', 'isValid': False}

# Gender validation


def gender_validation(new_person):
    if (new_person['gender'] == 'female' or
            new_person['gender'] == 'male'):
        return {'isValid': True}
    else:
        return {'data': 'Gender must be male or female',
                'isValid': False}

# getting all the persons


@app.route('/api', methods=['GET'])
def person_record():
    return jsonify(persons)


# get a person (Read)
@app.route('/api/<person_id>', methods=['GET'])
@app.route('/api/<int:person_id>', methods=['GET'])
def get_person(person_id):
    id_validation_response = id_validation(person_id)
    return id_validation_response['data']

# creating a person (create)


@app.route('/api', methods=['POST'])
def create_person():
    new_person = {
        'id': len(persons) + 1,
        'name': request.json['name'],
        'gender': request.json['gender'],
        'height': request.json['height'],
        'complexion': request.json['complexion']
    }
    gender_validation_response = gender_validation(new_person)

    if gender_validation_response['isValid']:
        persons.append(new_person)
    else:
        return gender_validation_response['data']
    return new_person

# updating a person (Update)


@app.route('/api/<person_id>', methods=['PUT'])
@app.route('/api/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    person_update = {
        'name': request.json['name'],
        'gender': request.json['gender'],
        'height': request.json['height'],
        'complexion': request.json['complexion']
    }

    id_validation_response = id_validation(person_id)
    gender_validation_response = gender_validation(person_update)

    if id_validation_response['isValid']:
        if gender_validation_response['isValid']:
            for person in persons:
                if person['id'] == person_id:
                    person['name'] = person_update['name']
                    person['gender'] = person_update['gender']
                    person['height'] = person_update['height']
                    person['complexion'] = person_update['complexion']
                    return person
            return id_validation_response['data']
        else:
            return gender_validation_response['data']
    else:
        return id_validation_response['data']

# Delete a person (Delete)


@app.route('/api/<person_id>', methods=['DELETE'])
@app.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    id_validation_response = id_validation(person_id)
    if not id_validation_response['isValid']:
        return id_validation_response['data']
    else:
        person = id_validation_response['data']
        persons.remove(person)
        return 'Person Deleted'


if __name__ == '__main__':
    app.run()
