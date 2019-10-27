# jsonforms
[![Build Status](https://travis-ci.org/dansonmuia/jsonforms.svg?branch=master)](https://travis-ci.org/dansonmuia/jsonforms)

This is a simple wrapper for using the popular WTForms library  to validate json data in flask applications.

### Why this wrapper?

Without this wrapper, your application code would look like:
```
from werkzeug.datastructures import MultiDict

from .forms import NameForm

@app.route('/', methods=['POST'])
def home():
    form = NameForm(MultiDict(request.get_json()))
    if form.validate:
        pass
```

Using this wrapper, you only need:
```
from .forms import JsonNameForm

@app.route('/', methods=['POST'])
def home():
    form = JsonNameForm()
    if form.validate:
        pass

```
Those less than 10 lines of code make your code cleaner

### Testing:

Clone the repository, and:

```
$ python3 -m venv venv

$ source venv/bin/activate

(venv)$ pip install -r requirements-dev.txt

(venv)$ pytest tests.py
```

