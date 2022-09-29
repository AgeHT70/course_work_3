from flask import render_template, Blueprint

from .dao.posts_dao import PostsDAO
from .dao.comments_dao import CommentsDao


posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')


posts_dao = PostsDAO("./data/posts.json")
comments_dao = CommentsDao("./data/comments.json")


@posts_blueprint.route('/')
def main_page():
    posts = posts_dao.get_all()
    for post in posts:
        post["content"] = post["content"][:50] + "..."

    return render_template('index.html', posts=posts)


@posts_blueprint.route('/post/<int:pk>')
def post_page(pk):
    post = posts_dao.get_by_pk(pk)
    comments = comments_dao.get_by_post_pk(pk)
    comments_count = len(comments)

    return render_template('post.html', post=post, comments=comments, comments_count=comments_count)


@posts_blueprint.route('/users/<username>')
def user_page(username):
    posts = posts_dao.get_by_username(username)
    for post in posts:
        post["content"] = post["content"][:50] + "..."

    return render_template('user-feed.html', user_posts=posts)


