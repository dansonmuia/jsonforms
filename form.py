from werkzeug.datastructures import MultiDict
from flask import request
from wtforms import Form


class JsonForm(Form):
    def __init__(self):
        data = MultiDict(request.get_json())
        super(JsonForm, self).__init__(data)
