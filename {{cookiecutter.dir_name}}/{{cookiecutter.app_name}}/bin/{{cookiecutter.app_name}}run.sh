#!/bin/bash

set -e
set -x

# Set up environment for Flask debug server
export FLASK_DEBUG=True
export FLASK_APP={{cookiecutter.app_name}}

# Compile js in the background
 npm run watch &

# Run development server
flask run --port 8000
