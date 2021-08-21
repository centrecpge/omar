from flask import Flask
from .views import main
from .extensions import *
from .admin import admin
from .user import user
def create_app(config_file='settings.py'):
	app=Flask(__name__)
	app.config.from_pyfile(config_file)
	db.init_app(app)
	bootstrap.init_app(app)
	app.register_blueprint(main)
	app.register_blueprint(user)
	app.register_blueprint(admin)

	# app.app_context()
	return app

