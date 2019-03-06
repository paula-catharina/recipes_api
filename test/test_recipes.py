from api import recipes
import unittest
from unittest.mock import MagicMock
from werkzeug.exceptions import HTTPException


mock_recipe_existing = {
        "name": "Pasta Puttanesca",
        "ingredients": "extra virgin olive oil, garlic cloves, peeled tomatoes, basil, "
                       "kalamata olives, anchovy, drained capers, dried oregano, "
                       "dried crushed red pepper, spaghetti, parsley, parmesan cheese",
        "preparation": "Heat oil in large pot over medium heat. Add garlic and sauté until fragrant, about 1 minute. "
                       "Add tomatoes with puree, olives, anchovies, capers, oregano, and crushed red pepper. Simmer "
                       "sauce over medium-low heat until thickened, breaking up tomatoes with spoon, about 8 minutes. "
                       "Season with salt and pepper. Meanwhile, cook pasta in large pot of boiling salted water until "
                       "tender but still firm to bite. Drain pasta; return to same pot. Add sauce and parsley. "
                       "Toss over low heat until sauce coats pasta, about 3 minutes. Serve with cheese",
        "servings": "4",
        "total_time": "15 minutes",
        "tags": "italian, fish, olive, pasta, tomato, quick and easy, not roast beef"
    }
wrong_recipe_name = "This is not a recipe"
wrong_tag = "Not a tag"
wrong_ingredient = "Not a ingredient"


class TestRecipes(unittest.TestCase):
    def testCreateExistingRecipe(self):
        print("\n - Testing api.recipes.create() with existing recipe")

        query = MagicMock()
        filter = MagicMock()
        query.filter.return_value = filter
        filter.filter.return_value = filter
        filter.one_or_none.return_value = mock_recipe_existing

        recipes.Recipe.query = query

        with self.assertRaises(HTTPException) as http_error:
            recipes.create(mock_recipe_existing)

        self.assertEqual(http_error.exception.code, 406)

    def testDeleteNonExistingRecipe(self):
        print("\n - Testing api.recipes.delete() with non existing recipe")

        query = MagicMock()
        filter = MagicMock()
        query.filter.return_value = filter
        filter.one_or_none.return_value = None

        recipes.Recipe.query = query

        with self.assertRaises(HTTPException) as http_error:
            recipes.delete(wrong_recipe_name)

        self.assertEqual(http_error.exception.code, 404)

    def testUpdateNonExistingRecipe(self):
        print("\n - Testing api.recipes.update() with non existing recipe")

        query = MagicMock()
        filter = MagicMock()
        query.filter.return_value = filter
        filter.one_or_none.return_value = None

        recipes.Recipe.query = query

        with self.assertRaises(HTTPException) as http_error:
            recipes.update(wrong_recipe_name, mock_recipe_existing)

        self.assertEqual(http_error.exception.code, 404)

    def testReadOneNonExistingRecipe(self):
        print("\n - Testing api.recipes.read_one() with non existing recipe")

        query = MagicMock()
        filter = MagicMock()
        query.filter.return_value = filter
        filter.one_or_none.return_value = None

        recipes.Recipe.query = query

        with self.assertRaises(HTTPException) as http_error:
            recipes.read_one(wrong_recipe_name)

        self.assertEqual(http_error.exception.code, 404)

    def testReadIngredientNonExistingRecipe(self):
        print("\n - Testing api.recipes.read_ingredient() with non existing ingredient")

        query = MagicMock()
        filter = MagicMock()
        query.filter.return_value = filter
        filter.all.return_value = None

        recipes.Recipe.query = query

        with self.assertRaises(HTTPException) as http_error:
            recipes.read_ingredient(wrong_ingredient)

        self.assertEqual(http_error.exception.code, 404)

    def testReadTagNonExistingRecipe(self):
        print("\n - Testing api.recipes.read_tag() with non existing tag")

        query = MagicMock()
        filter = MagicMock()
        query.filter.return_value = filter
        filter.all.return_value = None

        recipes.Recipe.query = query

        with self.assertRaises(HTTPException) as http_error:
            recipes.read_ingredient(wrong_tag)

        self.assertEqual(http_error.exception.code, 404)