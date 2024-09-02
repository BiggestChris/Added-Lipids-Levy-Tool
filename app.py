from flask import Flask, render_template, request, url_for, redirect, session, flash
import os
from flask_session import Session
# from functions import extract_github_details, fetch_github_repo_contents, read_text_file
# from functions_GPT import comprehend_data
from requests.exceptions import RequestException

app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


'''
TODO: ADd tasks
'''

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/recipe", methods=['GET', 'POST'])
def recipe():
    if request.method == 'POST':
        session['recipe'] = request.form.get('recipe')

        print(session['recipe'])

        return redirect("/results")

    return render_template("recipe.html")


@app.route("/results", methods=['GET'])
def results():
    # Safely check if 'recipe' exists in the session
    recipe = session.get('recipe')
    if recipe:
        # Handle the case where the recipe is found
        return render_template("results.html", recipe=recipe)
 
    else:
        # Handle the case where the recipe is not found
        return render_template("results.html", recipe='No recipe entered yet')        
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port)