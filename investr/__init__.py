import os

from flask import Flask

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'investr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/welcome')
    def welcome():
        return 'Welcome!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import account
    app.register_blueprint(account.bp)

    return app

from helpers import index_info
