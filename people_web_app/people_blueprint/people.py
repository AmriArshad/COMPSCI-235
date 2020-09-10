from flask import Blueprint, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

import people_web_app.adapters.repository as repo

people_blueprint = Blueprint(
    'people_bp', __name__
)


@people_blueprint.route('/')
def home():
    return render_template(
        'home.html',
        find_person_url = url_for('people_bp.find_person'),
        list_people_url = url_for('people_bp.list_people')
    )


@people_blueprint.route('/list')
def list_people():
    return render_template(
        'list_people.html',
        people = repo.repo_instance,
        find_person_url = url_for('people_bp.find_person'),
        list_people_url = url_for('people_bp.list_people')
        )


@people_blueprint.route('/find', methods = ['GET', 'POST'])
def find_person():
    form = SearchForm()

    if form.validate_on_submit():
        post_id = form.person_id

        for person in repo.repo_instance:
            if post_id.data == person.id_number:
                return render_template(
                    'list_person.html',
                    person = person,
                    find_person_url = url_for('people_bp.find_person'),
                    list_people_url = url_for('people_bp.list_people')
                    )

        return render_template(
            'list_person.html',
            person = None,
            find_person_url = url_for('people_bp.find_person'),
            list_people_url = url_for('people_bp.list_people')
            )
    
    return render_template(
        'find_person.html',
        title = 'Search',
        form = form,
        handler_url = url_for('people_bp.find_person'),
        find_person_url = url_for('people_bp.find_person'),
        list_people_url = url_for('people_bp.list_people')        
        )


class SearchForm(FlaskForm):
    
    person_id = IntegerField('Person id')
    submit = SubmitField('Find')
