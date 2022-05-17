import os

from .api.application import create_app

app = create_app(os.getenv("FLASK_ENV"))

from .db import db
from .create_data import create_sample_data
