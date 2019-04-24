
# from flask import Flask, request, make_response, session, escape
# from werkzeug.utils import secure_filename
# file_name = secure_filename(f.filename)
from blink.app import create_app

app = create_app(env='dev')

if __name__ == "__main__":
    app.run()
