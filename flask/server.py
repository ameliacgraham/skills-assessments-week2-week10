from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route('/')
def display_homepage():
    return render_template("index.html")

@app.route("/application-form", methods=["GET"])
def application_form():
    job_titles = ["Software Engineer", "QA Engineer", "Product Manager"]
    flash("Salary requirement must be numeric and have no commas")
    return render_template("application-form.html",
                            job_titles=job_titles)

@app.route("/application-success", methods=["POST"])
def acknowledge_application():
    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    salary_requirement = request.form.get("salary-requirement")
    job_title = request.form.get("position")
    if salary_requirement.isnumeric():
        salary_requirement = int(request.form.get("salary-requirement"))
        return render_template("application-response.html",
                       first_name=first_name,
                       last_name=last_name,
                       salary_requirement=salary_requirement,
                       job_title=job_title
                       )
    else:
        return redirect("/application-form")




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(host="0.0.0.0")
