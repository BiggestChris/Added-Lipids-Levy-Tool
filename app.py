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
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port)