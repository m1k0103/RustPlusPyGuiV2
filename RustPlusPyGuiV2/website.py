from flask import Flask, render_template, redirect, session, request, abort



app = Flask(__name__)



# handles the homepage. if user is authed, go straight to dashboard. if not, enter the base code that was set in the cfg.
@app.route("/",methods=["GET", "POST"])
def auth():
    if request.method == "GET":
        if session["authed"] and "authed" in session:
            pass
        pass
    elif request.method == "POST":
        pass
    else:
        abort(404)