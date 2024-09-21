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
from sqlalchemy.exc import SQLAlchemyError

# Load environment variables from .env file
load_dotenv()

def generate_results():
    try:

        # Error handling for ChatGPT inside here
        session['results'] = comprehend_data(session['recipe']) # Reset results

        # Create a new ChatHistory record
        new_chat = ChatHistory(prompt=session['recipe'], response=session['results'])

        # Try to add and commit the record to the database
        try:
            # Adding a record to database
            db.session.add(new_chat)
            db.session.commit()

        except SQLAlchemyError as db_err:
            db.session.rollback()  # Rollback if there is an error
            print(f"Database error: {str(db_err)}")
            # You can log this error or set a flag here if needed
            session['db_error'] = "There was an error saving the result to the database."

    except Exception as e:
        # Catch any other unexpected errors
        print(f"Unexpected error: {str(e)}")
        session['results'] = "An unexpected error occurred while processing the results."