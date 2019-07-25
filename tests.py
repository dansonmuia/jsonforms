import json
from unittest import TestCase

import flask
from wtforms import fields as f, validators as v

from .form import JsonForm

app = flask.Flask(__name__)


class NameForm(JsonForm):
    name = f.StringField('Name', validators=[v.DataRequired()])
    email = f.StringField('Email', validators=[v.DataRequired(), v.Email()])


valid_data = {'name': 'John Smith',
              'email': 'j@example.com'
              }

invalid_data = {'email': 'j_at_example'}


class TestJsonForm(TestCase):
    def test_form_picks_up_json_data(self):
        with app.test_client() as c:
            rv = c.post('/', data=json.dumps(valid_data), headers={'Content-Type': 'application/json'})
            form = NameForm()
            self.assertTrue(form.validate())

    def test_form_invalidates_invalid_data(self):
        with app.test_client() as c:
            rv = c.post('/', data=json.dumps(invalid_data), headers={'Content-Type': 'application/json'})
            form = NameForm()

            self.assertFalse(form.validate())
            self.assertTrue('name' in form.errors)
            self.assertTrue('email' in form.errors)
