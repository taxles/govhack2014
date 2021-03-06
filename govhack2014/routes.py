from govhack2014 import app
from govhack2014.models import *  # noqa
from flask import render_template, request, flash, redirect, url_for  # noqa
from govhack2014.resources import *  # noqa


def get_post_value(key):
    try:
        return request.form[key]
    except KeyError:
        return None


@app.route('/')
def index():
    return render_template('index.html')
