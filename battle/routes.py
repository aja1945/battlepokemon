from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import battle_bp
from ..models import Pokemon, User
from .. import db

@battle_bp.route('/attack/<int:opponent_id>', methods=['GET', 'POST'])
@login_required
def attack(opponent_id):
    opponent = User.query.get_or_404(opponent_id)

    if request.method == 'POST':
        flash('Battle results will be displayed here.', 'info')

    return render_template('attack.html', user=current_user, opponent=opponent)
