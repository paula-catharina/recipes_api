import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


basedir = os.getenv("RECIPES_BASE_DATA_DIR")
swagger_dir = basedir + '\swagger'
db_dir = basedir + '\db'
# Create the connexion application instance
connex_app = connexion.App(__name__, specification_dir=swagger_dir)

# Get the underlying Flask app instance
app = connex_app.app

# Build the Sqlite URL for SqlAlchemy
sqlite_uri = "sqlite:///" + os.path.join(db_dir, "recipes.db")

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)