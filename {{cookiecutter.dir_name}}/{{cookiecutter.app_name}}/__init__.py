
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)

# (Reference http://flask.pocoo.org/docs/0.12/patterns/packages/)
import {{cookiecutter.app_name}}.views
