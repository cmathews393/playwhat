from flask import Flask, render_template, request, blueprints, jsonify
import os
from playwhat.modules import gamepass


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )
    
    product_info = gamepass.mainfunc()

    @app.route("/")
    def home():
        return render_template("index.html.j2", product_info=product_info)

    return app