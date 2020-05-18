class Recipe:
    # every ingredient is measured in cups
    # except for salt, pepper (pinch), and eggs
    def __init__(self, flour, yeast, sugar, salt, pepper, eggs):
        self.flour = flour
        self.yeast = yeast
        self.sugar = sugar
        self.salt = salt
        self.pepper = pepper
        self.eggs = eggs
    def list_ingredients():
        print("This is a new recipe")
        list_ingredients = classmethod(list_ingredients)

bread = Recipe(2, 1, 0, 1, 1, 0)
print(bread.eggs)
