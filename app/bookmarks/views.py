from flask import render_template, Blueprint, request, redirect

from .dao.bookmarks_dao import BookmarksDAO
from ..posts.dao.posts_dao import PostsDAO


bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')


posts_dao = PostsDAO("./data/posts.json")
bookmarks_dao = BookmarksDAO("./data/bookmarks.json")


@bookmarks_blueprint.route('/bookmarks')
def bookmarks_page():
    posts = bookmarks_dao.get_all()
    for post in posts:
        post["content"] = post["content"][:50] + "..."
    return render_template('bookmarks.html', posts=posts)


@bookmarks_blueprint.route('/bookmarks/add/<int:post_pk>')
def add_page(post_pk):
    post = posts_dao.get_by_pk(post_pk)
    bookmarks_dao.add(post)
    return redirect("/", code=302)


@bookmarks_blueprint.route('/bookmarks/remove/<int:post_pk>')
def del_page(post_pk):
    post = posts_dao.get_by_pk(post_pk)
    bookmarks_dao.del_bookmark(post_pk)
    return redirect("/", code=302)

