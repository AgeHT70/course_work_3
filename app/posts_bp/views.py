from flask import render_template, Blueprint
from .dao.posts_dao import PostsDAO
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')


posts_dao = PostsDAO("./data/posts.json")


@posts_blueprint.route('/')
def main_page():
    posts = posts_dao.get_all()
    for post in posts:
        post["content"] = post["content"][:50] + "..."

    return render_template('index.html', posts=posts)


@posts_blueprint.route('/post/<int:pk>')
def post_page(pk):
    post = posts_dao.get_by_pk(pk)
    # print(post)
    return render_template('post.html', post=post)


