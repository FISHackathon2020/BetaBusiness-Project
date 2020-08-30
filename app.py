from flask import Flask, render_template, flash, url_for
from forms import MainForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '516d72896e5d87cca4df6acb7caaedcc'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MainForm()
    if form.validate_on_submit():
        flash('Thank you for your submission, we will be emailing you shortly!', 'success')

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.debug = True
    app.run()
