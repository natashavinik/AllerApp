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
    # print_test("logged in?", logged_in_email)
    
    allergy_list = request.args.get('irritants').split(",")
    chosen_product = request.args.get('search')
    ig_by_pr = crud.get_irritantgroups_by_product(chosen_product, allergy_list)
    # print_test("product", chosen_product)
    # print_test("irritant groups in product", ig_by_pr)

    if ig_by_pr:
        culprits = crud.get_irritant_ingredient_names(ig_by_pr)
        approved = False
    else:
        culprits = None
        approved = True
    # print_test("culprits", culprits)
    
    cp_ingredients = crud.get_ingredient_names_by_product(chosen_product)
    ings = ", ".join(cp_ingredients)
    # print_test("ingredients ", ings)
   
    if logged_in_email:
        user_id = crud.get_user_by_email(logged_in_email).user_id
        for allergy in allergy_list:
            irritantgroup_id = crud.get_irritantgroup_id_by_name(allergy)
            irritantgroup = crud.create_userirritantgroup(user_id, irritantgroup_id)
            db.session.add(irritantgroup)
            db.session.commit()
        product_id = crud.get_product_id_by_name(chosen_product)

        already_searched = crud.searchedproduct_by_userid_productid(user_id, product_id)

        if not already_searched:
            searched_product = crud.create_searchedproduct(user_id=user_id, product_id = product_id, approved = approved, favorited = None)
            db.session.add(searched_product)
            db.session.commit()
            
        if ig_by_pr:
            can_have = "allergic"
            #function to find searched products allergic to = allprods
            searched_prods = crud.get_allergic_products_by_user_id(user_id)
            
        else:
            can_have = "notallergic"
            searched_prods = crud.get_notallergic_products_by_user_id(user_id)
            #function to find searched products not allergic = allprods
        def all_prods(sprod):
            return{
                "name":sprod.products.product_name,
                "id":sprod.searched_product_id

            }
        dict_userprods = list(map(all_prods, searched_prods))
        # print_test("dictionary products", dict_userprods)
        
        searched_prod = crud.searchedproduct_by_userid_productid(user_id, product_id)
        searched_prod_id = searched_prod.searched_product_id
        # print_test("searched product", searched_prod)
        # print_test("searched product id", searched_prod_id)
        
        return jsonify([{"canhave":can_have}, {"cp":searched_prod_id}, {"allprods":dict_userprods}, {"productname":chosen_product}, {"badings":culprits}, {"allings":ings}])
    else:
        if ig_by_pr:
            return (f'<div id="allergicdiv"> You <div class="d-inline" id=allergyanswer> <b>are allergic</b></div> to {chosen_product} <br> <br> These are the culprits: {culprits}</div>')
        else:
            return (f'<div id="allergicdiv">You are <div class="d-inline" id=allergyanswer><b>not allergic</b></div> to {chosen_product}!</div>')


 
@app.route('/addfavorite', methods=['GET', 'POST'])
def add_favorite():
    """adds that searched product to a users favorites/ changes the objects favorite attribute"""
    fav_obj = request.args.get('name')
    print("\n" * 4 )
    print(fav_obj)
    print("\n" * 4 )
    f_product = crud.searchedproduct_by_id(fav_obj)
    if f_product.favorited is True:
        f_product.favorited = False
    elif f_product.favorited is False:
        f_product.favorited = True
    else:
        f_product.favorited = True
    db.session.commit()
    u_id = crud.user_id_by_searchedproduct_id(fav_obj)
    u_id = u_id.user_id
    # print_test("user_id", u_id)
    user_favs = crud.get_favorite_products_by_user_id(u_id)
    # print_test("user favorites", user_favs)
    def map_favs(favorite):
        return{
            "name":favorite.products.product_name,
            "id":favorite.searched_product_id
        }    
    dict_userfavs = map(map_favs, user_favs)
    
    return jsonify(list(dict_userfavs))


@app.route('/search', methods=['POST'])
def search():
    """ Searches through products"""

    term = request.form["q"]
    print ('term: ', term)

    json_data = crud.get_product_name_list(term)

    filtered_dict = [v.product_name for v in json_data]

    resp = jsonify(filtered_dict)
    resp.status_code = 200
    return resp


@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a user."""

    user = crud.get_user_by_id(user_id)
    irritants = crud.get_irritantgroup()
    products = crud.get_product()
    user_irritantgroups = crud.get_user_irritantgroups_by_user_id(user_id)
    user_searchedproducts = crud.get_searchedproducts_by_user_id(user_id)

    return render_template("user_details.html", user=user, irritants=irritants, products=products, user_irritantgroups=user_irritantgroups, user_searchedproducts=user_searchedproducts)


@app.route("/register", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("There's already an account with that email. Try again.")
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
        flash(f"Welcome back, {user.fname}!")
        return redirect(f"/users/{user.user_id}")


@app.route ("/logout")
def log_user_out():
    """logs out user, sends to homepage"""

    session.pop('user_email')
    flash("You've been logged out.")
    return redirect('/')

 


def print_test(label, thing_to_print):
    print("\n" * 4 )
    print (label)
    print (thing_to_print)
    print("\n" * 4 )
    return


if __name__ == "__main__":
    connect_to_db(app)
    print("We're running!")
    app.run()
    