from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from . import auth_bp
from .models import User, Pokemon
from .forms import RegistrationForm, LoginForm

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home')) 
        else:
            flash('Login unsuccessful. Please check email and password.', 'error')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@auth_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import pokemon_bp
from ..models import Pokemon, User
from .. import db

@pokemon_bp.route('/pokemon/add/<int:pokemon_id>')
@login_required
def add_pokemon(pokemon_id):
    if len(current_user.pokemon) < 5:
        pokemon_data = get_pokemon_data(pokemon_id)

        if not pokemon_data:
            flash('Pokemon not found!', 'error')
        else:
            save_pokemon_to_db(pokemon_data)
            flash(f'You added {pokemon_data["name"]} to your collection!', 'success')
    else:
        flash('You have reached the maximum number of Pokémon in your collection.', 'error')

    return redirect(url_for('home'))

@pokemon_bp.route('/pokemon/remove/<int:pokemon_id>')
@login_required
def remove_pokemon(pokemon_id):
    pokemon = Pokemon.query.get_or_404(pokemon_id)

    if current_user == pokemon.user:
        db.session.delete(pokemon)
        db.session.commit()
        flash(f'You removed {pokemon.name} from your collection.', 'success')
    else:
        flash('You do not own this Pokémon.', 'error')

    return redirect(url_for('home'))

from your_flask_app.pokemon.routes import pokemon_bp

