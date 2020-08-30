import os
from flask import Flask, render_template, flash, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms import MainForm
from werkzeug.utils import secure_filename
from scraper import applicant, extract_text_from_pdf

app = Flask(__name__)
app.config["SECRET_KEY"] = "516d72896e5d87cca4df6acb7caaedcc"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = [".pdf"]
app.config["UPLOAD_PATH"] = "static/resumes"


db = SQLAlchemy(app)


class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    resume = db.Column(db.String(20), nullable=False)
    score1 = db.Column(db.Integer, nullable=True)
    score2 = db.Column(db.Integer, nullable=True)
    score3 = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.email}, {self.resume}, Score 1: {self.score1}, Score 2: {self.score2}, Score 3: {self.score3}"


def get_scores(filename):
    file = open(filename, "rb")
    temp = extract_text_from_pdf(file)
    app = applicant(temp)
    return app.getWinAsOneTeam(), app.getLeadWithIntegrity(), app.getBeTheChange()
    # print(app.GPA)


@app.route("/", methods=["GET", "POST"])
def index():
    form = MainForm()
    if form.validate_on_submit():
        f = form.resume.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config["UPLOAD_PATH"], filename))
        score1, score2, score3 = get_scores(
            os.path.join(app.config["UPLOAD_PATH"], filename)
        )
        applicant = Applicant(
            first_name=form.fname.data,
            last_name=form.lname.data,
            email=form.email.data,
            resume=filename,
            score1=score1,
            score2=score2,
            score3=score3,
        )

        db.session.add(applicant)
        db.session.commit()
        flash(
            "Thank you for your submission, we will be emailing you shortly!", "success"
        )
    else:
        flash("There was an error with your submission", "danger")
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.debug = True
    app.run()
