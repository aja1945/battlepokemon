from flask import Blueprint

pokemon_bp = Blueprint('pokemon', __name__, template_folder='templates')

from . import routes
