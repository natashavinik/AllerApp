# AllerApp
AllerApp helps people feel safe about what products they are using in their body. Allerap allows users to look up personal care products (shampoos, soaps, skincare, etc.), select which ingredients they want to avoid or are allergic to, and find out if the product is safe for them. 

## Table of Contents 📖
* [Tech Stack](#techstack)
* [Features](#features)
* [Set-Up](#setup)
* [Future Improvements](#futureimprovements)
* [About Me](#aboutme)

## <a name="techstack"></a>Tech Stack 🤖
* Backend: Python, Flask, SQL, PostgreSQL, SQLAlchemy
* Frontend: Javascript, HTML, CSS, Bootstrap, AJAX, JSON, Jinja2
* Other: Scrapy (used for data-scraping)

## <a name="features"></a>Features 🙌
🎥 [See a full video walk-through](https://youtu.be/GplYq6jrtfQ)

#### Homepage
* Users select ingredients to avoid, and using the autocomplete dropdown list, select the product they want to test
* The result will return if the user is allergic to the product or not, and if they are, it will display the offending ingredients.
* Products were scraped from the web using Scrapy
* Users can register or log-in for more features
![AllerApp Homepage](/static/readmegifs/AllerAppHomepage.gif)

### User Page
* A logged in user has their allergy profile pre-populated for them when they search for a product.
* If they are allergic to it, an offcanvas comes up showing the full list of ingredients and the offending ingredients.
![AllerApp User Page](/static/readmegifs/AllerAppUserPage.gif)

#### User Page - Safe & Unsafe Products
* Whenever a logged in user searches a product, it is immediately added to and displayed in the users safe and unsafe products list. This makes it easy for the user to see products they've already searched that they can or cant have.
![AllerApp Safe & Unsafe Products](/static/readmegifs/AllerAppSafeUnsafe.gif)

#### User Page - Favorited Products
* Clicking the "Add" button on any of the user's listed Safe Products will add the product to the user's favorite products list. 
* Hitting the Remove button on a product in the favorite list will remove it from the favorites list. 
![AllerApp Favorited Products](/static/readmegifs/AllerAppFavorited.gif)

## <a name="setup"></a>Set Up 🛠
To run this project, clone or fork this repo:
```
git clone https://github.com/natashavinik/AllerApp.git
```
Create and activate a virtual environment inside your directory
```
virtualenv env
source env/bin/activate
```
Install the dependencies:
```
pip3 install -r requirements.txt
```
Set up the database:
(This will take a bit of time, grab some coffee or a treat)
```
python3 seed_database.py
```
Run the app:
```
python3 server.py
```
You can now navigate to 'localhost:5000/' to access AllerApp

## <a name="futureimprovements"></a>Future Improvements 💫
* Remake this in React
* Add more options for ingredients to avoid
* Let the user manually input ingredients to avoid
* Set up a barcode scanner so that a user can quickly scan a product at a store to see if they can use it or not
* Passcode encryption for more security

## <a name="aboutme"></a>About Me 🙌 
Hello! I'm Natasha and i'm a software engineer by day, comedian by night. I created AllerApp in four weeks as my capstone project for Hackbright, a full-stack software engineering bootcamp. I'd love to connect with you on [LinkedIn](https://www.linkedin.com/in/natashavinik/)!