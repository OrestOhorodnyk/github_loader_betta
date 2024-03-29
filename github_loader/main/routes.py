from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from github import Github
from github.GithubException import BadCredentialsException, GithubException
from github_loader import db
from github_loader.main.models import User
from github_loader.main.forms import LoginForm
from github_loader.utils.github_helper import create_repo, load_project_to_repo
from github_loader import LOGGER
from sqlalchemy.exc import SQLAlchemyError, DatabaseError

main = Blueprint('main', __name__)


@main.route("/home")
@login_required
def home():
    return render_template('home.html')


@main.route("/")
@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        try:
            github = Github(form.user_name.data, form.password.data)
            github_user = github.get_user()
            repo = create_repo(user=github_user, name='new_repo')
        except BadCredentialsException as e:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            LOGGER.error(f"Login to GitHub Failed, user: {github_user.raw_data.get('name')}, error {e}")
            return render_template('login.html', title='Login', form=form)
        except GithubException as e:
            LOGGER.error(f"An error occurred, error {e}")

        load_project_to_repo(repo=repo)
        user = User(github_user=github_user.raw_data)
        db.session.add(user)
        try:
            db.session.commit()
        except (SQLAlchemyError, DatabaseError) as e:
            LOGGER.error(f"DB error: {e} ")
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('main.home'))
    return render_template('login.html', title='Login', form=form)


@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.login'))
