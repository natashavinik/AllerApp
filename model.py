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

    irritantgroups = db.relationship("IrritantGroup", secondary="userirritantgroups", back_populates="users") 
    searchedproducts = db.relationship("SearchedProduct", back_populates="user") 

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class IrritantGroup(db.Model):
    """A group of potential irritating ingredients."""

    __tablename__ = "irritantgroups"

    irritantgroup_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    irritantgroup_name = db.Column(db.String)

    ingredients = db.relationship("Ingredient", back_populates="irritantgroup")
    users = db.relationship("User", secondary="userirritantgroups", back_populates="irritantgroups")


    def __repr__(self):
        return f"<IrritantGroup irritantgroup_id={self.irritantgroup_id} irritantgroup_name={self.irritantgroup_name}>"


class Ingredient(db.Model):
    """An ingredient"""

    __tablename__ = "ingredients"

    ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ingredient_name = db.Column(db.String)

    irritantgroup_id = db.Column(db.Integer, db.ForeignKey('irritantgroups.irritantgroup_id'), nullable=True)
    
    irritantgroup = db.relationship('IrritantGroup', back_populates="ingredients")

    products = db.relationship("Product", secondary="productingredients", back_populates="ingredients")


    def __repr__(self):
        return f"<Ingredient ingredient_id={self.ingredient_id} ingredient_name={self.ingredient_name}>"


class UserIrritantGroup(db.Model):
    """A user's irritant groups to avoid."""

    __tablename__ = "userirritantgroups"

    user_irritantgroup_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    irritantgroup_id = db.Column(db.Integer, db.ForeignKey("irritantgroups.irritantgroup_id"), nullable=False)



    def __repr__(self):
        return f"<UserIrritantgroup user_irritantgroup_id={self.user_irritantgroup_id} irritantgroup_id={self.irritantgroup_id}>"


class Product(db.Model):
    """A product."""

    __tablename__ = "products"

    product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_name = db.Column(db.String)
    product_type = db.Column(db.String)

    searchedproducts = db.relationship('SearchedProduct', back_populates="product") 

    ingredients = db.relationship('Ingredient', secondary="productingredients", back_populates="products")


    def __repr__(self):
        return f"<Product product_id={self.product_id} product_name={self.product_name}>"

class ProductIngredient(db.Model):
    """A product's ingredient."""

    __tablename__ = "productingredients"

    product_ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.ingredient_id"), nullable=False)



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




def connect_to_db(flask_app, db_uri="postgresql:///allergyingredients", echo=True):
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



