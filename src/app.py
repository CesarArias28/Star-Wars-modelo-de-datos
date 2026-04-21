"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Favorite
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity
)

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/login', methods=['POST'])

def login():

 body = request.get_json()
 
   



@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):

    single_planet = Planet.query.get(planet_id)

    if single_planet is None:

        return jsonify({"msg": "Planet not found"}), 404
    
    response_body = single_planet.serialize()
    return jsonify(response_body), 200



@app.route('/users/<int:user_id>/favorites', methods=['GET'])

def get_all_favorites(user_id):

    all_favorites = Favorite.query.filter_by(user_id=user_id).all()

    all_favorites = [a.serialize() for a in all_favorites]

    return jsonify(all_favorites), 200 

@app.route('/people', methods=['GET'])

def get_all_characters():

    all_characters = Character.query.all()

    character_list = [c.serialize() for c in all_characters]

    return jsonify(character_list), 200 

@app.route('/planets/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):

    single_planet = Planet.query.get(planet_id)

    if single_planet is None:
        return jsonify({"msg": "Planet not found"}), 404

    db.session.delete(single_planet)
    db.session.commit()

    return jsonify({"msg": "Planet deleted successfully"}), 200




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
