from flask import render_template, Blueprint, request


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

@main.route('/result', methods=['POST', 'GET'])
def result_page():
    if request.method == 'POST':
        course = request.form.get('course')
        branch = request.form.get('branch')
        sem = request.form.get('semester')
        form_data = [course, branch, sem]
        return render_template('result.html', form=form_data)