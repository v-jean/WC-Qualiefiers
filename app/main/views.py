from . import main_bp
from flask import render_template, request, session, flash, redirect

@main_bp.route("/")
def home():
    return render_template("home.html")