from flask import Flask
import flask.cli
import subprocess


app = Flask(__name__)
flask.cli.show_server_banner = lambda *args: None

import logging
logging.getLogger("werkzeug").disabled = True


@app.route('/external')
def display_external():
    subprocess.run(["DisplaySwitch", "/External"])
    return "Switching to external display..."


@app.route('/extend')
def display_extend():
    subprocess.run(["DisplaySwitch", "/Extend"])
    return "Switching to monitors..."


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
