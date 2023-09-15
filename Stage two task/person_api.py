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


# validation id
def id_validation(person_id):
    if isinstance(person_id, str):
        return jsonify({'error': 'Invalid ID'})
    return jsonify({'error': 'Person not found'})


# getting all the persons


@app.route('/api', methods=['GET'])
def person_record():
    return jsonify(persons)


# get a person (Read)
@app.route('/api/<person_id>', methods=['GET'])
@app.route('/api/<int:person_id>', methods=['GET'])
def get_person(person_id):
    for person in persons:
        if person['id'] == person_id:
            return person
    return id_validation(person_id)

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
    for new_p in new_person:
        if (new_p['gender'] == 'male' or
                new_p['gender'] == 'female'):
            persons.append(new_person)
            return new_person
        else:
            return {'error': 'Gender must be male or female'}

    # persons.append(new_person)
    # return new_person

# updating a person (Update)


@app.route('/api/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    for person in persons:
        if person['id'] == person_id:
            person['name'] = request.json['name']
            person['gender'] = request.json['gender']
            person['height'] = request.json['height']
            person['complexion'] = request.json['complexion']
            return person
    return {'error': 'Person not found'}

# Delete a person (Delete)


@app.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    for person in persons:
        if person['id'] == person_id:
            persons.remove(person)
            return {'Person': 'Person Deleted'}
    return {'error': 'Person not found'}


if __name__ == '__main__':
    app.run()
