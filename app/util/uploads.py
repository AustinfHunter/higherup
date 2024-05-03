import os
from flask import current_app
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_image(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(
            current_app.root_path +
            "/static/images/uploads/" + filename
        )
        return filename
    return ""
