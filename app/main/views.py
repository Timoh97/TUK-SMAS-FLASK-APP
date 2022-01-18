
from operator import pos
from flask import render_template,request,flash,redirect,url_for,abort
from . import main
from .. import db,photos
from ..models import *
from .forms import *
from flask_login import login_required,current_user

@main.route('/')
def index():

    posts = Post.query.order_by(Post.time_created.desc())

    return render_template('index.html',posts=posts)


@main.route('/create-post', methods=['GET','POST'])
@login_required
def create_post():
    form = PostForm()
    subscribers = Subscriber.query.all()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        post = Post(content=content, title=title, user_id=current_user.id)
        post.save_post()
        flash('Post created!', category='success')
        for subscriber in subscribers:
            mail_message('New Blog Post','email/new_post',subscriber.email,post=post)
        return redirect(url_for('.index'))

    return render_template('create_post.html',post_form=form,user=current_user)