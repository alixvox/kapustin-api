from flask import Blueprint, request, jsonify
from api.models import Works
from sqlalchemy import or_

filter_blueprint = Blueprint('filter', __name__)

# Search Works by Title
@filter_blueprint.route('/opus/search/title', methods=['GET'])
def search_by_title():
    title = request.args.get('q')
    works = Works.query.filter(Works.title.ilike(f"%{title}%")).all()
    return jsonify([work.json() for work in works]), 200

# Search Works by Section Name
@filter_blueprint.route('/opus/search/section', methods=['GET'])
def search_by_section():
    section_keyword = request.args.get('name')
    works = Works.query.filter(Works.section_names.ilike(f"%{section_keyword}%")).all()
    return jsonify([work.json() for work in works]), 200

# Filter Works by Type
@filter_blueprint.route('/opus/filter', methods=['GET'])
def filter_by_type():
    type_ = request.args.get('type')
    works = Works.query.filter_by(type=type_).all()
    return jsonify([work.json() for work in works]), 200

# Filter Works by Year Range
@filter_blueprint.route('/opus/year', methods=['GET'])
def filter_by_year_range():
    start_year = int(request.args.get('start'))
    end_year = int(request.args.get('end'))
    works = Works.query.filter(Works.year.between(start_year, end_year)).all()
    return jsonify([work.json() for work in works]), 200

# Filter Works by Instrument
@filter_blueprint.route('/opus/filter/instruments', methods=['GET'])
def filter_by_instrument():
    instruments = request.args.get('instruments').split(',')
    conditions = [Works.instruments.ilike(f"%{instrument}%") for instrument in instruments]
    works = Works.query.filter(or_(*conditions)).all()
    return jsonify([work.json() for work in works]), 200

# Filter Works by Number of Instruments
@filter_blueprint.route('/opus/filter/num-instruments', methods=['GET'])
def filter_by_num_instruments():
    num_instruments = int(request.args.get('num-instruments'))
    works = Works.query.filter_by(num_instruments=num_instruments).all()
    return jsonify([work.json() for work in works]), 200

# Filter Works by Maximum Length
@filter_blueprint.route('/opus/filter/length-max', methods=['GET'])
def filter_by_max_length():
    max_length = request.args.get('length-max')
    works = Works.query.filter(Works.length <= max_length).all()
    return jsonify([work.json() for work in works]), 200

# Filter Works by Minimum Length
@filter_blueprint.route('/opus/filter/length-min', methods=['GET'])
def filter_by_min_length():
    min_length = request.args.get('length-min')
    works = Works.query.filter(Works.length >= min_length).all()
    return jsonify([work.json() for work in works]), 200

# Filter Works by Number of Sections
@filter_blueprint.route('/opus/filter/num-sections', methods=['GET'])
def filter_by_num_sections():
    num_sections = int(request.args.get('num-sections'))
    works = Works.query.filter_by(num_sections=num_sections).all()
    return jsonify([work.json() for work in works]), 200
