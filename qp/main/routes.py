from flask import render_template, Blueprint


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home_page():
    return render_template('home.html')


@main.route('/about')
def about_page():
    return render_template('about.html')


@main.route('/contact')
def contact_page():
    return render_template('contact.html')