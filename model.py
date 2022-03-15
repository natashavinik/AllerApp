"""Models for skin allergy app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    useringredients = db.relationship('UserIngredient', back_populates="user") 

    searchedproducts = db.relationship('SearchedProduct', back_populates="user") 



    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Ingredient(db.Model):
    """An ingredient."""

    __tablename__ = "ingredients"

    ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ingredient_name = db.Column(db.String)

    altingredientnames = db.relationship('AltIngredientName', back_populates="ingredient") 
    useringredients = db.relationship('UserIngredient', back_populates="ingredient") 


    def __repr__(self):
        return f"<Ingredient ingredient_id={self.ingredient_id} ingredient_name={self.ingredient_name}>"


class AltIngredientName(db.Model):
    """Alternate name for ingredient"""

    __tablename__ = "altingredientnames"

    alt_ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))
    alt_ingredient_name = db.Column(db.String)

    ingredient = db.relationship('Ingredient', back_populates="altingredientnames") 


    def __repr__(self):
        return f"<Alternate Ingredient Name alt_ingredient_id={self.alt_ingredient_id} alt_ingredient_name={self.alt_ingredient_name}>"


class UserIngredient(db.Model):
    """A user's ingredient to avoid."""

    __tablename__ = "useringredients"

    user_ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))

    
    user = db.relationship('User', back_populates="useringredients")
    ingredient = db.relationship('Ingredient', back_populates="useringredients") 


    def __repr__(self):
        return f"<UserIngredientID user_ingredient_id={self.user_ingredient_id} ingredient_id={self.ingredient_id}>"


class Product(db.Model):
    """A product."""

    __tablename__ = "products"

    product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_name = db.Column(db.String)
    product_type = db.Column(db.String)

    searchedproducts = db.relationship('SearchedProduct', back_populates="product") 
    productingredients = db.relationship('ProductIngredient', back_populates="product") 


    def __repr__(self):
        return f"<Product product_id={self.product_id} product_name={self.product_name}>"


class ProductIngredient(db.Model):
    """A product's ingredeint."""

    __tablename__ = "productingredients"

    product_ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))
    ingredient = db.Column(db.String)

    product = db.relationship('Product', back_populates="productingredients") 


    def __repr__(self):
        return f"<ProductIngredient product_ingredient_id={self.product_ingredient_id} ingredient={self.ingredient}>"
    

class SearchedProduct(db.Model):
    """A products that a user has searched."""

    __tablename__ = "searchedproducts"

    searched_product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    favorited = db.Column(db.Boolean)
    approved = db.Column(db.Boolean)

    user = db.relationship('User', back_populates="searchedproducts") 
    product = db.relationship('Product', back_populates="searchedproducts") 


    def __repr__(self):
        return f"<SearchedProduct Searched_product_id={self.searched_product_id} product_id={self.product_id}>"








def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
