"""CRUD operations."""

from model import db, User, IrritantGroup, Ingredient, UserIrritantGroup, Product, ProductIngredient, SearchedProduct, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()



def create_irritantgroup(irritantgroup_name):
    """Create and return a new irritant group."""

    irritantgroup = IrritantGroup(irritantgroup_name=irritantgroup_name)

    return irritantgroup


def get_irritantgroup():
    """Return all irritantgroups."""

    return IrritantGroup.query.all()


def get_irritantgroup_by_id(irritantgroup_id):
    """Return an irritantgroup by primary key."""

    return IrritantGroup.query.get(irritantgroup_id)

def get_irritantgroup_by_name(irritantgroup_name):
    """Return an irritantgroup by name."""

    return IrritantGroup.query.get(irritantgroup_name)

def get_irritantgroup_id_by_name(irritantgroup_name):
    """Return an irritantgroup ID by name."""
    #gets are only for primary keys

    ig_name = IrritantGroup.query.filter_by(irritantgroup_name=irritantgroup_name).one()

    return ig_name.irritantgroup_id



def create_ingredient(irritantgroup_id, ingredient_name):
    """Create and return a new ingredient."""

    ingredient = Ingredient(irritantgroup_id=irritantgroup_id, ingredient_name=ingredient_name)
    #would be way cooler to pass through the irritant group
    return ingredient


def get_ingredients():
    """Return all ingredients."""

    return Ingredient.query.all()


#get all altnames based off of ingredient id name

def get_ingredients_by_group_id(irritantgroup_id):
    """Return a list of all ingredients by irritantgroupID."""
    
    return Ingredient.query.filter_by(irritantgroup_id=irritantgroup_id).all()

## querying a product and it's ingredients seeing if irritant group associated
# and if that irritant group is one that user selected?

# User list of irritant groups. (can pre-click checkboxes for logged in user) (keep same form)
#get product ingredients, filter by irritant group is not none, 
# # then see if any irritant groups are included in list they are awnting to avoid
# convert the list of irritants from product ingregiendts to a set and compare to chosen irritant groups


#list of irritant groups - 
# 
def get_irritantgroups_by_product(chosenproduct, allergylist):
    """lists irritant groups by product name"""

    return Ingredient.query.filter(Ingredient.irritantgroup_id.is_not(None))\
                     .join(ProductIngredient).join(Product)\
                     .filter(Product.product_name == chosenproduct).join(IrritantGroup)\
                     .filter(IrritantGroup.irritantgroup_name.in_(allergylist)).all()
    # return IrritantGroup.query.join(Ingredient).join(ProductIngredient).join(Product).filter(Product.product_name == chosenproduct).filter(Ingredient.irritantgroup_id.is_not(None)).all()

#(each of above can do .irritantgroup.irritantgroup_name) for latesss




def get_ingredient_by_id(ingredient_id):
    """Return an ingredient by ingredientID."""

    return Ingredient.query.get(ingredient_id)

def get_ingredient_by_name(ingredient_name):
    """Return an ingredient by it's name."""

    return Ingredient.query.filter_by(ingredient_name = ingredient_name).first()

def get_ingredients_by_product(productname):
    """Return a list of ingredients by product"""
    return Ingredient.query.join(ProductIngredient).join(Product).filter(Product.product_name == productname).all()


def create_user_irritantgroup_allergylist(user_id, allergylist):
    """Create and return a new user irritant group from allergy list."""
    for allergy in allergylist:
        irritantgroup_id = get_irritantgroup_id_by_name(allergy)
        bob = create_userirritantgroup(user_id, irritantgroup_id)
    return bob
    # return UserIrritantGroup.query.filter_by(user_id = user_id).all()

def create_userirritantgroup(user_id, irritantgroup_id):
    """Create and return a new user irritant group."""

    userirritantgroup = UserIrritantGroup(user_id=user_id, irritantgroup_id=irritantgroup_id)

    return userirritantgroup

def get_user_irritantgroups_by_user_id(user_id):
    """Get user irritant groups by a users id"""
    
    return IrritantGroup.query.join(UserIrritantGroup).join(User).filter(User.user_id == user_id).all()
    # return UserIrritantGroup.query.filter(user_id = user_id).all()

    ###FUNCTION TO GET ALL OF THESE
    ###FUNCTION TO GET AL OF THESE BY USER ID

def create_product(product_name, product_type):
    """Create and return a new product."""

    product = Product(product_name=product_name, product_type=product_type)

    return product

def get_product():
    """Return all products."""

    return Product.query.all()

def get_product_name_list(search_term):
    """Return products that start with the search term"""

    return Product.query.filter(Product.product_name.like(f'%{search_term}%')).all()

# def get_product_name_list():
#     """Return product names"""
#     prod_name_list = []

#     for prod in Product.query.all():
#         prod_name_list.append(prod.product_name)
#     return prod_name_list


    ##FUNCTION TO GET ALL OF THESE
    ##FUNCTION TO GET THIS BY PRODUCT NAME
    ##FUNCTION TO GET ALL BY PRODUCT TYPE?

def get_product_id_by_name(product_name):
    """Return a product ID by name."""
    #gets are only for primary keys
    pr_name = Product.query.filter_by(product_name=product_name).one()

    return pr_name.product_id


    ##FUNCTION TO RETURN ALL OF THESE
    ##FUNCTION TO RETURN ALL BY PRODUCT NAME

def create_searchedproduct(user_id, product_id, approved, favorited):
    """Create and return a new searchedproduct."""

    searchedproduct = SearchedProduct(user_id=user_id, product_id=product_id, approved=approved, favorited=favorited)

    return searchedproduct

    ##FUNCTION TO RETURN ALL OFTHESE
    ##FUNCTION TO RETURN THESE BY USER
    ##FUNCTION TO FIGURE OUT IF THESE ARE APPROVED OR NOT? (LOOKAT CRUD FROM MOVIE LAB)

# def compare_lists(list_1, list_2):
#     """Compare allergy and product ingredients
#     if they share an ingredient, print True and the ingredient(s), otherwise False"""

#     a_set = set(list_1)
#     b_set = set(list_2)
#     if len(a_set.intersection(b_set)) > 0:
#         print(a_set.intersection(b_set))
#         return True
#     return False

# def make_full_allergy_list(allergy_input):
#     """Takes users checkboxed broad allergy input,
#     creates list of all specific allergic"""
#     full_allergy_list = []

#     for item in allergy_input:
#         i_id = get_ingredient_id_by_name(item)
#         alt_list = get_alt_ingredients_by_id(i_id)
#         full_allergy_list.extend(alt_list)

#     return full_allergy_list


if __name__ == "__main__":
    from server import app

    connect_to_db(app)