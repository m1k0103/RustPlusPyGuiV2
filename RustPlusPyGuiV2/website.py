from flask import Flask, render_template, redirect, session, request, abort, redirect



app = Flask(__name__)
app.secret_key = "very_secret_key_that_should_be_changed_as_soon_as_possible_please_dear_user"



# handles the homepage. if user is authed, go straight to dashboard. if not, enter the base code that was set in the cfg.
@app.route("/",methods=["GET", "POST"])
def auth():
#    try:
#        session["authed"]
#    except KeyError:
#        session["authed"] = False
#
    if request.method == "GET":
        return render_template("auth.html")
    elif request.method == "POST":
        pass
    else:
        abort(404)


@app.route("/dashboard", methods=["GET"])
def dashboard():
    pass