import logging
import os
import sys
from flask import Flask, render_template


# Flask App Configurations
app_config = {
    # Set DEBUG to True only if you're on the development server.
    'DEBUG': True if os.getenv('SERVER_SOFTWARE', '').startswith('Development/') else False,
}


# Create the flask app
logging.info('Starting the Flask app!')
app = Flask(__name__)
app.config.update(app_config)


# Handle requests to the site root
@app.route("/")
def home_page():
    return render_template('hello.html')


# Handle string variable routes and passing parameters to the view
@app.route('/user/<username>')
def username_page(username):

    context = {
        'title': 'Username Page',
        'username': username,
    }

    return render_template('user.html', context=context)


# Handle integer variable routes and passing parameters to the view
@app.route('/post/<int:post_id>')
def post_page(post_id):

    context = {
        'title': 'Post Id Page',
        'post_id': post_id,
    }

    return render_template('post.html', context=context)
