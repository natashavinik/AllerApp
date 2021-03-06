"""CRUD operations."""

from model import db, User, IrritantGroup, Ingredient, UserIrritantGroup, Product, ProductIngredient, SearchedProduct, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


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


def get_irritantgroups_by_product(chosenproduct, allergylist):
    """lists irritant groups by product name"""

    return Ingredient.query.filter(Ingredient.irritantgroup_id.is_not(None))\
                     .join(ProductIngredient).join(Product)\
                     .filter(Product.product_name == chosenproduct).join(IrritantGroup)\
                     .filter(IrritantGroup.irritantgroup_name.in_(allergylist)).all()
    # return IrritantGroup.query.join(Ingredient).join(ProductIngredient).join(Product).filter(Product.product_name == chosenproduct).filter(Ingredient.irritantgroup_id.is_not(None)).all()

def get_irritant_ingredient_names(igbyprs):
    """A products ingredients that a user is allergic to based on allergies"""
    igname = []
    for obj in igbyprs:
        igname.append(obj.ingredient_name)
    return ", ".join(igname)     


def get_ingredient_by_name(ingredient_name):
    """Return an ingredient by it's name."""

    return Ingredient.query.filter_by(ingredient_name = ingredient_name).first()


def get_ingredient_names_by_product(productname):
    """Return a list of ingredients by product"""
    cp_ingredientsobj = Ingredient.query.join(ProductIngredient).join(Product).filter(Product.product_name == productname).all()
    cp_ingredients = []
    for obj in cp_ingredientsobj:
        cp_ingredients.append(obj.ingredient_name)
    return cp_ingredients


def create_userirritantgroup(user_id, irritantgroup_id):
    """Create and return a new user irritant group."""

    userirritantgroup = UserIrritantGroup(user_id=user_id, irritantgroup_id=irritantgroup_id)

    return userirritantgroup

def get_user_irritantgroups_by_user_id(user_id):
    """Get user irritant groups by a users id"""
    
    return IrritantGroup.query.join(UserIrritantGroup).join(User).filter(User.user_id == user_id).all()
    # return UserIrritantGroup.query.filter(user_id = user_id).all()

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


def get_product_id_by_name(product_name):
    """Return a product ID by name."""
    #gets are only for primary keys
    pr_name = Product.query.filter_by(product_name=product_name).one()

    return pr_name.product_id


def get_searchedproducts_by_user_id(user_id):
    """get products a user has searched for"""
    # return Product.query.join(SearchedProduct).join(User).filter(User.user_id == user_id).all()
    return SearchedProduct.query.join(Product).join(User).filter(User.user_id == user_id).all()

def get_allergic_products_by_user_id(u_id):
    """get allergic products by user id"""
    return SearchedProduct.query.filter_by(user_id = u_id, approved=False).join(Product).all()

def get_notallergic_products_by_user_id(u_id):
    """get notallergic products by user id"""
    return SearchedProduct.query.filter_by(user_id = u_id, approved=True).join(Product).all()


def get_favorite_products_by_user_id(u_id):
    """get favorite products by user id"""
    return SearchedProduct.query.filter_by(user_id = u_id, favorited=True).join(Product).all()


def create_searchedproduct(user_id, product_id, approved, favorited):
    """Create and return a new searchedproduct."""

    searchedproduct = SearchedProduct(user_id=user_id, product_id=product_id, approved=approved, favorited=favorited)

    return searchedproduct

def searchedproduct_by_id(sp_id):
    """return searched product by id"""
    return SearchedProduct.query.filter_by(searched_product_id=sp_id).one()

def user_id_by_searchedproduct_id(sp_id):
    """return user id by searched product id"""
    return User.query.join(SearchedProduct).filter(SearchedProduct.searched_product_id==sp_id).one()


def searchedproduct_by_userid_productid(users_id, products_id):
    """return searched product byproduct id and user"""
    return SearchedProduct.query.filter_by(user_id = users_id, product_id = products_id).first()



if __name__ == "__main__":
    from server import app

    connect_to_db(app)



# def get_users():
#     """Return all users."""

#     return User.query.all()


# def get_irritantgroup_by_id(irritantgroup_id):
#     """Return an irritantgroup by primary key."""

#     return IrritantGroup.query.get(irritantgroup_id)

# def get_irritantgroup_by_name(irritantgroup_name):
#     """Return an irritantgroup by name."""

#     return IrritantGroup.query.get(irritantgroup_name)

# def get_ingredients():
#     """Return all ingredients."""

#     return Ingredient.query.all()


# def get_ingredients_by_group_id(irritantgroup_id):
#     """Return a list of all ingredients by irritantgroupID."""
    
#     return Ingredient.query.filter_by(irritantgroup_id=irritantgroup_id).all()

# def get_ingredients_in_ig_group(chosenproduct):

#     return Ingredient.query.filter(Ingredient.irritantgroup_id.is_not(None))\
#                      .join(ProductIngredient).join(Product)\
#                      .filter(Product.product_name == chosenproduct).all()


# def get_ingredient_by_id(ingredient_id):
#     """Return an ingredient by ingredientID."""

#     return Ingredient.query.get(ingredient_id)

# def get_ingredients_by_product(productname):
#     """Return a list of ingredients by product"""
#     return Ingredient.query.join(ProductIngredient).join(Product).filter(Product.product_name == productname).all()

# def create_user_irritantgroup_allergylist(user_id, allergylist):
#     """Create and return a new user irritant group from allergy list."""
#     for allergy in allergylist:
#         irritantgroup_id = get_irritantgroup_id_by_name(allergy)
#         bob = create_userirritantgroup(user_id, irritantgroup_id)
#     return bob
#     # return UserIrritantGroup.query.filter_by(user_id = user_id).all()