from . import main_bp
from flask import render_template, request, session, flash, redirect, url_for
from .data import TEAMS, MATCHES
TEAMS.pop(0)
from .utils import takePoints

@main_bp.route("/")
def home():
    return render_template("home.html", teams=TEAMS, matches=MATCHES[0], nextmd=1)

@main_bp.route("/matchday/<int:md>", methods=["POST", "GET"])
def nextMatchDay(md):
    if request.method == "GET":
        return render_template("home.html", teams=TEAMS, matches=MATCHES[md], nextmd=md+1)
    elif request.method == "POST":
        for teams in MATCHES[md-1]:
            indexT1 = int(TEAMS.index(teams[0]))
            indexT2 = int(TEAMS.index(teams[1]))
            scoreT1 = int(request.form[str(teams[0].name)])
            scoreT2 = int(request.form[str(teams[1].name)])
            TEAMS[indexT1].goals_for += scoreT1
            TEAMS[indexT1].goals_against += scoreT2
            TEAMS[indexT2].goals_for += scoreT2
            TEAMS[indexT2].goals_against += scoreT1
            if scoreT1 > scoreT2:
               TEAMS[indexT1].points += 3
            elif scoreT1 < scoreT2:
                TEAMS[indexT2].points += 3
            else:
                TEAMS[indexT1].points += 1
                TEAMS[indexT2].points += 1
            TEAMS.sort(key=takePoints, reverse=True)
        return redirect(url_for("main.nextMatchDay", md=md))

