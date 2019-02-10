
import {{cookiecutter.app_name}}
import flask

@{{cookiecutter.app_name}}.app.route('/', methods=["GET"])
def main(methods=["GET"]):
    """ Main route, entry point for react. """ 
    return flask.render_template('index.html')
