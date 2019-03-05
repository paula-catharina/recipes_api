from datetime import datetime
from config.config import db, ma


class Recipe(db.Model):
    __tablename__ = "recipe"
    recipe_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    preparation = db.Column(db.String)
    servings = db.Column(db.Integer)
    total_time = db.Column(db.String)
    tags = db.Column(db.String)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class RecipeSchema(ma.ModelSchema):
    class Meta:
        model = Recipe
        sqla_session = db.session