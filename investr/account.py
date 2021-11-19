import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from investr.db import get_db

bp = Blueprint('account', __name__, url_prefix='/account')


@bp.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == "GET":

        return render_template('account/home.html')


@bp.route('/quote', methods = ['GET', 'POST'])
def quote():
    if request.method == "GET":

        return render_template('account/home.html')


bp.route('indices', methods = ['GET', 'POST'])
def indices():
    if request.method == "GET":

        index_info = indices()

        return render_template('account/indices.html', index_info)