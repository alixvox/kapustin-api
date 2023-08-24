from flask import Blueprint, jsonify
from api.models import Works

get_blueprint = Blueprint('get', __name__)

# Get Work by Opus Number
@get_blueprint.route('/opus/<int:opus_id>', methods=['GET'])
def get_work_by_opus(opus_id):
    work = Works.query.get(opus_id)
    if not work:
        return jsonify({'message': 'Work not found'}), 404
    return jsonify(work.json()), 200

# Get Works with No Recording
@get_blueprint.route('/opus/no-recording', methods=['GET'])
def get_no_recording():
    works = Works.query.filter_by(recording_exists=False).all()
    return jsonify([work.json() for work in works]), 200

# Get Works by Year
@get_blueprint.route('/opus/year/<int:year>', methods=['GET'])
def get_works_by_year(year):
    works = Works.query.filter_by(year=year).all()
    return jsonify([work.json() for work in works]), 200

# Get Works With 1 Section Only
@get_blueprint.route('/opus/one-section', methods=['GET'])
def get_one_section():
    works = Works.query.filter_by(num_sections=1).all()
    return jsonify([work.json() for work in works]), 200

# Get Works Referencing Other Artists
@get_blueprint.route('/opus/referenced', methods=['GET'])
def get_referenced():
    works = Works.query.filter(Works.referenced_work != None, Works.referenced_work != '').all()
    return jsonify([work.json() for work in works]), 200
