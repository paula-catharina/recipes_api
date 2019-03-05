"""
This is the recipes module and supports all the ReST actions for the
RECIPES collection
"""
from flask import make_response, abort
from config.config import db
from model.models import Recipe, RecipeSchema


def read_all():
    """
    This function responds to a request for /api/recipes
    with the complete lists of recipes
    :return: json string of list of recipes
    """
    # Create the list of recipes from existing data
    recipe = Recipe.query.order_by(Recipe.name).all()
    # Serialize data
    recipe_schema = RecipeSchema(many=True)
    data = recipe_schema.dump(recipe).data
    return data


def read_one(name):
    """
    This function responds to a request for /api/recipes/{name}
    with one matching recipe from recipes
    :param name: name of recipe to find
    :return: recipe matching name
    """
    # Get the recipe requested
    recipe = Recipe.query.filter(Recipe.name == name).one_or_none()

    if recipe is not None:
        recipe_schema = RecipeSchema()
        data = recipe_schema.dump(recipe).data
        return data

    # If recipe id does not exist
    else:
        abort(
            404,
            "Recipe not found for name: {name}".format(name=name),
        )

    return recipe


def read_ingredient(ingredient):
    """
    This function responds to a request for /api/recipes/ingredient/{ingredient}
    with one matching recipe from recipes
    :param ingredient: name of ingredient to find
    :return: recipe matching ingredient name
    """
    # Get the recipe requested
    recipe = Recipe.query.filter(Recipe.ingredients.contains(ingredient)).all()

    if recipe is not None:
        recipe_schema = RecipeSchema(many=True)
        data = recipe_schema.dump(recipe).data
        return data

    # If recipe id does not exist
    else:
        abort(
            404,
            "Recipe not found with ingredient: {ingredient}".format(ingredient=ingredient),
        )

    return recipe


def read_tag(tag):
    """
    This function responds to a request for /api/recipes/tag/{tag}
    with one matching recipe from recipes
    :param tag: tag to find
    :return: recipes matching tag
    """
    # Get the recipe requested
    recipe = Recipe.query.filter(Recipe.tags.contains(tag)).all()

    if recipe is not None:
        recipe_schema = RecipeSchema(many=True)
        data = recipe_schema.dump(recipe).data
        return data

    # If recipe id does not exist
    else:
        abort(
            404,
            "Recipe not found with tag: {tag}".format(tag=tag),
        )

    return recipe


def create(recipe):
    """
    This function creates a new recipe in the recipes structure
    based on the passed in recipes data
    :param recipe:  recipe to create in people structure
    :return: 201 on success, 406 on recipes exists
    """
    name = recipe.get('name')
    ingredients = recipe.get('ingredients')
    preparation = recipe.get('preparation')
    servings = recipe.get('servings')
    total_time = recipe.get('total_time')
    tags = recipe.get('tags')

    existing_recipe = Recipe.query \
        .filter(Recipe.name == name) \
        .filter(Recipe.ingredients == ingredients) \
        .filter(Recipe.preparation == preparation) \
        .filter(Recipe.servings == servings) \
        .filter(Recipe.total_time == total_time) \
        .filter(Recipe.tags == tags) \
        .one_or_none()

    # Is it possible to insert the recipe?
    if existing_recipe is None:

        # Create a recipe instance using the schema and the passed-in recipe
        schema = RecipeSchema()
        new_recipe = schema.load(recipe, session=db.session).data

        # Add the recipe to the database
        db.session.add(new_recipe)
        db.session.commit()

        # Serialize and return the newly created person in the response
        return schema.dump(new_recipe).data, 201

    # Otherwise, if recipe exists already
    else:
        abort(406, f'recipe {name} exists already')


def update(name, recipe):
    """
    This function updates an existing recipe in the recipe structure
    :param name: name of recipe to update in the recipes structure
    :param recipe: recipe to update
    :return: updated recipe structure
    """
    # Get the recipe requested from the db into session
    recipe_to_update = Recipe.query.filter(Recipe.name == name).one_or_none()

    # Did we find a recipe?
    if recipe_to_update is not None:

        # turn the passed in recipe into a db object
        schema = RecipeSchema()
        updated_recipe = schema.load(recipe, session=db.session).data

        # set the id for updated recipe
        updated_recipe.recipe_id = recipe_to_update.recipe_id

        # merge the new object into the old and commit it to the db
        db.session.merge(updated_recipe)
        db.session.commit()

        # return updated recipe in the response
        data = schema.dump(updated_recipe).data

        return data, 200

    # Otherwise, recipe wasn't found
    else:
        abort(
            404,
            "Recipe not found for name: {name}".format(name=name),
        )


def delete(name):
    """
    This function deletes a recipe from the recipe structure
    :param name: name of recipe to delete
    :return: 200 on successful delete, 404 if not found
    """
    # Get the recipe requested
    recipe = Recipe.query.filter(Recipe.name == name).one_or_none()

    # If recipe exists
    if recipe is not None:
        db.session.delete(recipe)
        db.session.commit()
        return make_response(
            "Recipe {name} deleted".format(name=name), 200
        )

    # If recipe doesn't exist
    else:
        abort(
            404,
            "Recipe not found for name: {name}".format(name=name),
        )