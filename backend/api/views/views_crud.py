from flask import Blueprint, request, jsonify
from api.models import db, Works

crud_blueprint = Blueprint('crud', __name__)

# Get All Works
@crud_blueprint.route('/opus', methods=['GET'])
def get_all_works():
    works = Works.query.all()
    return jsonify([work.json() for work in works]), 200

# Add New Work
@crud_blueprint.route('/opus', methods=['POST'])
def add_new_work():
    data = request.get_json()
    new_work = Works(
        opus_id=data['opus_id'],
        title=data['title'],
        type=data['type'],
        year=data['year'],
        recording_exists=data['recording_exists'],
        length=data['length'],
        youtube_link=data['youtube_link'],
        num_instruments=data['num_instruments'],
        instruments=data['instruments'],
        num_sections=data['num_sections'],
        section_names=data['section_names'],
        referenced_work=data['referenced_work']
    )
    db.session.add(new_work)
    db.session.commit()
    return jsonify(new_work.json()), 201

# Update Work
@crud_blueprint.route('/opus/<int:opus_id>', methods=['PUT'])
def update_work(opus_id):
    work = Works.query.get(opus_id)
    if not work:
        return jsonify({'message': 'Work not found'}), 404

    data = request.get_json()
    for key, value in data.items():
        setattr(work, key, value)

    db.session.commit()
    return jsonify(work.json()), 200

# Delete Work
@crud_blueprint.route('/opus/<int:opus_id>', methods=['DELETE'])
def delete_work(opus_id):
    work = Works.query.get(opus_id)
    if not work:
        return jsonify({'message': 'Work not found'}), 404

    db.session.delete(work)
    db.session.commit()
    return jsonify({'message': 'Work deleted successfully'}), 200
