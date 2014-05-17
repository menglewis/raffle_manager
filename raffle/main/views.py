# -*- coding: utf-8 -*-
import random
from flask import render_template, request, flash, redirect, url_for
from flask.ext.login import login_required
from raffle import db
from . import main
from .models import Raffle, RaffleEntry
from .forms import RaffleForm, RaffleEntryForm, flash_form_errors

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = RaffleForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            raffle = Raffle(name=form.name.data)
            db.session.add(raffle)
            db.session.commit()
            flash("Raffle added", "success")
            return redirect(url_for('main.index'))
        else:
            flash_form_errors(form)
    raffles = Raffle.query.all()
    return render_template('main/index.html', raffles=raffles, form=form)

@main.route('/<int:id>', methods=['GET', 'POST'])
@login_required
def raffle(id):
    
    form = RaffleEntryForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            raffle_entry = RaffleEntry(name=form.name.data, quantity=form.quantity.data, raffle_id=id)
            db.session.add(raffle_entry)
            db.session.commit()
            flash("Entry Added", "success")
            return redirect(url_for('main.raffle', id=id))
    raffle = Raffle.query.get(id)
    return render_template('main/raffle.html', raffle=raffle, form=form)

@main.route('/<int:id>/delete', methods=['GET'])
@login_required
def raffle_delete(id):
    raffle = Raffle.query.get(id)
    db.session.delete(raffle)
    db.session.commit()
    flash("Raffle deleted", "success")
    return redirect(url_for('main.index'))

@main.route('/<int:id>/result', methods=['GET'])
@login_required
def raffle_winner(id):
    raffle = Raffle.query.get(id)

    return render_template('main/result.html', raffle=raffle)
