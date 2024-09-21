# Added Lipids Levy
  Repo for submission to Inversity NESTA Challenge

DEPLOYMENT: https://added-lipids-levy-tool.onrender.com/

# Flask framework built off of existing projects, Inversity Learner submission was used as a start template

Summary: 
This project is the technical submission for the Inversity Challenge: ‘Burgers to broccoli? How can technology help us eat healthier and live longer?’. It functions as a web app built using Flask, which takes recipes for food items, and uses ChatGPT to analyse unnecessary ingredients that add excess amounts of fat to the food beyond what is deemed necessary to make a functional food product. Essentially, working out if the recipe designer has chosen to add excess fat in order to make the food taste nicer, at the expense of adding excess calories. The app will then assign a levy of £1 for every 250 calories generated from these excess fats. This is a tool to provide an objective yet accessible 'judge' for assessing what is/isn't considered excessive for different recipes, so that a levy could be introduced and food creators can proactively have their recipes assessed and ideally change their formulas to minimise the levy being applied - much similar to the outcome of the Soft Drinks Levy.


# File structure

app.py - This is the main flask file which contains all of the flask routes

functions_GPT.py - This contains the comprehend_data function, which is the only function in the app that calls the ChatGPT API. It contains the prompts in how ChatGPT should analyse the recipes and calculate the levy, and includes the error handling around the API calls.

functions.py - This contains the generate_results function, which is the function that uses the Flask Session variables to run comprehend_data, save results, and push to the database to save as a record. This doesn't pass any variables so it's a static function, but it is called in multiple places so was abstracted out. It contains error handling for writing to the database.

models.py - This contains the table class as needed for SQL Alchemy. This is used to define the table needed to store each record in the database for recalling at a later time.

requirements.txt - This contains details of the modules needed for the app to function.

test_GPT.py - A test script for comprehend_data function outside of the app.

templates folder - contains the HTML pages to use

- index.html - this is the homepage for the app - it links to the Recipe page and includes a brief FAQ on how to use the app.
- layout.html - this is the Jinja template used for the other html pages, key thing it conatains is a navbar for navigating the entire app.
- recipe.html - this is the page where users are asked to input their recipe and submit.
- records.html - this page displays all the records from the database and shows all the recipes submitted and results generated for each one
- results.html - this page relays to the user the results from ChatGPT, alongside their original recipe underneath.

static folder - contains static information
- favicon - this folder contains the NESTA favicon
- images - this folder contains the NESTA logo
- site.css - this page contains the custom CSS used

example_recipes folder - this folder contains a list of recipes run into comprehend_data and its results before the database was set up, so there was an audit trail of information produced.