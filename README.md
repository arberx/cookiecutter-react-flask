# cookiecutter-react-flask

Love Flask? Love React?  `cookiecutter-react-flask` uses the `cookiecutter` library to setup a minimal, and modular 
flask-react project that you can run in seconds!

Included in the project are webpack, and babel configurations, package.json, and a setup.py.

### Prerequisites
#
* python3.6 (are any python3+ version, just make sure to modify the below commands.)
* node
* `cookiecutter`

### Setup
#
1) `git clone https://github.com/arberx/cookiecutter-react-flask.git`
2) In the directory you want the project to live:
   *  `python3.6 -m cookiecutter cookiecutter-react-flask`
   * Fill in both, `dir_name` and `app_name` when prompted.
 
### Run
#

1. (optional, but highly recommended) 
   cd into the projects directory (`dir_name` filled above) and run:
   * `python3.6 -m venv env`
   * `source env/bin/activate`
   * `pip3.6 install nodeenv`
   * `nodeenv --python-virtualenv`
   * `source env/bin/activate`

2. Install python packages, and node packages:
   * `pip3.6 install -e .`
   * `npm install .`

3. Run script located in the `app_name/bin` directory: 
   * `./app_name/bin/app_namerun.sh`

Head over to `localhost:8000`, you should see: **Hi! From cookiecutter-flask-react**

That's it!

### File Explanation

Inside the `app_name` folder
* `views/index.py` contains the main flask route, serving `index.html`.
* `templates/` contains the html template rendered by the main route. Flask will look at this folder when render_template is invoked.
* `js/` contains the javascript files for the app. Add new javascript files here!
* `static/` should contain things like images and css. 
* `static/js` this is very important. `webpack` will bundle everything in `js/` directory, and create a bundle.js in this directory. `templates/index.html` refrences `bundle.js` and that's how `ReactDOM` knows where to render the react components located in `js/`.
