from flask import Flask, render_template, request, url_for, redirect, session, flash
import os
from flask_session import Session
# from functions import extract_github_details, fetch_github_repo_contents, read_text_file
from functions_GPT import comprehend_data
from requests.exceptions import RequestException
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Development config: connection string for local 

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DEV_DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from models import ChatHistory

# Ensure the tables are created when the app starts if they don't already exist in the database
with app.app_context():
    db.create_all()


'''
TODO: Add tasks
'''

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/recipe", methods=['GET', 'POST'])
def recipe():
    if request.method == 'POST':
        session['recipe'] = request.form.get('recipe')

        # print(session['recipe'])

        return redirect("/results")

    return render_template("recipe.html")


@app.route("/results", methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        session['results'] =  comprehend_data(session['recipe'])
        # Create a new ChatHistory record
        new_chat = ChatHistory(prompt=session['recipe'], response=session['results'])
        
        # Add and commit the record to the database
        db.session.add(new_chat)
        db.session.commit()

        return redirect("/results")

    else:

        # Safely check if 'recipe' exists in the session and if 'results' exists
        recipe = session.get('recipe')
        results = session.get('results')

        # Handle the case where the recipe is found
        if recipe:
            if results:
                return render_template("results.html", recipe=recipe, results=results)
            else:
                return render_template("results.html", recipe=recipe, results='No results generated yet')
        
        # Handle the case where the recipe is not found
        else:
            return render_template("results.html", recipe='No recipe entered yet', results='No results generated yet')        
    

@app.route("/records", methods=['GET'])
def records():
    records = ChatHistory.query.all()
    return render_template("records.html", records=records)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port)