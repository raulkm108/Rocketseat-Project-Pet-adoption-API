from flask import Blueprint, jsonify
from src.main.composer.pet_lister_composer import pet_lister_composer
from src.views.http_types.http_request import HttpRequest

pet_route_bp = Blueprint("pet_routes", __name__)

@pet_route_bp.route("/pet", methods=["GET"])
def list_pets():
    http_request = HttpRequest()
    view = pet_lister_composer()

    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code