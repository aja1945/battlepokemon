from flask_login import UserMixin
from your_flask_app import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    pokemon = db.relationship('Pokemon', backref='user', lazy=True)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"User('{self.first_name}', '{self.email}')"

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    hp = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    ability = db.Column(db.String(50))
    image_url = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Pokemon('{self.name}', '{self.user_id}')"

@auth_bp.route('/')
def home():
    return redirect(url_for('pokemon.collection'))

    app.register_blueprint(auth_bp)
app.register_blueprint(pokemon_bp)
app.register_blueprint(battle_bp)



