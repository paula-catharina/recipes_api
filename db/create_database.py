import os
from config.config import db
from model.models import Recipe

# Data to initialize database with
RECIPES = [
    {
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
    },
    {
        "name": "Aqueous Martini",
        "ingredients": "water, green olives",
        "preparation": "Fill a cocktail shaker with ice. Pour in the gin and vermouth.Shake for 2-3 minutes. "
                       "Strain into a martini glass and garnish with an olive.",
        "servings": "1",
        "total_time": "5 minutes",
        "tags": "american, drink, in",
    },
    {
        "name": "Chilled Cucumber Soup",
        "ingredients": "cucumbers, greek yogurt, fresh lemon juice, shallot, garlic cloves, mint leaves, extra "
                       "virgin olive oil, salt, pepper, red onion",
        "preparation": "Blend the olive oil, cucumber, yogurt, lemon juice, shallots, garlic, mint leaves and salt and "
                       "pepper taste together. Refrigerate for 8 hours. Serve chilled, topped with a drizzle of olive "
                       "oil and the red onion.",
        "servings": "4",
        "total_time": "8 hours",
        "tags": "soup, american, very safe, no stove"
    }
]

# Delete database file if it exists currently
basedir = os.getenv("RECIPES_BASE_DATA_DIR")
if os.path.exists(basedir + "/db/recipes.db"):
    os.remove(basedir + "/db/recipes.db")

# Create the database
db.create_all()

# iterate over the RECIPES structure and populate the database
for recipe in RECIPES:
    recipe = Recipe(name=recipe.get("name"), ingredients=recipe.get("ingredients"),
                    preparation=recipe.get("ingredients"), servings=recipe.get("servings"),
                    total_time=recipe.get("total_time"), tags=recipe.get("tags"))
    db.session.add(recipe)

db.session.commit()