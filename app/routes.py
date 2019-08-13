from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from github import Github
from github.GithubException import BadCredentialsException
from app.models import User
from app import app, db
from app.forms import LoginForm
from github_helper import create_repo, load_project_to_repo


@app.route("/home")
@login_required
def home():
    # print(session.get('gh_raw_data'))
    # print(session.get('gh_headers'))
    # github = Github().create_from_raw_data(
    #     klass=MainClass.Github,
    #     raw_data=session.get('gh_raw_data'),
    #     headers=session.get('gh_headers')
    # )
    # for i in github.get_user().get_repos():
    #     print(i)
    return render_template('home.html')


@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        try:
            github = Github(form.user_name.data, form.password.data)
            github_user = github.get_user()
        except BadCredentialsException as e:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            return render_template('login.html', title='Login', form=form)

        repo = create_repo(user=github_user, name='new_repo')
        load_project_to_repo(repo=repo)
        user = User(github_user=github_user.raw_data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
