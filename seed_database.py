"""Script to seed database."""

import os
import json

import crud
import model
import server

os.system("dropdb allergyingredients")
os.system("createdb allergyingredients")

model.connect_to_db(server.app)
model.db.create_all()

# Load bad ingredients from JSON file
import codecs

badingredients = json.load(codecs.open('data/avoidingredients.json', 'r', 'utf-8-sig'))

productlist = json.load(codecs.open('data/realproducts.json', 'r', 'utf-8-sig'))
# productlist = json.load(codecs.open('data/testproducts.json', 'r', 'utf-8-sig'))


# Create ingredients and store them in list
print(badingredients)


# in one for loop i can create the irritant group and add them ot new ingredients

# in products

###Adds irritant groups from baddies dictionary,
### then adds those ingredients to ingredient database

for n_irritant in badingredients:

    db_irritantgroup = crud.create_irritantgroup(n_irritant)
    model.db.session.add(db_irritantgroup)
    model.db.session.commit()
    ig_id = db_irritantgroup.irritantgroup_id
    irritantingredient = crud.create_ingredient(ig_id, n_irritant)
    model.db.session.add(irritantingredient)
    model.db.session.commit()

    for ingredient in badingredients[n_irritant]:
        db_ingredient = crud.create_ingredient(ig_id, ingredient)
        model.db.session.add(db_ingredient)

model.db.session.commit()



#Create product ingredients and store them in database, make product
for n_product in productlist:
    ingredientlist = []
    for pr_in in n_product["ingredients"]:
        # check if ingredient is in the database (crud? get ingredient by name, .first, returns none if none)
        if crud.get_ingredient_by_name(pr_in) is None:
            db_ingredient = crud.create_ingredient(irritantgroup_id=None, ingredient_name=pr_in)
            model.db.session.add(db_ingredient)
        # skip this  -check if it belongs to an irritant group (crud?)
        # skip this  - if so, add irritant group to ingredient (is this crud?)
        #add ingredient instance to ingredientlist
        ingredient = crud.get_ingredient_by_name(pr_in)
        ingredientlist.append(ingredient)

    # create product
    product_name, product_type = (
        (n_product["name"] + " - " + n_product["brand"]),
        n_product["type"],
    )
    db_product = crud.create_product(product_name, product_type)
    db_product.ingredients.extend(ingredientlist)
    model.db.session.add(db_product)
    

model.db.session.commit()




# #Create product ingredients and store them in database
# for n_product in productlist:
#     n_id = crud.get_product_id_by_name(n_product["name"])

#     for pr_in in n_product["ingredients"]:
#         db_prodingredient = crud.create_productingredient(n_id, pr_in) ###maybe we dont need this now?
#         model.db.session.add(db_prodingredient)

# model.db.session.commit()

# Create 10 users
for n in range(10):
    email = f"user{n}@test.com"
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)

model.db.session.commit()
