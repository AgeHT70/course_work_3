from flask import render_template, Blueprint, request

from .dao.posts_dao import PostsDAO
from .dao.comments_dao import CommentsDao
from .. import bookmarks
from ..bookmarks.dao.bookmarks_dao import BookmarksDAO

# from ..bookmarks.views import bookmarks_dao

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')

posts_dao = PostsDAO("./data/posts.json")
comments_dao = CommentsDao("./data/comments.json")
bookmarks_dao = BookmarksDAO("./data/bookmarks.json")


@posts_blueprint.route('/')
def main_page():
    posts = posts_dao.get_all()
    for post in posts:
        post["content"] = post["content"][:50] + "..."

    bookmarks_len = len(bookmarks_dao.get_all())
    return render_template('index.html', posts=posts, bookmarks_len=bookmarks_len)


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


@posts_blueprint.route('/search')
def search_page():
    search_word = request.args.get('s')

    posts = posts_dao.get_by_keyword(search_word)
    for post in posts:
        post["content"] = post["content"][:50] + "..."
    count_posts = len(posts)

    return render_template('search.html', posts=posts[:10], count_posts=count_posts)
