"""Server for product allergy app."""

from flask import Flask, render_template, flash, request, session, redirect, jsonify
from model import connect_to_db, db
import crud
import os, json
import codecs

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def home():
    """View homepage."""

    irritants = crud.get_irritantgroup()
    products = crud.get_product()

    return render_template("home.html", irritants=irritants, products=products)

@app.route("/submitirritants", methods=['GET','POST'])
def submit_irritants():
    """Add chosen irritants to tempolist.
    Compare to ingredients in chosen product """
    logged_in_email = session.get("user_email")
    #Below for if it's a non-user on the general page
    # if logged_in_email is None:
    allergylist = request.args.get('irritants').split(",")
    chosen_product = request.args.get('search')
    ig_by_pr = crud.get_irritantgroups_by_product(chosen_product, allergylist)
    if logged_in_email:
        user_id = crud.get_user_by_email(logged_in_email).user_id
        for allergy in allergylist:
            irritantgroup_id = crud.get_irritantgroup_id_by_name(allergy)
            irritantgroup = crud.create_userirritantgroup(user_id, irritantgroup_id)
            db.session.add(irritantgroup)
            db.session.commit()
        product_id = crud.get_product_id_by_name(chosen_product)
        if ig_by_pr:
            print ("\n" * 4 )
            print(ig_by_pr)
            print('wow')
            print(crud.get_ingredients_in_ig_group(chosen_product))
            print("\n" * 4 )
            approved = False
        else:
            approved = True
        already_searched = crud.searchedproduct_by_userid_productid(user_id, product_id)
        if not already_searched:
            searchedproduct = crud.create_searchedproduct(user_id=user_id, product_id = product_id, approved = approved, favorited = None)
            db.session.add(searchedproduct)
            db.session.commit()

    if ig_by_pr:
        return (f'Boo, you are allergic to {chosen_product}')
    else:
        return (f'Yay! You are not allergic to {chosen_product}!')
 
@app.route('/addfavorite', methods=['GET', 'POST'])
def add_favorite():
    """adds that searched product to a users favorites/ changes the objects favorite attribute"""
    favobj = request.args.get('name')
    print(favobj)
    fproduct = crud.searchedproduct_by_id(favobj)
    fproduct.favorited = True
    db.session.commit()
    


    return (f"{fproduct} has been added to your favorites!")




@app.route('/search', methods=['POST'])
def search():
    """ does search through products"""

    term = request.form["q"]
    print ('term: ', term)

    json_data = crud.get_product_name_list(term)


    filtered_dict = [v.product_name for v in json_data]
    # filtered_dict = [v for v in json_data if term in v]
    # print(filtered_dict)

    resp = jsonify(filtered_dict)
    resp.status_code = 200
    return resp


@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a user."""

    user = crud.get_user_by_id(user_id)
    # ratings = crud.get_ratings_by_user(user_id);
    irritants = crud.get_irritantgroup()
    products = crud.get_product()
    user_irritantgroups = crud.get_user_irritantgroups_by_user_id(user_id)
    user_searchedproducts = crud.get_searched_products_by_user_id(user_id)

    return render_template("user_details.html", user=user, irritants=irritants, products=products, user_irritantgroups=user_irritantgroups, user_searchedproducts=user_searchedproducts)


@app.route("/register", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
        return redirect("/")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}, {user.user_id}!")
        return redirect(f"/users/{user.user_id}")

   #BELOW IS THE CODE WE'LL WANT TO USE ON USER LOGIN PAGES
    # if request.method =='POST':
    #     allergylist = request.form.getlist('ingredients')
    #     print(allergylist)
    #     for item in allergylist:
    #         i_id = crud.get_ingredient_id_by_name(item)
    #         useringredient = crud.create_useringredient(1, i_id) #USING 1 FOR NOW
    #         db.session.add(useringredient)
    #         db.session.commit()




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)