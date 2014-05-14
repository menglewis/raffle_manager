# -*- coding: utf-8 -*-
from flask import flash
from flask_wtf import Form
from wtforms import TextField, IntegerField
from wtforms.validators import DataRequired

class RaffleForm(Form):
    name = TextField('Name', validators=[DataRequired()])

class RaffleEntryForm(Form):
    name = TextField('Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])

def flash_form_errors(form, category="warning"):
    '''Flash all errors for a form.'''
    for field, errors in form.errors.items():
        for error in errors:
            flash("{0} - {1}"
                    .format(getattr(form, field).label.text, error), category)
