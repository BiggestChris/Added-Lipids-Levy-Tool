import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from functions_GPT import comprehend_data
from models import ChatHistory
from app import db
from flask import Flask, render_template, request, url_for, redirect, session, flash
import os
from flask_session import Session

# Load environment variables from .env file
load_dotenv()

def generate_results():
    # TODO: Error handling - Calling ChatGPT so need error handling here (either in function or outside)
    session['results'] = comprehend_data(session['recipe']) # Reset results

    # Create a new ChatHistory record
    new_chat = ChatHistory(prompt=session['recipe'], response=session['results'])

    # Add and commit the record to the database
    # TODO: Error handling - Adding a record to database so need error handling
    db.session.add(new_chat)
    db.session.commit()