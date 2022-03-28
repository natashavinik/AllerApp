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

@app.route("/submitirritants", methods=['GET'])
def submit_irritants():
    """Add chosen irritants to userirritants table.
    Compare to ingredients in chosen product """


    
    allergylist = request.args.get('irritants').split(",")
    print(type(allergylist))
    print("\n"*4)
    print(allergylist)
    # full_allergy_list = crud.make_full_allergy_list(allergylist)
    # ### do this w/ sqlAlchemy queries like the productname list

    chosen_product = request.args.get('search')
    print("\n"*4)
    print(chosen_product)
    print("\n"*4)
    ig_by_pr = crud.get_irritantgroups_by_product(chosen_product, allergylist)
    print("\n"*4)
    print("bob")
    print(ig_by_pr)
    print("bob")
    print("\n"*4)


    if ig_by_pr:
        return (f'Boo, you are allergic to {chosen_product}')
    else:
        return (f'Yay! You are not allergic to {chosen_product}!')
    

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
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)
    ratings = crud.get_ratings_by_user(user_id);

    return render_template("user_details.html", user=user, ratings=ratings)


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
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")

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